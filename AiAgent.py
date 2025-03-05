import os
from langchain_community.agent_toolkits import GmailToolkit 


from langchain_community.tools.gmail.utils import (
    build_resource_service,
    get_gmail_credentials,
)
from langchain_openai import ChatOpenAI
from langchain import hub
from langchain.agents import AgentExecutor, create_openai_functions_agent

import app_gs



def main(slackMessage : str):
    llm = ChatOpenAI(api_key= os.environ["OPENAI_API_KEY"], model= "gpt-4o-mini")

    gJsonData = app_gs.main()
    
    print(gJsonData)
    gsDate= gJsonData["ocDate"]
    gsName= gJsonData["personName"]
    gsEmail= gJsonData["personEmail"]

    credentials = get_gmail_credentials(
        token_file="token.json",
        scopes=["https://mail.google.com/"],
        client_secrets_file="credential.json",
    )
    api_resource = build_resource_service(credentials=credentials)
    toolkit = GmailToolkit(api_resource=api_resource)

    instructions = """You are an AI assistant . """
    base_prompt = hub.pull("langchain-ai/openai-functions-template")
    prompt = base_prompt.partial(instructions=instructions)


    agent = create_openai_functions_agent(llm, toolkit.get_tools(), prompt)

    agent_executor = AgentExecutor(
        agent=agent,
        tools=toolkit.get_tools(),
        
        verbose=False,
    )

    to_email= gsEmail
    receiver= gsName
    subject= "error message"
    body = slackMessage
    print(to_email)
    print(receiver)
    print(subject)
    print(body)

    args = {
    "input": f"Create a mail draft. Your subject will be '{subject}' email body will be Mr. '{receiver}' --- '{body}' and email receiver '{to_email}' put in the Drafts mail folder."
}
    
    
    result= agent_executor.invoke(args)
    print(result)

if __name__ == "__main__":
    main()
