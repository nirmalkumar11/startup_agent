from crewai.tools import BaseTool
from crewai_tools import SerperDevTool


class MarketResearchTool(BaseTool):
    name: str = "Market Research Tool"
    description: str = (
        "Researches customer demand, pain points, market timing, "
        "willingness to pay, market size signals, and user behavior."
    )

    def _run(self, startup_idea: str) -> str:
        search_tool = SerperDevTool()

        queries = [
            f"{startup_idea} customer demand",
            f"{startup_idea} user pain points",
            f"{startup_idea} willingness to pay",
            f"{startup_idea} market size",
            f"{startup_idea} industry growth",
            f"{startup_idea} why now trend",
            f"{startup_idea} customer problems"
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