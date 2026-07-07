# Chat_with_SQL_DB
AI-powered SQL chatbot built with LangChain Agent Toolkit that converts natural language into SQL queries and retrieves answers from SQLite databases using LLMs.

An AI-powered application that enables users to interact with SQL databases using natural language. Instead of writing SQL queries manually, users can ask questions in plain English, and the application uses a LangChain SQL Agent to generate, execute, and return accurate results from the database.

 Features

* Natural language to SQL query generation
* LangChain SQL Agent Toolkit integration
* Support for SQLite databases
* LLM-powered query reasoning
* Interactive chat interface
* Error handling for invalid or ambiguous queries

 Tech Stack

* Python
* LangChain
* LangChain SQL Agent Toolkit
* SQLite
* Streamlit
* Groq/OpenAI-compatible LLM
* SQLAlchemy

 How It Works

1. The user enters a question in natural language.
2. The LangChain SQL Agent analyzes the database schema.
3. The agent generates the appropriate SQL query.
4. The query is executed on the database.
5. The results are returned in a conversational format.

This project demonstrates how Large Language Models can be combined with agent-based reasoning to build intelligent interfaces for structured databases.
