import graphene
from graphene_django import DjangoObjectType
from graphene_django import DjangoListField
from .models import Quizzes,Category,Answer,Question

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id","name")

class QuizzesType(DjangoObjectType):
    class Meta:
        model = Quizzes
        fields = ("id","title","category","quiz")

class QuestionType(DjangoObjectType):
    class Meta:
        model = Question
        fields = ("title","quiz")

class AnswerType(DjangoObjectType):
    class Meta:
        model = Answer
        fields = ("question","answer_text")

class Query(graphene.ObjectType):

    # all_quizzes = DjangoListField(QuizzesType) #no resolve required for DjangoListField
    all_quizzes = graphene.List(QuizzesType)
    all_questions = graphene.List(QuestionType)
    specific_quiz = graphene.Field(QuizzesType,id = graphene.Int())
    specific_question = graphene.Field(QuestionType,id = graphene.Int())
    specific_answer = graphene.List(AnswerType,id = graphene.Int())

    def resolve_specific_answer(self, info,id):
        return Answer.objects.filter (question_id = id)

    def resolve_specific_question(self, info,id ):
        return Question.objects.get(pk = id)

    def resolve_specific_quiz(self, info,id):
        return Quizzes.objects.get(pk = id)

    def resolve_all_quizzes(root, info):
        return Quizzes.objects.all()
    #     return Quizzes.objects.filter(id=1) # to resolve based on parameters

    def resolve_all_questions(root,info):
        return Question.objects.all()
    # def resolve_quiz(root, info):
    #     return f"This is the first question"

schema = graphene.Schema(query = Query)    