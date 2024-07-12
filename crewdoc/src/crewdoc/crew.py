from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# Uncomment the following line to use an example of a custom tool
from crewdoc.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
from crewai_tools import SerperDevTool

@CrewBase
class CrewdocCrew():
	"""Crewdoc crew"""
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def researcher(self) -> Agent:
		return Agent(
			config=self.agents_config['researcher'], # Debe apuntar al decorador correspondiente del archivo agents.yaml
			tools=[MyCustomTool()], # Example of custom tool, loaded on the beginning of file
			verbose=True,
			allow_delegation=True
		)

	@agent
	def reporting_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['reporting_analyst'],	# Debe apuntar al decorador correspondiente del archivo agents.yaml
   			tools=[MyCustomTool()], # Example of custom tool, loaded on the beginning of file
			verbose=True,
			allow_delegation=True
		)

	@task
	def clinical_analysis_task(self) -> Task:
		return Task(
			config=self.tasks_config['clinical_analysis_task'], # Debe apuntar al decorador correspondiente del archivo tasks.yaml
			agent=self.researcher() # Debe apuntar al agente que debe realizar la tarea
		)

	@task
	def clinical_history(self) -> Task:
		return Task(
			config=self.tasks_config['clinical_history'],
			agent=self.reporting_analyst(),
			output_file='report.md'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the Crewdr crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=2,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)