from .models import SensorGasModel
from .serializers import SensorGasSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
# Create your views here.

class PostPage(ListCreateAPIView):
    queryset = SensorGasModel.objects.all()
    serializer_class = SensorGasSerializer

class UpdatePostPage(RetrieveUpdateAPIView):
    queryset = SensorGasModel.objects.all()
    serializer_class = SensorGasSerializer