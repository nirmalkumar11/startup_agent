from crewai.tools import BaseTool
from crewai_tools import SerperDevTool


class CompetitorResearchTool(BaseTool):
    name: str = "Competitor Research Tool"
    description: str = (
        "Finds startup competitors, pricing, market saturation, "
        "competitive positioning, and moat opportunities."
    )

    def _run(self, startup_idea: str) -> str:
        search_tool = SerperDevTool()

        queries = [
            f"top competitors of {startup_idea}",
            f"{startup_idea} alternatives",
            f"{startup_idea} pricing competitors",
            f"{startup_idea} startup market leaders",
            f"{startup_idea} competitive landscape"
        ]

        results = []

        for query in queries:
            try:
                response = search_tool.run(query)

                results.append(
                    f"\nSEARCH QUERY: {query}\n"
                    f"RESULT:\n{response}\n"
                )

            except Exception as e:
                results.append(
                    f"\nQUERY FAILED: {query}\n"
                    f"ERROR: {str(e)}\n"
                )

        return "\n".join(results)