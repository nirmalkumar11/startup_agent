from crewai.tools import BaseTool
from crewai_tools import SerperDevTool


class StartupResearchTool(BaseTool):
    name: str = "Startup Research Tool"
    description: str = (
        "Researches startup markets, trends, customer demand, "
        "industry growth, and relevant startup insights."
    )

    def _run(self, startup_idea: str) -> str:
        search_tool = SerperDevTool()

        queries = [
            f"{startup_idea} market size",
            f"{startup_idea} startup trends 2026",
            f"{startup_idea} customer demand",
            f"{startup_idea} industry growth",
            f"{startup_idea} biggest problems users face"
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
                    f"\nQUERY FAILED: {query}\nERROR: {str(e)}"
                )

        return "\n".join(results)