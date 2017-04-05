from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.models import User
from rest_framework import generics, renderers, permissions, viewsets
from rest_framework.decorators import api_view, detail_route
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import Exchange
from .serializers import ExchangeSerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly


class ExchangeViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides 'list', 'create', 'retrieve',
    'update' and 'destroy' actions.

    """
    queryset = Exchange.objects.all()
    serializer_class = ExchangeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides 'list' and 'detail' actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


# class WeekendViewSet(viewsets.ReadOnlyModelViewSet):
#     """
#     This viewset automatically provides 'list' and detail' actions.
#     """
#     queryset = Weekend.objects.all()
#     serializer_class = WeekendSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'holidays': reverse('holiday-list', request=request, format=format),
        'weekends': reverse('weekend-list', request=request, format=format),
        'users': reverse('user-list', request=request, format=format),
        'exchanges': reverse('exchange-list', request=request, format=format)
        })


class IndexView(generic.ListView):
    template_name = 'stxclock/index.html'
    context_object_name = 'stxclock_index'

    def get_queryset(self):
        return Exchange.objects.all()

def index(request):
    exchange_list = Exchange.objects.all()
    return render(request, 'stxclock/index.html', {'exchange_list': exchange_list})
# def index(request):
#     exchange_list = Exchange.objects.all()
#     context = {
#             'exchange_list': exchange_list,
#             }
#     return render(request, 'stxclock/index.html', context)


# def detail(request, exchange_id):
#     exchange = get_object_or_404(Exchange, pk=exchange_id)
#     return render(request, 'stxclock/detail.html', {'exchange': exchange})
