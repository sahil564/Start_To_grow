# serializers.py
from rest_framework import serializers
from .models import FAQ,QBook

class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ['question', 'answer']


class QBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = QBook
        fields = ['id', 'user', 'user_question']