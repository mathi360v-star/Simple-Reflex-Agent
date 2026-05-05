# agent/agent.py

from agent.rules import RULES
from agent.processor import clean_input

class SimpleReflexAgent:

    def respond(self, user_input: str) -> str:
        cleaned = clean_input(user_input)

        for key, response in RULES:
            if key in cleaned:
                return response

        return "I don't understand"