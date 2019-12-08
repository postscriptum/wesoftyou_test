from my_app.models import Gadget
from my_app.serializers import GadgetSerializer
from rest_framework import generics


class GadgetList(generics.ListAPIView):
    queryset = Gadget.objects.all()
    serializer_class = GadgetSerializer
