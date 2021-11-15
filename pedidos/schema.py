import graphene
from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from pedidos.models import Pedido



# Se hace lo mismo con el modelo Ingredient
class PedidoNode(DjangoObjectType):
    class Meta:
        model = Pedido
        # Permite un filtrado mas avanzado
        filter_fields = {
            'cliente': ['exact', 'icontains'],
            'pedido': ['exact', 'icontains'],
            'total': ['exact'],
        }
        interfaces = (relay.Node, )


class Query(graphene.ObjectType):
    pedidos = relay.Node.Field(PedidoNode)
    all_pedidos = DjangoFilterConnectionField(PedidoNode)