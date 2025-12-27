import os
import streamlit as st

from decouple import config

from langchain_classic import hub
from langchain_classic.agents import create_react_agent, AgentExecutor
from langchain_core.prompts import PromptTemplate
from langchain_community.utilities.sql_database import SQLDatabase
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from langchain_openai import ChatOpenAI

from langchain_classic.tools import Tool
from tools.horario_loja import consultar_horario_loja


os.environ['OPENAI_API_KEY'] = config('OPENAI_API_KEY')

st.set_page_config(
    page_title='Estoque GPT',
    page_icon='📄',
)
st.header('Assistente de Estoque')

model_options = [
    'gpt-3.5-turbo',
    'gpt-4',
    'gpt-4-turbo',
    'gpt-4o-mini',
    'gpt-4o',
]
selected_model = st.sidebar.selectbox(
    label='Selecione o modelo LLM',
    options=model_options,
)

st.sidebar.markdown('### Sobre')
st.sidebar.markdown('Este agente consulta um banco de dados de estoque utilizando um modelo GPT.')

st.write('Faça perguntas sobre o estoque de produtos, preços e reposições.')
user_question = st.text_input('O que deseja saber sobre o estoque?')

# seleciona o modelo de llm
model = ChatOpenAI(
    model=selected_model,
)

# conexão com db
db_estoque = SQLDatabase.from_uri(
    "sqlite:///estoque.db",
    include_tables=["products_product", "brands_brand", "categories_category"]
)

# ----------------------  START - TOOLS  ----------------------------------------- #
# tool para acessar database
toolkit_estoque = SQLDatabaseToolkit(
    db=db_estoque,
    llm=model,
)
tool_estoque = toolkit_estoque.get_tools()

# tool para consultar horarios de loja
horario_tool = Tool(
    name="consultar_horario_loja",
    func=consultar_horario_loja,
    description="""
    Use esta ferramenta para responder perguntas sobre
    horário de funcionamento da loja, dias abertos,
    feriados e exceções de funcionamento.
    """
)
# ----------------------  END - TOOLS  ----------------------------------------- #

tools = tool_estoque + [horario_tool]
system_message = hub.pull('hwchase17/react')

agent = create_react_agent(
    llm=model,
    tools=tools,
    prompt=system_message,
)

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
    #handle_parsing_errors=True
)

prompt = """
Você é um agente que responde perguntas sobre estoque de produtos.

REGRAS IMPORTANTES:
- Use as ferramentas disponíveis quando necessário.
- Siga EXATAMENTE o formato esperado pelo agente.
- NÃO responda diretamente ao usuário até chegar à resposta final.
- NÃO explique o que você está fazendo.
- A resposta final deve ser clara, organizada e amigável para visualização.
- Sempre responda em português brasileiro.
- Use a ferramenta de estoque para verificar dados sobre perguntas de estoque
- Use a ferramenta de horário sempre que a pergunta for sobre funcionamento da loja, dias abertos ou feriados.
  Quando o usuário mencionar datas relativas como:
   - hoje
   - ontem
   - amanhã
   - próxima segunda, sexta etc.
  Converta SEMPRE para uma data absoluta no formato YYYY-MM-DD
  antes de chamar qualquer ferramenta.


Pergunta do usuário:
{q}
"""

prompt_template = PromptTemplate.from_template(prompt)

if st.button('Consultar'):
    if user_question:
        with st.spinner('Consultando o banco de dados...'):
            formatted_prompt = prompt_template.format(q=user_question)
            output = agent_executor.invoke({'input': formatted_prompt})
            st.markdown(output.get('output'))
    else:
        st.warning('Por favor, insira uma pergunta.')
