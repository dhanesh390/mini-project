from rest_framework.serializers import ModelSerializer

from .models import Shop


class ShopDetailsSerializer(ModelSerializer):
    """ This class is implemented to serialize the shop details data"""

    class Meta:
        model = Shop
        fields = '__all__'

