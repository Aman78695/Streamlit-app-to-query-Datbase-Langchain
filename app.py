
#from langchain.sql_database import SQLDatabase
from langchain.llms import OpenAI
from langchain.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
db = SQLDatabase.from_uri("mysql+pymysql://root:aman@localhost/aman")
llm = OpenAI(openai_api_key='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',temperature=0)

db_chain = SQLDatabaseChain(llm=llm, database=db, verbose=True)
db_chain.run("what is the district id of cbo named shahnaz")