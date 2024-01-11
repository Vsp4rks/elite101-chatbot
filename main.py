import time

welcome = input("Welcome to this chatbot. Would you like to talk?: ")
if welcome.lower() == "yes":
    print("Great! Let's start the conversation.")
elif welcome.lower() == "no":
    print("Okay, have a great day!")
else:
    print("I'm sorry, I didn't understand that.")

name = input("What's your name?: ")
print("Nice to meet you, " + name + "!")
age = input("What's your age?: ")
if int(age) < 13:
    print("Our responses will be kid-friendly!")
else:
    print("Our responses will be more mature.")

question = input(f"What question would you like to ask, {name}?: ")
if question == "What time is it?":
    print("The time is " + time.strftime("%H:%M:%S"))
elif question == "What's the weather like?":
    print("The weather is sunny and warm.")
elif question == "What's the most popular video game?":
    print("Looking at awards alone, Elden Ring is the most popular as it's won 320 Game of The Year Awards.")
leave_chat = input("Would you like to leave the chat? (yes/no): ")
if leave_chat.lower() == "yes":
    print("Goodbye! Have a great day!")
    quit()
else:
    print("Great! Let's keep chatting.")

question = input(f"What question would you like to ask, {name}?: ")
if question == "What time is it?":
    print("The time is " + time.strftime("%H:%M:%S"))
elif question == "What's the weather like?":
    print("The weather is sunny and warm.")
elif question == "What's the most popular video game?":
    print("Looking at awards alone, Elden Ring is the most popular as it's won 320 Game of The Year Awards.")