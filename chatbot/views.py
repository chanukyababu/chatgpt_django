from django.shortcuts import render
from django.http import JsonResponse
import openai


openai_api_key = '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'
openai.api_key =openai_api_key 

def ask_openai(message):
    response = openai.Completion.create(
        model = "text-davinci-003",
        prompt = message + " Subject is maths multiple choice question with Json format",
        max_tokens = 150,
        n=1,
        stop=None,
        temperature = 0.7
    )
    print(response)
    answer = response.choices[0].text.strip()
    return answer
# Create your views here.
def chatbot(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_openai(message)
        return JsonResponse({'message':message, 'response': response})
    return render(request, 'chatbot.html')
