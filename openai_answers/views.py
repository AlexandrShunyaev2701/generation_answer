from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from openai_answers.answer_openai_generation import AnswerTextGenerator
from openai_answers.models import Answer
from openai_answers.serializers import AnswerGenerationTextSerializer


class AnswerView(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerGenerationTextSerializer

    def get_queryset(self):
        queryset = self.queryset.all()
        return queryset

    @action(methods=["POST"], detail=False)
    def generation_answer(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user_question = serializer.validated_data.get("user_question")
        objects = Answer.objects.all()

        combined_content = ""
        for obj in objects:
            combined_content += f"Url: {obj.url}, Title: {obj.title}, Description: {obj.description}\n"

        generator = AnswerTextGenerator(combined_content, user_question)
        response = generator.generate_text()

        return Response({"answer": response})

