# JARVIS — Week 1 of 32
# Today: just text input and response
# Week 32: voice, memory, multi-agent AI

def jarvis_respond(command):
    command = command.lower()
    
    if "hello" in command or "hi" in command:
        return "Hello! Jarvis online. How can I help you?"
    elif "your name" in command:
        return "I am Jarvis. Built by Shubh. Version 0.1"
    elif "time" in command:
        import datetime
        return f"Current time is {datetime.datetime.now().strftime('%H:%M')}"
    elif "bye" in command or "exit" in command:
        return "Goodbye. Jarvis shutting down."
    
    else:
        return f"I heard you say: '{command}'. I am still learning to respond to this."

print("=" * 40)
print("JARVIS V0.1 — Week 1 of 32")
print("=" * 40)

while True:
    user_input = input("\nYou: ")
    if "bye" in user_input.lower() or "exit" in user_input.lower():
        print("Jarvis:", jarvis_respond(user_input))
        break
    print("Jarvis:", jarvis_respond(user_input))
