# CrewAI Agent Task Example

This project demonstrates how to use the CrewAI SDK to orchestrate multiple agents and tasks for automated research, summarization, and report generation. The example focuses on finding recent PostgreSQL security vulnerabilities and producing a Markdown report.

## How It Works

- **Agents**: Three agents are defined using CrewAI:
  - **Research Agent**: Searches for recent PostgreSQL CVEs (security vulnerabilities).
  - **Summary Agent**: Summarizes the findings in simple terms for developers.
  - **Writer Agent**: Generates a Markdown report with the summarized findings.
- **Tasks**: Each agent is assigned a specific task, executed in sequence:
  1. Search for vulnerabilities
  2. Summarize findings
  3. Write the report
- **Crew**: The agents and tasks are grouped into a Crew, which coordinates execution.
- **Integrations**:
  - Uses the CrewAI SDK for agent/task orchestration.
  - Integrates with OpenAI (for LLMs).
  - Loads API keys from a `.env` file using `python-dotenv`.

## Setup

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
2. **Configure API keys**:
   - Create a `.env` file in the project root with your OpenAI API key:
     ```env
     OPEN_AI_API_KEY=your_openai_api_key
     ```

## Usage

Run the main script:
```bash
python agent.py
```

The script will:
- Search for recent PostgreSQL vulnerabilities
- Summarize them
- Output a Markdown report

## References
- [CrewAI SDK Documentation](https://docs.crewai.com/)
- [OpenAI API](https://platform.openai.com/docs/api-reference)

---

*This example is for educational purposes and can be adapted for other research/reporting workflows using CrewAI.*
