from langchain.agents import (
    AgentExecutor,
    create_tool_calling_agent
)
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import Tool
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from .tools import WalterTools

load_dotenv()


class Walter:
    
    def __init__(self):
        self.agent_tools_class = WalterTools
        self.create_agent()
    
    def create_llm_model(self):
        self.llm = ChatOpenAI(model='gpt-4o-mini', temperature=0)
        return self.llm
        
    def create_agent_tools(self):
        self.tools = [
            Tool(
                name="baixar_video_youtube", 
                func=self.agent_tools_class.baixar_video_youtube, 
                description="Baixa vídeo do YouTube e retorna seu título, autor e descrição."
            ),
            Tool(
                name="extrair_audio_video", 
                func=self.agent_tools_class.extrair_audio, 
                description="Extrai o áudio de um arquivo MP4."
            ),
            Tool(
                name="descrever_imagem", 
                func=self.agent_tools_class.descreve_imagem, 
                description="Analisa o image_path e retorna uma descrição detalhada. Caso a imagem contenha texto, ele será transcrito."
            ),
            Tool(
                name="transcrever_audio", 
                func=self.agent_tools_class.transcrever_audio, 
                description="Transcreve um arquivo de áudio salvo em audio_path para texto utilizando reconhecimento de fala."
            ),
            Tool(
                name="salvar_nota", 
                func=self.agent_tools_class.salvar_nota, 
                description="Salva o texto em um arquivo de texto no diretório notas."
            ),
        ]
        return self.tools
    
    def create_agent_prompt_template(self):
        self.prompt_template = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    """
                    Você é um assistente especializado em ajudar os usuários a criar notas detalhadas e completas.
                    Você auxilia extraindo as informações principais, 
                    organizando-as em pontos estruturados e garantindo que as notas finais sejam abrangentes.
                    Sempre resuma as informações de maneira clara e concisa.
                    Mantenha o controle dos resultados das ferramentas e incorpore-os às notas conforme necessário.
                    O resultado final deve estar em português brasileiro e formatado em Markdown.
                    """

                ),
                ("placeholder", "{chat_history}"),
                ("human", "{input}"),
                ("placeholder", "{agent_scratchpad}"),
            ]
        )
        return self.prompt_template

    def create_agent(self):
        self.create_llm_model()
        self.create_agent_prompt_template()
        self.create_agent_tools()
        self.agent = create_tool_calling_agent(
            llm=self.llm,
            tools=self.tools,
            prompt=self.prompt_template,
        )
        return self.agent, self.tools

    def process_message(self, msg):
        agent_executor = AgentExecutor.from_agent_and_tools(
            agent=self.agent,
            tools=self.tools,
            verbose=True,
        )
        executor_prompt = {"input": f"""
            Identifique o tipo de arquivo da mensagem e utilize as tools para criar uma nota.
             - se for um link do youtube: baixe o video, extraia o audio do video baixado, transcreva o audio do audio extraido então salve a nota da transcrição
             - se for um arquivo mp4: extraia o audio do video, transcreva o audio do audio extraido então salve a nota da transcrição
             - se for um arquivo mp3 ou ogg: transcreva o audio então salve a nota da transcrição
             - se for um arquivo de imagem: descreva a imagem e seu conteudo e salve a nota a partir de sua transcrição
            a mensagem é: {msg}
        """}
        resultado = agent_executor.invoke(executor_prompt)
        return resultado
