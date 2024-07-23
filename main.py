#!/usr/bin/env python
from crewdoc.crew import CrewdocCrew
from dotenv import load_dotenv
load_dotenv('/Users/joaquinchamorromohedas/Desktop/crewdc/crewdoc/.env')  # Esto carga las variables de entorno desde '.env'

def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    inputs = {
        'topic': input("What is the topic of the analysis?"), #topic es el valor de la variable que se le pasará a la tarea clinical_analysis_task en el archivo tasks.yaml
        'specialty': "internista" #input("What is the name of the profesional?"),
        }
    CrewdocCrew().crew().kickoff(inputs=inputs) 

if __name__ == "__main__":
    run()