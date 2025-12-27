\## 📦 Estoque GPT – Assistente Inteligente de Estoque



O \*\*Estoque GPT\*\* é uma aplicação interativa desenvolvida com \*\*Streamlit\*\* que integra um \*\*modelo de linguagem (LLM)\*\* por meio do \*\*LangChain\*\*, permitindo consultas inteligentes sobre um banco de dados de estoque. A interface foi projetada para oferecer \*\*insights rápidos e precisos\*\* sobre produtos, preços, marcas, categorias e necessidades de reposição, utilizando linguagem natural em português brasileiro.



A aplicação conecta um modelo GPT a um banco de dados \*\*SQLite\*\*, onde o agente é capaz de interpretar perguntas do usuário, decidir automaticamente quando utilizar ferramentas disponíveis e executar consultas SQL para retornar respostas organizadas e amigáveis.



\### 🔍 Funcionalidades principais



\- 💬 \*\*Consulta em linguagem natural\*\* sobre estoque de produtos  

\- 🧠 \*\*Agente ReAct com LangChain\*\*, capaz de raciocinar e utilizar ferramentas conforme o contexto da pergunta  

\- 🗄️ \*\*Integração com banco de dados SQL\*\* para consulta de produtos, marcas e categorias  

\- ⚙️ \*\*Seleção dinâmica de modelos LLM\*\* diretamente pela interface  

\- 🇧🇷 Respostas sempre em \*\*português brasileiro\*\*, formatadas para fácil visualização  



\### 🛠️ Ferramentas (Tools)



Além da ferramenta de consulta ao banco de dados de estoque, o projeto inclui uma \*\*tool personalizada para consulta do horário de funcionamento da loja\*\*.



Essa ferramenta permite responder perguntas sobre:

\- Horários de abertura e fechamento  

\- Dias de funcionamento  

\- Feriados e exceções  



> 🔎 \*\*Observação:\*\* a tool de horário da loja foi adicionada \*\*principalmente para fins demonstrativos\*\*, mostrando como novas ferramentas podem ser facilmente integradas ao agente LangChain, tornando o projeto extensível e modular.



\### 🚀 Objetivo do projeto



O objetivo do \*\*Estoque GPT\*\* é demonstrar como combinar \*\*Streamlit + LangChain + LLMs\*\* para criar um assistente inteligente orientado a dados, com arquitetura flexível para expansão futura, seja com novas ferramentas, novas fontes de dados ou novos fluxos de negócio.



