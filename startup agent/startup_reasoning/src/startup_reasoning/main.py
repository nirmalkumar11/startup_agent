from dotenv import load_dotenv
from startup_reasoning.crew import StartupReasoningCrew


def get_user_input():
    print("\n=== Startup Reasoning System ===\n")

    idea = input("Startup Idea: ")
    target_users = input("Target Users: ")
    budget = input("Budget: ")
    timeline = input("Timeline: ")
    team_size = input("Team Size: ")
    country = input("Country: ")
    business_goal = input("Business Goal: ")

    return {
        "startup_idea": f"""
        Idea: {idea}
        Target Users: {target_users}
        Budget: {budget}
        Timeline: {timeline}
        Team Size: {team_size}
        Country: {country}
        Business Goal: {business_goal}
        """
    }


def run():
    load_dotenv()

    inputs = get_user_input()

    crew = StartupReasoningCrew().crew()

    result = crew.kickoff(inputs=inputs)

    print("\n")
    print("=" * 60)
    print("FINAL STARTUP REPORT")
    print("=" * 60)
    print(result)
    print("=" * 60)

    print("\nMarkdown report saved as: startup_report.md")


if __name__ == "__main__":
    run()