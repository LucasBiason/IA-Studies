import pytesseract
import base64
import os
from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain_community.tools import CopyFileTool
from langchain_openai import ChatOpenAI
from langchain_core.prompts.chat import HumanMessagePromptTemplate, MessagesPlaceholder
from langchain_core.prompts.chat import ChatPromptTemplate
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
from pydantic import BaseModel, Field

from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_openai import ChatOpenAI
from pdf2image import convert_from_path

load_dotenv()

class ProcessImage:
        
    def __init__(self):
        openai_api_key = os.getenv("OPENAI_API_KEY")
        self.llm = ChatOpenAI(
            model='gpt-4o-mini',
            temperature=0,
            openai_api_key=openai_api_key
        )

    def openai_analysis(self, image_path):
        with open(image_path, "rb") as image_file:
            base64_image = base64.b64encode(image_file.read()).decode("UTF-8")
            
        prompt = ChatPromptTemplate.from_messages(
            messages=[
                HumanMessage(content="""
                    Dada a imagem fornecida, extraia os dados importantes dela e retorne no seguinte formato:
                    - Empresa : nome da empresa que emitiu o recibo
                    - Tipo: tipo da despesa baseada nos itens comprados
                    - Itens: 
                        - Descrição: nome ou descrição da mercadoria
                        - Valor Unitário: valor unitário da mercadoria
                        - Quantidade: quantidade da mercadoria
                        - Valor Total: valor total da mercadoria
                    - Total: valor total da compra
                    - Desconto: valor do desconto
                    - Valor Pago: valor pago
                    Retorne os dados no formato JSON com nomes dos campos em snake_case.
                    {text}
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
        response = result['output'] 
    
        print(response)
        return response


print("== recibo001.png =================================")
ProcessImage().openai_analysis('../recursos/images/recibo001.png')
print("== recibo002.png =================================")
ProcessImage().openai_analysis('../recursos/images/recibo002.png')
print("== recibo003.png =================================")
ProcessImage().openai_analysis('../recursos/images/recibo003.png')
print("== recibo004.png =================================")
ProcessImage().openai_analysis('../recursos/images/recibo004.png')
print("== recibo005.png =================================")
ProcessImage().openai_analysis('../recursos/mages/recibo005.png')