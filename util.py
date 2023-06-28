from config import get_API
import openai

#API_KEY = 'replace with your API-KEY'

openai.api_key = get_API()

#Function that generates the reply from the ChatGPT
def chatGPTResponse(conversation):
    try:
        response = openai.ChatCompletion.create(
            model = 'gpt-3.5-turbo', 
            messages = conversation
        )
    
    except openai.error.APIConnectionError:
        return None
    
    
    conversation.append(
        {
            'role': response.choices[0].message.role, 
            'content' : response.choices[0].message.content
        }
    )
    return conversation

#Initializing the AI
def initializeConversation():
    global conversation
    conversation = []
    conversation.append(
        {
            'role':'system',
            'content' : 'How may I help you'
        }
    )
    conversation = chatGPTResponse(conversation)

#Function that return the prompt
def  getResponse(prompt):
    global conversation
    conversation.append({'role':'user','content' : prompt})
    conversation = chatGPTResponse(conversation)

    return conversation[-1]['content'].strip()

if __name__ == "__main__":
    choice = 1
    initializeConversation();
    while (choice != 0):
        prompt = input("Enter your prompt: ")
        response = getResponse(prompt)
        print(response)
        choice = int(input())
