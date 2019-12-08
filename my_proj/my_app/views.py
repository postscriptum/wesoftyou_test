from my_app.models import Gadget
from my_app.serializers import GadgetSerializer
from rest_framework import generics


class GadgetList(generics.ListAPIView):
    serializer_class = GadgetSerializer

    def get_queryset(self):
        queryset = Gadget.objects.all()
        # price filter
        min_price = self.request.query_params.get('min_price', None)
        if min_price is not None:
            queryset = queryset.filter(price__gte=int(min_price))
        max_price = self.request.query_params.get('max_price', None)
        if max_price is not None:
            queryset = queryset.filter(price__lte=int(max_price))
        # cashback filter
        min_cash = self.request.query_params.get('min_cash', None)
        if min_cash is not None:
            queryset = queryset.filter(cashback__gte=int(min_cash))
        max_cash = self.request.query_params.get('max_cash', None)
        if max_cash is not None:
            queryset = queryset.filter(cashback__lte=int(max_cash))
        # RAM filter
        ram = self.request.query_params.get('ram', None)
        if ram is not None:
            queryset = queryset.filter(tech__contains={'Объем оперативной памяти': '{} Гб'.format(ram)})
        # cores filter
        cores = self.request.query_params.get('cores', None)
        if cores is not None:
            queryset = queryset.filter(tech__contains={'Количество ядер процессора': '{}'.format(cores)})
        return queryset
