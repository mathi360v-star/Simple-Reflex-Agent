# main.py

from agent.agent import SimpleReflexAgent

agent = SimpleReflexAgent()

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Agent: Goodbye!")
        break

    response = agent.respond(user_input)
    print("Agent:", response)