from crewai import Agent, Task, Crew, Process, LLM
from crewai.project import CrewBase, agent, crew

from startup_reasoning.tools.startup_research_tool import (
    StartupResearchTool
)
from startup_reasoning.tools.market_tool import (
    MarketResearchTool
)
from startup_reasoning.tools.competitor_tool import (
    CompetitorResearchTool
)


@CrewBase
class StartupReasoningCrew:
    """Startup Reasoning Crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    def local_llm(self):
        return LLM(
            model="ollama/qwen3:1.7b",
            base_url="http://localhost:11434",
            temperature=0.3
        )

    # ---------------------------
    # TOOLS
    # ---------------------------

    def startup_research_tool(self):
        return StartupResearchTool()

    def market_tool(self):
        return MarketResearchTool()

    def competitor_tool(self):
        return CompetitorResearchTool()

    # ---------------------------
    # AGENTS
    # ---------------------------

    @agent
    def startup_intake_agent(self):
        return Agent(
            config=self.agents_config[
                "startup_intake_agent"
            ],
            llm=self.local_llm(),
            verbose=True
    )

    @agent
    def context_builder_agent(self):
        return Agent(
            config=self.agents_config[
                "context_builder_agent"
            ],
            llm=self.local_llm(),
            tools=[
                # self.startup_research_tool(),
                # self.market_tool(),
                # self.competitor_tool()
            ],
            verbose=True
        )

    @agent
    def market_analyst_agent(self):
        return Agent(
            config=self.agents_config[
                "market_analyst_agent"
            ],
            llm=self.local_llm(),
            tools=[],#[self.market_tool()]
            verbose=True
        )

    @agent
    def technical_architect_agent(self):
        return Agent(
            config=self.agents_config[
                "technical_architect_agent"
            ],
            llm=self.local_llm()
        )

    @agent
    def financial_analyst_agent(self):
        return Agent(
            config=self.agents_config[
                "financial_analyst_agent"
            ],
            llm=self.local_llm(),
        )

    @agent
    def competition_agent(self):
        return Agent(
            config=self.agents_config[
                "competition_agent"
            ],
            llm=self.local_llm(),
            tools=[],#[self.competitor_tool()]
            verbose=True
        )

    @agent
    def devils_advocate_agent(self):
        return Agent(
            config=self.agents_config[
                "devils_advocate_agent"
            ],
            llm=self.local_llm()

        )

    @agent
    def debate_moderator_agent(self):
        return Agent(
            config=self.agents_config[
                "debate_moderator_agent"
            ],
            llm=self.local_llm()
        )

    @agent
    def decision_judge_agent(self):
        return Agent(
            config=self.agents_config[
                "decision_judge_agent"
            ],
            llm=self.local_llm()
        )

    # ---------------------------
    # CREW
    # ---------------------------

    @crew
    def crew(self):

        startup_intake_task = Task(
            config=self.tasks_config[
                "startup_intake_task"
            ],
            agent=self.startup_intake_agent()
        )

        context_builder_task = Task(
            config=self.tasks_config[
                "context_builder_task"
            ],
            agent=self.context_builder_agent(),
            context=[startup_intake_task]
        )

        market_analysis_task = Task(
            config=self.tasks_config[
                "market_analysis_task"
            ],
            agent=self.market_analyst_agent(),
            context=[
                startup_intake_task,
                context_builder_task
            ]
        )

        technical_analysis_task = Task(
            config=self.tasks_config[
                "technical_analysis_task"
            ],
            agent=self.technical_architect_agent(),
            context=[
                startup_intake_task,
                context_builder_task
            ]
        )

        financial_analysis_task = Task(
            config=self.tasks_config[
                "financial_analysis_task"
            ],
            agent=self.financial_analyst_agent(),
            context=[
                startup_intake_task,
                context_builder_task
            ]
        )

        competition_analysis_task = Task(
            config=self.tasks_config[
                "competition_analysis_task"
            ],
            agent=self.competition_agent(),
            context=[
                startup_intake_task,
                context_builder_task
            ]
        )

        devils_advocate_task = Task(
            config=self.tasks_config[
                "devils_advocate_task"
            ],
            agent=self.devils_advocate_agent(),
            context=[
                market_analysis_task,
                technical_analysis_task,
                financial_analysis_task,
                competition_analysis_task
            ]
        )

        debate_task = Task(
            config=self.tasks_config[
                "debate_task"
            ],
            agent=self.debate_moderator_agent(),
            context=[
                market_analysis_task,
                technical_analysis_task,
                financial_analysis_task,
                competition_analysis_task,
                devils_advocate_task
            ]
        )

        decision_judge_task = Task(
            config=self.tasks_config[
                "decision_judge_task"
            ],
            agent=self.decision_judge_agent(),
            context=[
                startup_intake_task,
                context_builder_task,
                market_analysis_task,
                technical_analysis_task,
                financial_analysis_task,
                competition_analysis_task,
                devils_advocate_task,
                debate_task
            ],
            output_file="startup_report.md"
        )

        return Crew(
            agents=self.agents,
            tasks=[
                startup_intake_task,
                context_builder_task,
                market_analysis_task,
                technical_analysis_task,
                financial_analysis_task,
                competition_analysis_task,
                devils_advocate_task,
                debate_task,
                decision_judge_task
            ],
            process=Process.sequential,
            verbose=True,
            memory=False,
            cache=False,
            planning=False
        )