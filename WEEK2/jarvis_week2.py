# JARVIS — Week 2 of 32
# New this week: Jarvis can analyze data arrays
# Week 1 was: text commands
# Week 2 is: math + data analysis brain

import numpy as np
import datetime

def jarvis_array_helper(data):
    print("\n🤖 Jarvis Array Analysis:")
    print(f"  Data: {data}")
    print(f"  Mean: {np.nanmean(data):.2f}")
    print(f"  Max: {np.nanmax(data):.2f}")
    print(f"  Min: {np.nanmin(data):.2f}")
    print(f"  Sum: {np.nansum(data):.2f}")
    print(f"  Shape: {data.shape}")
    print(f"  Dot with itself: {np.dot(data, data):.2f}")

def jarvis_respond(command):
    command = command.lower()

    if "hello" in command or "hi" in command:
        return "Hello! Jarvis online. How can I help you?"
    
    elif "your name" in command:
        return "I am Jarvis. Built by Shubh. Version 0.2"
    
    elif "time" in command:
        return f"Current time is {datetime.datetime.now().strftime('%H:%M')}"
    
    # NEW WEEK 2 COMMANDS
    elif "analyze" in command:
        data = np.array([10, 20, 30, 40, 50])
        jarvis_array_helper(data)
        return "Analysis complete!"
    
    elif "matrix" in command:
        m = np.array([[1,2,3],[4,5,6],[7,8,9]])
        return f"Sample 3x3 matrix:\n{m}"
    
    elif "dot product" in command:
        v1 = np.array([1,2,3])
        v2 = np.array([4,5,6])
        return f"Dot product of {v1} and {v2} = {np.dot(v1,v2)}"

    elif "bye" in command or "exit" in command:
        return "Goodbye. Jarvis shutting down."
    
    else:
        return f"I heard: '{command}'. Still learning this command."

print("=" * 40)
print("JARVIS V0.2 — Week 2 of 32")
print("🆕 New: Array Analysis Powers!")
print("=" * 40)
print("Commands: analyze, matrix, dot product, time")

while True:
    user_input = input("\nYou: ")
    if "bye" in user_input.lower() or "exit" in user_input.lower():
        print("Jarvis:", jarvis_respond(user_input))
        break
    print("Jarvis:", jarvis_respond(user_input))