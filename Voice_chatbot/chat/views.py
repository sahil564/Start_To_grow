from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import QBookSerializer
from .models import FAQ
from nltk.chat.util import Chat, reflections



def load_data_from_db():
    faqs = FAQ.objects.all()
    return faqs

def create_chatbot_pairs():
    faqs = load_data_from_db()
    pairs = []
    for faq in faqs:
        pair = [faq.question, [faq.answer]]
        pairs.append(pair)
    return pairs



@api_view(['GET', 'POST'])
def conversation(request):
    if request.method == 'GET':
        return Response("Called Get Request")

    elif request.method == 'POST':
        serializer = QBookSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            pair=create_chatbot_pairs()
            bot = Chat(pair, reflections)
            bot_response = bot.respond(serializer.data.get("user_question"))
            return Response(bot_response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

