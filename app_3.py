from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import create_sql_agent
from langchain_groq import ChatGroq
import traceback
import os 
from dotenv import load_dotenv
load_dotenv()
os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")


def create_agent():
      db = SQLDatabase.from_uri("sqlite://Classroom.db")
 
      llm = ChatGroq(
            model = "llama-3.3-70b-versatile"
      )

      agent = create_sql_agent(
            llm = llm,
            verbose=True,
            db=db,
            agent_type="tool-calling", 
      )
      return agent

agent = create_agent()
while (True):
      user_input = input("user:")
      if user_input.lower() in ["quit","exit"]:
            print("bye bye bye")
            break;
      try:
            response = agent.invoke({"input":user_input})
            print(response)
      
      except:
            traceback.print_exc()