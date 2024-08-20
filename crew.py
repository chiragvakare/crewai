from crewai import Crew, Process
from agents import blog_researcher, blog_writer
from tasks import research_task, write_task

# Forming the tech-focused crew with enhanced configurations
crew = Crew(
  agents=[blog_researcher, blog_writer],
  tasks=[research_task, write_task],
  process=Process.sequential,  # Optional: Sequential task execution is default
  memory=True,
  cache=True,
  max_rpm=100,
  share_crew=True,
  max_iterations=1000,  # Global iteration limit
  time_limit=3600  # Global time limit
)

# Start the task execution process with enhanced feedback
result = crew.kickoff(inputs={'topic': 'AI VS ML VS DL vs Data Science'})
print(result)
