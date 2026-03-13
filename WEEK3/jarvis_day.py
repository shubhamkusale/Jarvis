import pandas as pd
import numpy as np
import datetime

def jarvis_explore_data(filepath):
    df = pd.read_csv(filepath)
    
    print("=" * 40)
    print("📊 JARVIS DATA ANALYSIS")
    print("=" * 40)
    
    # Shape
    print(f"Dataset: {df.shape[0]} rows, {df.shape[1]} columns")
    
    # All column names
    print(f"Columns: {list(df.columns)}")
    
    # Missing values
    print("\n📊 Missing Values:")
    print(df.isnull().sum())
    
    # Fill ALL numeric columns automatically
    for col in df.select_dtypes(include=[np.number]).columns:
        df[col] = df[col].fillna(df[col].mean())
    
    print("\n✅ Missing values filled!")
    
    # Statistics for entire dataset
    print("\n📈 Statistics:")
    print(df.describe())

def jarvis_respond(command):
    command = command.lower()

    if "hello" in command:
        return "Hello! Jarvis V0.3 online!"
    elif "your name" in command:
        return "I am Jarvis. Built by Shubh. Version 0.3"
    elif "time" in command:
        return f"Time: {datetime.datetime.now().strftime('%H:%M')}"
    elif "analyze" in command:
        filepath = input("Jarvis: Enter CSV filepath: ")
        jarvis_explore_data(filepath)
        return "Analysis complete!"
    elif "bye" in command:
        return "Goodbye! Jarvis shutting down."
    else:
        return f"I heard: '{command}'. Still learning!"

print("=" * 40)
print("JARVIS V0.3 — Week 3 of 32")
print("🆕 Can explore ANY CSV dataset!")
print("=" * 40)
print("Commands: hello, your name, time, analyze, bye")

while True:
    user_input = input("\nYou: ")
    if "bye" in user_input.lower():
        print("Jarvis: Goodbye!")
        break
    print("Jarvis:", jarvis_respond(user_input))