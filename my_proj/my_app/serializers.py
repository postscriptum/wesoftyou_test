from rest_framework import serializers
from my_app.models import Gadget


class GadgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gadget
        fields = ['code', 'category', 'link', 'price', 'cashback',
                  'full_desc', 'tech', 'photo_links']
