import ollama

chat_messages = []

def create_message(content, role):
    return {'role': role, 'content': content}

def chat():
    response = ollama.chat(model='llama3', stream=True, messages=chat_messages)
    assistant_message = ''
    for chunk in response:
        assistant_message += chunk['message']['content']
        print(chunk['message']['content'], end='', flush=True)
    chat_messages.append(create_message(assistant_message, 'assistant'))

def ask(urlText):
    
    with open(urlText, "r", encoding="utf-8") as archivo:
        textMeet = archivo.read()
    
    message = f"""
    
    According to this meeting, fill out the fields in the json format and do not respond anything else.
    
    {textMeet}
    
    {{
    "current meet": {{
        "Meet Title": "Invent a title",
        "integrantes": [""],
        "meeting summary": "Summary this meet in one sentence"
    }},
    "task": [
        {{"Person in charge of the task": "", "Task Title":"", "task description": ""}},
        {{"Person in charge of the task": "", "Task Title":"", "task description": ""}},
        {{"Person in charge of the task": "", "Task Title":"", "task description": ""}},
        {{"Person in charge of the task": "", "Task Title":"", "task description": ""}}
    ]
    }},
    "future meet": [
        {{"Meeting name": "", "Date":"", "Meet description": ""}},
        {{"Meeting name": "", "Date":"", "Meet description": ""}},
        {{"Meeting name": "", "Date":"", "Meet description": ""}},
        {{"Meeting name": "", "Date":"", "Meet description": ""}}
    ]
    }}
    """
    chat_messages.append(create_message(message, 'user'))
    #print(f'\n\n--{message}--\n\n')
    chat()
