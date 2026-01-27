# ===============================
# Imports
# ===============================

from typing import List, Literal, Annotated
from pydantic import BaseModel
from pyjokes import get_joke
from langgraph.graph.state import CompiledStateGraph

from langgraph.graph import StateGraph, END
from operator import add

# ===============================
# State Definitions
# ===============================

class Joke(BaseModel):
    """Represents a single joke."""
    text: str
    category: str


class JokeState(BaseModel):
    """
    Global state shared across the LangGraph.
    """
    jokes: Annotated[List[Joke], add] = []
    jokes_choice: Literal["n", "c", "l", "r", "q"] = "n"
    category: str = "neutral"
    language: str = "en"
    quit: bool = False


# ===============================
# Node Functions
# ===============================

def show_menu(state: JokeState) -> dict:
    """
    Displays menu and captures user input.
    """
    print("\n" + "=" * 55)
    print(f"🎭 Category : {state.category.upper()}")
    print(f"🌐 Language : {state.language}")
    print(f"😂 Jokes Told : {len(state.jokes)}")
    print("=" * 55)

    choice = input(
        "[n] Next Joke  "
        "[c] Change Category  "
        "[l] Change Language  "
        "[r] Reset History  "
        "[q] Quit\n> "
    ).strip().lower()

    return {"jokes_choice": choice}


def fetch_joke(state: JokeState) -> dict:
    """
    Fetches a joke using pyjokes.
    """
    joke_text = get_joke(
        language=state.language,
        category=state.category
    )

    print(f"\n😂 {joke_text}")

    return {
        "jokes": [
            Joke(text=joke_text, category=state.category)
        ]
    }


def update_category(state: JokeState) -> dict:
    """
    Updates joke category.
    """
    categories = ["neutral", "chuck", "all"]

    print("\nSelect Category:")
    print("[0] Neutral")
    print("[1] Chuck Norris")
    print("[2] All")

    selection = int(input("> ").strip())
    return {"category": categories[selection]}


def update_language(state: JokeState) -> dict:
    """
    Updates joke language.
    """
    languages = ["en", "de", "es", "fr"]

    print("\nSelect Language:")
    print("[0] English")
    print("[1] German")
    print("[2] Spanish")
    print("[3] French")

    selection = int(input("> ").strip())
    return {"language": languages[selection]}


def reset_jokes(state: JokeState) -> dict:
    """
    Clears joke history.
    """
    print("\n🔁 Joke history reset.")
    return {"jokes": []}


def exit_bot(state: JokeState) -> dict:
    """
    Gracefully exits the application.
    """
    print("\n🚪 Exiting Joke Bot...")
    return {"quit": True}


# ===============================
# Router Function
# ===============================

def route_choice(state: JokeState) -> str:
    """
    Determines next node based on user choice.
    """
    return {
        "n": "fetch_joke",
        "c": "update_category",
        "l": "update_language",
        "r": "reset_jokes",
        "q": "exit_bot",
    }.get(state.jokes_choice, "exit_bot")


# ===============================
# Graph Construction
# ===============================

def build_joke_graph():
    """
    Builds and compiles the LangGraph.
    """
    workflow = StateGraph(JokeState)

    # Register nodes
    workflow.add_node("show_menu", show_menu)
    workflow.add_node("fetch_joke", fetch_joke)
    workflow.add_node("update_category", update_category)
    workflow.add_node("update_language", update_language)
    workflow.add_node("reset_jokes", reset_jokes)
    workflow.add_node("exit_bot", exit_bot)

    # Entry point
    workflow.set_entry_point("show_menu")

    # Conditional routing
    workflow.add_conditional_edges(
        "show_menu",
        route_choice,
        {
            "fetch_joke": "fetch_joke",
            "update_category": "update_category",
            "update_language": "update_language",
            "reset_jokes": "reset_jokes",
            "exit_bot": "exit_bot",
        }
    )

    # Normal edges
    workflow.add_edge("fetch_joke", "show_menu")
    workflow.add_edge("update_category", "show_menu")
    workflow.add_edge("update_language", "show_menu")
    workflow.add_edge("reset_jokes", "show_menu")
    workflow.add_edge("exit_bot", END)

    return workflow.compile()


# ===============================
# Main Entry Point
# ===============================

def main():
    print("\n🎉 WELCOME TO LANGGRAPH JOKE BOT 🎉")
    print("Agentic Workflow Without LLMs\n")

    graph = build_joke_graph()
    graph.invoke(JokeState(), config={"recursion_limit": 100})

    print("\n📊 SESSION SUMMARY")
    print("Thank you for using the Joke Bot!")


if __name__ == "__main__":
    main()
