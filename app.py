import streamlit as st
from pathlib import Path
from langchain.agents import create_sql_agent
from langchain.sql_database import SQLDatabase
from langchain.callbacks import StreamlitCallbackHandler
from langchain.agents.agent_types import AgentType
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from sqlalchemy import create_engine
import sqlite3
from langchain_groq import ChatGroq

st.set_page_config(page_title="Langchain: Chat with SQL Database",page_icon="parrot")
st.title("Langchain: Chat with SQL")

LOCALDB = "USE_LOCALDB"
MYSQL =  "USE_MYSQL"

radio_opt= ["use sql lite database = student.db","Connect to your database"]
selectd_opt = st.sidebar.radio(label="Choose the db which you want to use",options=radio_opt)

if radio_opt.index(selectd_opt) ==1:
    db_uri = MYSQL
    mysql_host = st.sidebar.text_input("give MYSQL HOST")
    mysql_user = st.sidebar.text_input("give MYSQL USER")
    mysql_password = st.sidebar.text_input("give MYSQL PASSWORD",type="password")
    mysql_db = st.sidebar.text_input("give MYSQL DATABASE")
    
else:
    db_uri = LOCALDB
    
api_key = st.sidebar.text_input(label = "GROQ API KEY",type='password')

if not db_uri:
    st.info("please enter the information")
    
if not api_key:
    st.info("please add the groq key")
    
    
llm = ChatGroq(groq_api_key=api_key,model_name ="gemma2-9b-it",streaming=True)

@st.cache_resource(ttl="2h")
def configure_db(db_uri,mysql_host=None,mysql_user=None,mysql_password=None,mysql_db=None):
    if db_uri ==LOCALDB:
        dbfile_path = (Path(__file__).parent/"temp_student.db").absolute()
        print(dbfile_path)
        creator =  lambda:sqlite3.connect(f"file:{dbfile_path}?mode=ro",uri=True)
        return SQLDatabase(create_engine("sqlite:///",creator=creator))
    
    elif db_uri == MYSQL:
        if not (mysql_db and mysql_host and mysql_user and mysql_password):
            st.error("Please enter the database details")
             
            st.stop()
             
        return SQLDatabase(create_engine(f"mysql+mysqlconnector://{mysql_user}:{mysql_password}@{mysql_host}/{mysql_db}"))
    

if db_uri == MYSQL:
    db = configure_db(db_uri,
                      mysql_host=mysql_host,
                      mysql_user=mysql_user,
                      mysql_password=mysql_password,
                      mysql_db=mysql_db)
    
else:
    db = configure_db(db_uri)

toolkit = SQLDatabaseToolkit(db = db,llm = llm)

agent = create_sql_agent(
    llm= llm,
    toolkit=toolkit,
    verbose=True,
    Agent_type = AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    handle_parsing_errors=True
    )

if "messages" not in st.session_state or st.sidebar.button("Clear chat history"):
    st.session_state["messages"] =[{"role":"assistant", "content":"How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])
    
    
user_query = st.chat_input(placeholder="Ask a question about your database")

if user_query:
    st.session_state.messages.append({"role":"user","content":user_query})
    st.chat_message("user").write(user_query)
    
    with st.chat_message("assistant"):
        streamlit_callback = StreamlitCallbackHandler(st.container())
        response = agent.run(user_query, callbacks=[streamlit_callback])
        st.session_state.messages.append({"role":"assistant","content":response})
        st.write(response)