from crewai_tools import BaseTool

import os
import chromadb
from dotenv import load_dotenv, find_dotenv

from langchain.agents import tool
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_community.vectorstores import Chroma
from langchain_openai import ChatOpenAI, OpenAIEmbeddings


class RAG_OpenAI(BaseTool):
    name: str = "Respuesta a la pregunta en español usando OpenAI"
    description: str = "Esta herramienta se utiliza para obtener la repuesta de una llm a la pregunta formulada. La pregunta debe ser respondida en español"
    
    def _run(self, pregunta: str) -> str:
      # Carga las variables de entorno desde un archivo .env
      load_dotenv(find_dotenv(), override=True)

      # Obtiene la API key de OpenAI desde las variables de entorno
      api_key_openAI = os.environ.get("OPENAI_API_KEY")
      
      llm = os.environ.get("OPENAI_MODEL_NAME")
       
      model = ChatOpenAI(model=llm, api_key=api_key_openAI)
        
      prompt = ChatPromptTemplate.from_template(template="Pregunta: {question}\n")
      output_parser = StrOutputParser()
       
      chain = prompt | model | output_parser
      respuesta = chain.invoke({"question": pregunta})
      
      return respuesta 


"""
if __name__ == "__main__":
    tool = RAG_OpenAI()
    resultado = tool.run("¿Cuál es la capital de España?")
    print(resultado)

"""


"""
 
    
import os
import chromadb
from dotenv import load_dotenv, find_dotenv

from langchain.agents import tool
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_community.vectorstores import Chroma
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

 
class MyTools:
    @tool
    def GPT_answer(query: str) -> str:
      """ """_summary_: Esta herramienta se utiliza pare obtener la repuesta de openAI en español
         Args:
              query (str): la pregunta debe ser respondida por openAI en español
      """ """
    
      # Carga las variables de entorno desde un archivo .env
      load_dotenv(find_dotenv(), override=True)

      # Obtiene la API key de OpenAI desde las variables de entorno
      api_key_openAI = os.environ.get("OPENAI_API_KEY")
      
      llm = os.environ.get("OPENAI_MODEL_NAME")
       
      model = ChatOpenAI(model=llm, api_key=api_key_openAI)
        
      prompt = ChatPromptTemplate.from_template(template="Question: {question}\n")
      output_parser = StrOutputParser()
       
      chain = prompt | model | output_parser
      respuesta = chain.invoke({"question": query})
      
      return respuesta 
      
      
       
    @tool
    def RAG_answer(query: str) -> str:
      """ """_summary_: Esta herramienta se utiliza pare obtener la repuesta RAG de openAI sobre documentos PDF en español
        Args:
              query (str): la pregunta debe ser respondida por openAI en español
      """ """

      embedding_function = OpenAIEmbeddings()

      # Carga las variables de entorno desde un archivo .env
      load_dotenv(find_dotenv(), override=True)

      # Obtiene la API key de OpenAI desde las variables de entorno
      api_key_openAI = os.environ.get("OPENAI_API_KEY")
      
      llm = os.environ.get("OPENAI_MODEL_NAME")
       
      model = ChatOpenAI(model=llm, api_key=api_key_openAI)
      
      
      client = chromadb.HttpClient(host='localhost', port="8010")


      # Recuperar vectores de DB
      db4 = Chroma(
          client=client,
          collection_name="SEED_5",
          embedding_function=embedding_function,
      )

      retriever = db4.as_retriever(
              search_type="similarity", search_kwargs={"k": 10})
    
      
      template = """ """Answer the question based only on the following context:
      {context}
      Question: {question}
      """ """
      prompt = ChatPromptTemplate.from_template(template)
      output_parser = StrOutputParser()
      setup_and_retrieval = RunnableParallel(
          {"context": retriever, "question": RunnablePassthrough()})
      chain = setup_and_retrieval | prompt | model | output_parser
      respuesta=chain.invoke(query)
      
      return respuesta
   
    
    def tools(self):
       return [MyTools.GPT_answer, MyTools.RAG_answer] 


"""   