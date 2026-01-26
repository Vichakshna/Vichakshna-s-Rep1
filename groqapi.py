from groq import Groq
import os
Client=Groq(api_key=os.getenv("GROQ_API_KEY"))

def llm_call(Prompt, systme_instruction):
    response=Client.chat.completions.create(
        model="llama-3.1-8b-instant" ,
        messages = [{"role":"system","content":system_instruction},{"role":"user","content":Prompt}],
        temperature=0.7
    )

    print(response.choices[0].message.content)

'''Top_k=40,     
    Top_p=0.8,
    max_token=1000'''

def program_exit(Prompt,system_instructions):
    n=1
    while n not in(0,"0"):
        llm_call(Prompt,system_instruction)
        print("Executed llm call")
        n=input("enter any key, if you want to exit type 0")


if __name__ == "__main__":

    Prompt=input("enter the prompt")

    system_instruction = "You are my tutor."

    program_exit(Prompt, system_instruction)

