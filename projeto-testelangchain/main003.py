

# DuckDuckGoSearchRun
from langchain_community.tools import DuckDuckGoSearchRun
ddg_search = DuckDuckGoSearchRun()
search_result = ddg_search.run('Quem foi Alan Turing?')
print(search_result)

# PythonREPL
from langchain_experimental.utilities import PythonREPL
python_repl = PythonREPL()
result = python_repl.run('print(5 + 5)')
print(result)

# WikipediaQueryRun
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
wikipedia = WikipediaQueryRun(
    api_wrapper=WikipediaAPIWrapper(lang='pt')
)
wikipedia_results = wikipedia.run('Quem foi Alan Turing?')
print(wikipedia_results)

