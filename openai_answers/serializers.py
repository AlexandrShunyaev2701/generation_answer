from rest_framework import serializers
from openai_answers.models import Answer


class AnswerGenerationTextSerializer(serializers.Serializer):
    user_question = serializers.CharField(write_only=True, required=True)

    class Meta:
        fields = ['user_question']