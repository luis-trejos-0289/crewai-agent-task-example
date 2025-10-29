import os
from crewai import Agent, Task, Crew
from dotenv import load_dotenv

load_dotenv()


os.environ["OPENAI_API_KEY"] = os.getenv('OPEN_AI_API_KEY')  # or load from .env

searcher = Agent(
    role="Research Agent",
    goal="Find recent PostgreSQL security vulnerabilities",
    backstory="Expert in cybersecurity news and CVE analysis"
)

summarizer = Agent(
    role="Summary Agent",
    goal="Summarize vulnerabilities in simple terms for developers",
    backstory="Experienced technical writer with a focus on cybersecurity"
)

writer = Agent(
    role="Writer Agent",
    goal="Create a Markdown report with findings",
    backstory="Skilled in documentation and report generation"
)

search_task = Task(
    description="Search for recent PostgreSQL CVEs",
    agent=searcher,
    expected_output="List of vulnerabilities with short descriptions"
)

summary_task = Task(
    description="Summarize findings clearly",
    agent=summarizer,
    expected_output="Concise summaries of each vulnerability"
)

write_task = Task(
    description="Save summaries to markdown file",
    agent=writer,
    expected_output="Markdown file with all summaries"
)

crew = Crew(
    agents=[searcher, summarizer, writer],
    tasks=[search_task, summary_task, write_task],
    verbose=True
)

result = crew.kickoff()
print(result)
