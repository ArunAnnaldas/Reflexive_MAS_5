from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from langchain.callbacks import get_openai_callback


llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo",
	openai_api_key="")

# Step 1: Planner Agent
def planner_agent(task):
    messages = [
        SystemMessage(content="You are a senior software architect. Break down coding tasks into implementation steps."),
        HumanMessage(content=f"Task: {task}")
    ]
    return llm(messages).content

# Step 2: Coder Agent
def coder_agent(instruction, feedback=None):
    messages = [
        SystemMessage(content="You are an expert Python developer. Write clean, correct code based on the instructions."),
        HumanMessage(content=instruction)
    ]
    if feedback:
        messages.append(HumanMessage(content=f"Update your code based on this reviewer feedback:\n{feedback}"))
    return llm(messages).content

# Step 3: Critic Agent
def critic_agent(code):
    messages = [
        SystemMessage(content="You are a senior code reviewer. Critically review the code and suggest improvements. If it's good, respond with 'APPROVED'."),
        HumanMessage(content=f"Code:\n{code}")
    ]
    return llm(messages).content

# 🔁 Reflexive Loop Orchestrator
def run_multi_agent_loop(user_request, max_retries=3):
    print("📌 User Request:", user_request)

    print("\n🔧 Step 1: Planner Agent...")
    plan = planner_agent(user_request)
    print(plan)

    print("\n💻 Step 2: Coder Agent (Initial Attempt)...")
    code = coder_agent(plan)
    print(code)

    for attempt in range(1, max_retries + 1):
        print(f"\n🧐 Critic Agent (Attempt {attempt})...")
        review = critic_agent(code)
        print(review)

        if "APPROVED" in review.upper():
            print("\n✅ Code approved by Critic. Final version:")
            print(code)
            return

        print("\n🔁 Feedback received. Coder will revise...")
        code = coder_agent(plan, feedback=review)

    print("\n⚠️ Max retries reached. Last version of the code:")
    print(code)

# 🔍 Try it
if __name__ == "__main__":
    user_prompt = "Write a function to check if a number is prime"
    with get_openai_callback() as cb:
        run_multi_agent_loop(user_prompt)
        print("\n📊 Token Usage Summary:")
        print(cb)