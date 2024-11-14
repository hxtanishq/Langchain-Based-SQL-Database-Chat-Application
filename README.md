# Langchain-Based-SQL-Database-Chat-Application


Langchain-Based SQL Database Chat Application
Introduction
This project is a Streamlit-based chat application that allows users to interact with a SQL database using the Langchain framework. The application leverages the power of Langchain, a Python library that simplifies the development of large language model (LLM) applications, to provide a natural language-based interface for querying and interacting with a MySQL database.
Features

Natural Language Interface: Users can ask questions and issue commands to the application using natural language, and the application will translate those inputs into appropriate SQL queries.
Contextual Awareness: The application maintains session-level context, allowing users to ask follow-up questions or build upon previous interactions.
Database Connectivity: The application connects to a MySQL database using the provided credentials, allowing users to access and manipulate data stored within the database.
Streamlit-based UI: The application features a clean and intuitive Streamlit-based user interface, making it easy for users to interact with the application.

Technologies Used

Langchain: A Python library that simplifies the development of LLM applications, providing a set of abstractions and tools for building conversational AI systems.
GROQ API: A GraphQL-like API that allows for powerful and flexible querying of data stored in a MySQL database.
MySQL: A popular open-source relational database management system (RDBMS) used to store the data accessed by the application.
Streamlit: A Python library that enables the rapid development of interactive web applications, used to create the user interface for this project.

Getting Started
To use the Langchain-Based SQL Database Chat Application, follow these steps:

### Clone the Repository: Start by cloning the project repository to your local machine.
### Set up the Environment: Create a new virtual environment and install the required dependencies by running pip install -r requirements.txt.
#### Configure the Database Connection: Update the config.py file with the appropriate MySQL database credentials and connection details.
#### Run the Application: Launch the Streamlit application by running  streamlit run app.py.
#### Interact with the Chat Interface: Once the application is running, you can start asking questions and issuing commands to the chat interface. 
The application will handle the translation of natural language inputs into SQL queries and provide the corresponding results.



User: What are the total sales for the last 30 days?
Assistant: To get the total sales for the last 30 days, I will execute the following SQL query:

SELECT SUM(sales_amount) AS total_sales 
FROM sales_table
WHERE sale_date >= DATE_SUB(CURDATE(), INTERVAL 30 DAY);

The query sums the sales_amount column from the sales_table where the sale_date is within the last 30 days. This will give us the total sales for the last 30 days.
