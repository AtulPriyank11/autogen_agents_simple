from autogen import ConversableAgent
from agents import UserProxyAgent, AssistantAgent
from functions import fetch_data, generate_code_snippet, answer_question

def main():
    # Initialize Autogen agents
    user_agent = UserProxyAgent(name="UserProxy")
    assistant_agent = AssistantAgent(name="Assistant")

    # User asks to fetch data
    user_message = "Can you fetch data for 'latest news'?"
    print(user_agent.send_message(user_message))
    response = assistant_agent.receive_message(fetch_data("latest news"))
    print(response)

    # User asks for a code snippet
    user_message = "Can you generate a code snippet for data processing?"
    print(user_agent.send_message(user_message))
    response = assistant_agent.receive_message(generate_code_snippet("data processing"))
    print(response)

    # User asks a question using RAG
    user_message = "What is the capital of France?"
    print(user_agent.send_message(user_message))
    response = assistant_agent.receive_message(answer_question("What is the capital of France?"))
    print(response)

if __name__ == "__main__":
    main()
