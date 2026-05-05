user_input = input("Say something: ").lower().strip()

rules = {
    "hi": "Hello!",
    "how are you": "I am fine!",
    "bye": "Goodbye!"
}

for key in rules:
    if key in user_input:
        print(rules[key])
        break
else:
    print("I don't understand")