from django.shortcuts import render,redirect
from django.http import JsonResponse
import openai
from .models import Chat

from django.utils import timezone

openai_api_key = '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' # Replace YOUR_API_KEY with your openai apikey
openai.api_key = openai_api_key

def ask_openai(message):
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo-16k-0613",
        # prompt = message,
        # max_tokens=150,
        # n=1,
        # stop=None,
        # temperature=0.7,
        messages=[
            {"role": "system", "content": "you are a smart assistant at the Global System PC store and you must help the user with all issues related to the topic of Computers, for example, help with the selection of components for price, performance, and so on."},
            {"role": "user", "content": message},
        ]
    )
    answer = response.choices[0].message.content.strip()
    return answer

# Create your views here.

def chatbot(request):
    chats = Chat.objects.filter(user=request.user)


    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_openai(message)

        return JsonResponse({'message': message, 'response': response})
    return render(request, 'chatbot.html', {'chats': chats})


