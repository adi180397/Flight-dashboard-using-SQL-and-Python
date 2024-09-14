import streamlit as st
import pandas as pd
import mysql.connector
import os
from dotenv import load_dotenv
load_dotenv()
from langchain_groq import ChatGroq
from langchain.agents import create_sql_agent
from langchain.sql_database import SQLDatabase
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.agents.agent_types import AgentType
from sqlalchemy import create_engine
from langchain.callbacks import StreamlitCallbackHandler

# Load the API key from environment variables
groq_api_key = os.getenv('GROQ_API_KEY')

# Streamlit UI
st.title('Chat with your Database')
st.sidebar.subheader('Connect to your Database')

# User inputs for database connection
host = st.sidebar.text_input('Enter host name', key="host")
user = st.sidebar.text_input('Enter user name', key="user")
password = st.sidebar.text_input('Enter your password', type='password', key="password")
db = st.sidebar.text_input('Enter Database name', key="db")

# Set up the ChatGroq model
llm = ChatGroq(groq_api_key=groq_api_key, model_name="gemma2-9b-it", temperature=0.7)

# Function to configure the database connection
@st.cache_resource
def configure(host=None, user=None, password=None, db=None):
    try:
        return SQLDatabase(create_engine(f"mysql+mysqlconnector://{user}:{password}@{host}/{db}"))
    except Exception as e:
        st.error(f"Error connecting to the database: {e}")
        return None

# Initialize my_db in session_state
if "my_db" not in st.session_state:
    st.session_state.my_db = None

# Connect to the database when the button is clicked
if st.sidebar.button('Connect'):
    st.session_state.my_db = configure(host, user, password, db)
    if st.session_state.my_db:
        st.success('Connected to the database')
    else:
        st.error('Failed to connect. Please check your credentials.')

# Only proceed if the database connection has been made
if st.session_state.my_db:
    toolkit = SQLDatabaseToolkit(db=st.session_state.my_db, llm=llm)

    # Create the agent
    agent = create_sql_agent(
        llm=llm,
        toolkit=toolkit,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=False
    )

    # Clear messages history
    if "messages" not in st.session_state or st.sidebar.button("Clear message history"):
        st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

    # Display previous messages
    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    # User input for query
    user_query = st.chat_input(placeholder="Ask anything from the database")

    if user_query:
        st.session_state.messages.append({"role": "user", "content": user_query})
        st.chat_message("user").write(user_query)

        with st.chat_message("assistant"):
            streamlit_callback = StreamlitCallbackHandler(st.container())
            response = agent.run(user_query, callbacks=[streamlit_callback])
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.write(response)
