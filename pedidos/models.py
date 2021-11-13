from django.db import models


class Pedido(models.Model):

    cliente = models.CharField(max_length=100)

    pedido = models.TextField()

    total = models.TextField()


    def __str__(self):

        return self.cliente


