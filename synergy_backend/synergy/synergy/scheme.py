import graphene
import employzapp.schema
class Query(employzapp.schema.Query, graphene.ObjectType):
    pass
class Mutation(employzapp.schema.Mutation, graphene.ObjectType):
    pass
schema = graphene.Schema(query=Query, mutation=Mutation)