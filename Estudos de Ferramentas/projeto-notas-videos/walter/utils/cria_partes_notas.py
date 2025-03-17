import os
import re

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()


PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))


class Notes:
    
    def __init__(self):
        self.llm = ChatOpenAI(model='gpt-4o-mini', temperature=0)
    
    def cria_tags(self, texto):
        """Cria tags referentes ao texto."""
        tags = self.llm.invoke(f"""Crie até 10 tags referentes a este texto: \n{texto}\n
            Voce deve responder apenas as tags, sem nenhum comentario, nem numeração
            as tags devem estar alinhadas em uma unica linha, separadas por um espaço
            Elas devem ser relacionadas apenas ao conteudo do texto
            por exemplo, um texto que fale sobre filosofia pode ter a tag #filosofia
            outro exemplo, um texto que fale sobre treino de academia pode ter as tags #fitness #health
            todas a tags devem ter # na frente, por exemplo: #exemplo
        """)
        return tags.content

    def cria_resumo_curto(self, texto):
        """Cria um resumo curto de até 20 palavras da Transcrição"""
        resumo_curto = self.llm.invoke(f"Crie um resumo do texto em 20 palavras: \n{texto}")
        return resumo_curto.content

    def cria_resumo_detalhado(self, texto):
        """Cria um resumo detalhado da Transcrição"""
        resumo_detalhado= self.llm.invoke(f"""
            Resuma detalhadamente o texto:  \n{texto}\n
            mantendo todas as informações importantes de forma estruturada
            o Resumo deve conter todas as informações para que uma pessoa que não leu o texto orignal possa entender por completo
        f""")
        return resumo_detalhado.content

    def cria_bullet_point(self, texto):
        """Cria um bullet point baseado na Transcrição"""
        bullet_point = self.llm.invoke(f"""
            Liste em bullet points as principais ideias referentes ao texto: \n{texto}
        """)
        return bullet_point.content

    def formata_nota(self, tags, resumo_curto, resumo_detalhado, bullet_point):
        """Formata os textos em uma unica nota com título, #tags, os resumos."""
        texto_final = f"""
            {tags}\n\n
            ## Resumo Curto\n{resumo_curto}\n\n
            ## Resumo Detalhado\n{resumo_detalhado}\n\n
            ## Bullet Points\n{bullet_point}\n\n
        """
        return texto_final

    def salvar_nota(self, transcricao_path):
        """Salva o texto em um arquivo de texto no diretório _notas."""
        print('Criando texto da Nota')
        
        transcricao_path = transcricao_path.replace("'", "")
        print(f'1transcricao_path {transcricao_path}')

        with open(transcricao_path, "rb") as file:
            transcricao = file.read()
            tags = self.cria_tags(transcricao)
            resumo_curto = self.cria_resumo_curto(transcricao)
            resumo_detalhado = self.cria_resumo_detalhado(transcricao)
            bullet_point = self.cria_bullet_point(transcricao)
            nota = self.formata_nota(tags, resumo_curto, resumo_detalhado, bullet_point)
            print ('nota criada\n\n')

        output_path = os.path.join(PROJECT_DIR, 'transcricoes', 'notas')
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        
        base_name = os.path.splitext(os.path.basename(transcricao_path))[0]
        resumo_path = os.path.join(output_path, f'{base_name}.md')
        with open(resumo_path, 'w') as f:
            f.write(nota)
        print(f"Nota salva em: {resumo_path}")

