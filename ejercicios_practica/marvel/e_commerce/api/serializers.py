
# Primero importamos los modelos que queremos serializar:
from e_commerce.models import *

# Luego importamos todos los serializadores de django rest framework.
from rest_framework import serializers


class ComicSerializer(serializers.ModelSerializer):
    # new_field = serializers.SerializerMethodField()

    # def get_new_field(self, obj):
    #     return {'message': 'Acá puedo devolver más información.'}

    class Meta:
        model = Comic
        fields = '__all__'
        # fields = ('marvel_id', 'title', 'new_field')
        read_only_fields = ('id',)


# TODO: Realizar el serializador para el modelo de User y WishList


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model= User
        fields= ('id', 'username','email')


class WishListSerializer(serializers.ModelSerializer):

    class Meta:
        model= WishList
        fields=('__all__')

    def perform_authentication(self, request):
        """
        Perform authentication on the incoming request.

        Note that if you override this and simply 'pass', then authentication
        will instead be performed lazily, the first time either
        `request.user` or `request.auth` is accessed.
        """
        request.user
