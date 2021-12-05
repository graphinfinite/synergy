import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from employzapp.models import Occupation
# Create a GraphQL type for the model
class OccupationType(DjangoObjectType):
    class Meta:
        model = Occupation


# Create a Query type
class Query(ObjectType):
    occupation = graphene.Field(OccupationType, id=graphene.Int())
    occupations = graphene.List(OccupationType)
    def resolve_occupation(self, info, id):
        print("hello")
        if id is not None:
            return Occupation.objects.get(pk=id)
        return None
    def resolve_occupations(self, info, **kwargs):
        print("hello")
        return Occupation.objects.all()


# Create Input Object Types
class OccupationInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()
    company_name = graphene.String()
    position_name = graphene.String()
    hire_date = graphene.DateTime()
    fire_date = graphene.DateTime()
    salary = graphene.Int()
    fraction = graphene.Int()
    base = graphene.Int()
    advance = graphene.Int()
    by_hours = graphene.Boolean()

# Создание профиля
class CreateOccupation(graphene.Mutation):
    class Arguments:
        input = OccupationInput(required=True)
    ok = graphene.Boolean()
    occupation = graphene.Field(OccupationType)
    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        occupation_instance = Occupation(name=input.name, 
                                        company_name = input.company_name,
                                        position_name = input.position_name,
                                        hire_date = input.hire_date,
                                        fire_date =input.fire_date ,
                                        salary = input.salary,
                                        fraction = input.fraction,
                                        base =input.base ,
                                        advance = input.advance,
                                        by_hours =input.by_hours)
        occupation_instance.save()
        return CreateOccupation(ok=ok, occupation=occupation_instance)

# Обновление профиля
class UpdateOccupation(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = OccupationInput(required=True)
    ok = graphene.Boolean()
    occupation = graphene.Field(OccupationType)
    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        occupation_instance = Occupation.objects.get(pk=id)
        if occupation_instance:
            ok = True
            occupation_instance.name = input.name
            occupation_instance.company_name = input.company_name,
            occupation_instance.position_name = input.position_name,
            occupation_instance.hire_date = input.hire_date,
            occupation_instance.fire_date =input.fire_date ,
            occupation_instance.salary = input.salary,
            occupation_instance.fraction = input.fraction,
            occupation_instance.base =input.base ,
            occupation_instance.advance = input.advance,
            occupation_instance.by_hours =input.by_hours
            occupation_instance.save()
            return UpdateOccupation(ok=ok, occupation=occupation_instance)
        return UpdateOccupation(ok=ok, occupation=None)


class Mutation(graphene.ObjectType):
    create_occupation = CreateOccupation.Field()
    update_occupation = UpdateOccupation.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)