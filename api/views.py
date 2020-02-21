from .models import SensorGasModel
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from .serializers import SensorGasSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, RetrieveAPIView
from rest_framework.decorators import action
# Create your views here.

class PostPage(ListCreateAPIView):
    queryset = SensorGasModel.objects.all()
    serializer_class = SensorGasSerializer

class UpdatePostPage(RetrieveUpdateAPIView):
    queryset = SensorGasModel.objects.all()
    serializer_class = SensorGasSerializer

class AjaxGasView(RetrieveAPIView):
    model = SensorGasModel
    serializer_class = SensorGasSerializer
    lookup_field= "no_tiang"

    def get_object(self, queryset=None):
        no_tiang= self.kwargs.get('no_tiang')
        obj = SensorGasModel.objects.filter(no_tiang=no_tiang).order_by('-time_stamp')[0]
        return obj
