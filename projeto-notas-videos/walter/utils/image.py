import base64
import os

from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain_community.tools import CopyFileTool
from langchain_openai import ChatOpenAI
from langchain_core.prompts.chat import HumanMessagePromptTemplate, MessagesPlaceholder
from langchain_core.prompts.chat import ChatPromptTemplate
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv


load_dotenv()


PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))


class ProcessImage:
    
    def __init__(self):
        openai_api_key = os.getenv("OPENAI_API_KEY")
        self.llm = ChatOpenAI(
            model='gpt-4o-mini', 
            temperature=0,  
            openai_api_key=openai_api_key
        )
    
    def openai_analysis(self, image_path):
        """
        Analisa imagem, e descreve detalhadamente seu conteudo.
        Caso ela possua textos, transcreve em formato markdown.
        """
        with open(image_path, "rb") as image_file:
            base64_image = base64.b64encode(image_file.read()).decode("UTF-8")

        prompt = ChatPromptTemplate.from_messages(
            messages=[
                HumanMessage(content="""
                    Analise a imagem, e descreva detalhadamente seu conteudo.
                    Caso ela possua textos, transcreva-os em formato markdown.
                """),
                 HumanMessagePromptTemplate.from_template(
                    template=[
                        {"type": "image_url", "image_url": {"url": "{image_url}"}},
                    ]
                ),
                MessagesPlaceholder("agent_scratchpad"),
            ]
        )

        tools = [CopyFileTool()]
        agent = create_openai_tools_agent(self.llm, tools, prompt)
        agent_executor = AgentExecutor(
            agent=agent,
            tools=tools,
        )
        result = agent_executor.invoke({"image_url": f"data:image/jpeg;base64,{base64_image}", "agent_scratchpad": []})
        return result['output']
    
    def save_file_transcription(self, image_path):
        transcricao = self.openai_analysis(image_path)
        
        output_path = os.path.join(PROJECT_DIR, 'transcricoes')
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        base_name = os.path.splitext(os.path.basename(image_path))[0]
        transcricao_path = os.path.join(output_path, f'{base_name}.md')
        with open(transcricao_path, 'w') as f:
            f.write(transcricao.strip())
        return transcricao_path
 