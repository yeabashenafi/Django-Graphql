import graphene
from graphene_django import DjangoObjectType
from .models import Hero

class HeroType(DjangoObjectType):
    class Meta:
        model = Hero
        fields = ("id","name","lastname")

class Query(graphene.ObjectType):
    all_heroes = graphene.List(HeroType)

    def resolve_all_heroes(root, info):
        return Hero.objects.all()

schema = graphene.Schema(query=Query)
