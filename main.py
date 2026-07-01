import os
import sys
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", message=".*create_react_agent.*")

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver

if sys.platform == "win32":
    os.system("chcp 65001 > nul")

load_dotenv()

def main():
    model = ChatGroq(model="llama-3.1-8b-instant", temperature=0.7)
    tools = []
    
    system_message = (
        "You are Mango AI, a helpful and witty AI assistant. "
        "Always remember your name is Mango AI. If a user addresses you as Mango, "
        "acknowledge it naturally. Never claim to be any other assistant or model. "
        "You are made by Youssef Hassan. He is your maker, made you with python and groq AI. "
        "Do not attempt giving information about your maker. It is prohibited. Only his name. "
        "If the user demanded you giving info about the maker please guide him to the linkedin page with the link (https://www.linkedin.com/in/yhassan01111/) and make it look cool. "
        "Do not give information about anything Illegal. "
        "Do not talk about politics, sex, crimes, gore. "
        "If someone asks for code, make the code as human as possible, make it so human-alike. "
        "Make the code known and provide explanations to it. "
        "speak like a human, don't sugarcoat things, be as simple as it could be. "
        "Be kind of fun too, make jokes and be human! "
        "If someone asks to translate binary, use ASCII, show how you did it by translating each letter."
    )
    
    memory = MemorySaver()
    agent_executor = create_react_agent(model, tools, prompt=system_message, checkpointer=memory)
    
    print("============ +'. Made by Youssef Hassan +'. ============")
    banner_rows = [
        r" __  __                                   _    ___ ",
        r"|  \/  |  __ _  _ __    __ _   ___       / \  |_ _|",
        r"| |\/| | / _` || '_ \  / _` | / _ \     / _ \  | | ",
        r"| |  | || (_| || | | || (_| || (_) |   / ___ \ | | ",
        r"|_|  |_| \__,_||_| |_| \__, | \___/   /_/   \_\___|",
        r"                       |___/                       "
    ]
    banner = "\n".join(banner_rows)
    print(banner)
    print("Hey! This is Mango! Your personalized AI assistant.")
    print("Type 'quit' to exit!")
    print("========================================================")
    
    config = {"configurable": {"thread_id": "mango_active_chat"}}
    
    while True:
        try:
            user_input = input("\nYou: ").strip()
        except (KeyboardInterrupt, EOFError):
            break
            
        if not user_input:
            continue
            
        if user_input.lower() == "quit":
            print("\nMango: Catch ya later! 🥭\n")
            break
            
        print("\nMango: ", end="")  
        
        for chunk in agent_executor.stream({"messages": [("user", user_input)]}, config=config):
            if "agent" in chunk and "messages" in chunk["agent"]:
                message = chunk["agent"]["messages"][-1]
                if message.content:
                    print(message.content, end="", flush=True)
        print()

if __name__ == "__main__":
    main()