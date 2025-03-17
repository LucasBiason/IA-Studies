import os
import requests
import sqlite3

from bs4 import BeautifulSoup

from langchain import hub
from langchain.agents import create_react_agent, AgentExecutor
from langchain.prompts import PromptTemplate
from langchain_community.utilities.sql_database import SQLDatabase
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from langchain_openai import ChatOpenAI
from langchain.tools.sql_database.tool import QuerySQLDataBaseTool, InfoSQLDatabaseTool

from dotenv import load_dotenv
load_dotenv()
os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY")


class IPCARepository:
    DB_NAME = 'ipca.db'
    
    def __init__(self):
        self.create_table()
        
    def create_table(self):
        conn = sqlite3.connect(self.DB_NAME)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS IPCA (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                value REAL,
                month TEXT,
                year INTEGER,
                UNIQUE(month, year)
            )
        ''')
        conn.close()
        
    def create(self, value, month, year):
        conn = sqlite3.connect(self.DB_NAME)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT OR IGNORE INTO IPCA (value, month, year)
            VALUES (?, ?, ?)
        ''', (value, month, year))
        conn.commit()
        conn.close()


class ScrapIPCA:
    def __init__(self):
        self.response = requests.get('https://www.idealsoftwares.com.br/indices/ipca_ibge.html')
        self.html_content = self.response.content
        self.soup = BeautifulSoup(self.html_content, 'html.parser')
        self.table = self.soup.find_all(
            name='table',
            attrs={'class': 'table table-bordered table-striped text-center'},
        )[1]
        
    def get_ipca_data(self):
        ipca_data = []
        for row in self.table.find_all('tr')[1:]:
            cols = row.find_all('td')
            if cols:
                month_year = cols[0].text.strip()
                value = cols[1].text.strip()\
                    .replace(',', '.')\
                    .replace(' ', '').replace('\n', '')
                if value:
                    month, year = month_year.split('/')
                    ipca_data.append((float(value), month, int(year)))
        return ipca_data


def criar_ipca():
    ipca_data = ScrapIPCA().get_ipca_data()
    ipca_repo = IPCARepository()
    for value, month, year in ipca_data:
        ipca_repo.create(value, month, year)
    print('Dados históricos do IPCA salvos com sucesso!')


class AgentIPCA:
    BD_NAME = 'sqlite:///ipca.db'
    
    def __init__(self):
        self.db = SQLDatabase.from_uri(self.BD_NAME)
        self.model = ChatOpenAI(model='gpt-3.5-turbo')
        self.toolkit = self.create_toolkit()
        self.agent = self.create_agent()
        self.agent_executor = self.create_agent_executor()
        self.prompt_template = self.create_prompt_template()
        
    def create_toolkit(self):
        tools = [
            QuerySQLDataBaseTool(db=self.db),
            InfoSQLDatabaseTool(db=self.db)
        ]
        return tools

    def create_agent(self):
        print(hub.pull('hwchase17/react'))
        agent = create_react_agent(
            llm=self.model,
            tools=self.toolkit,
            prompt=hub.pull('hwchase17/react'),
        )
        return agent
    
    def create_agent_executor(self):
        agent_executor = AgentExecutor(
            agent=self.agent,
            tools=self.toolkit,
            verbose=True,
            handle_parsing_errors=True,
        )
        return agent_executor
    
    def create_prompt_template(self):
        prompt = '''
            Use as ferrmentas necessárias para responder perguntas relacionadas ao histórico de IPCA ao longo dos anos.
            Responda tudo em português brasileiro.
            Não invente dados, utilize apenas os dados disponíveis.
            Não providencie informações que não foram solicitadas.
            Perguntas: {q}
        '''
        prompt_template = PromptTemplate.from_template(prompt)
        return prompt_template
    
    def invoke(self, question):
        return self.agent_executor.invoke({
            'input': self.prompt_template.format(q=question),
        })
    

if __name__ == '__main__':
    criar_ipca()
    
    agent = AgentIPCA()
    while True:
        question = input('O que deseja saber sobre IPCA? ')
        if question == 'sair':
            break
        output = agent.invoke(question)
        print(output.get('output'))