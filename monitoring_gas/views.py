from django.shortcuts import render
from api.models import SensorGasModel
from api.serializers import SensorGasSerializer

def homeView(request):
    try:
        tiang1 = SensorGasModel.objects.filter(no_tiang="Tiang A").order_by('-time_stamp')[0]
    except:
        tiang1 = None
    try:
        tiang2 = SensorGasModel.objects.filter(no_tiang="Tiang B").order_by('-time_stamp')[0]
    except:
        tiang2 = None
    try:
        tiang3 = SensorGasModel.objects.filter(no_tiang="Tiang C").order_by('-time_stamp')[0]
    except:
        tiang3 = None
    # print(querysets)
    context = {
        'judul': 'Home',
        # 'querysets': querysets,
        'tiang1': tiang1,
        'tiang2': tiang2,
        'tiang3': tiang3,
    }
    return render(request, 'index.html',context)

def logView(request):
    queryset = SensorGasModel.objects.all().order_by('time_stamp')
    # for instance in queryset:
    #     val = instance.sensor_value
    #     ppm =  (10000/ 4096) * val + 200
    #     instance.sensor_value = ppm
    #     instance.save()
    context = {
        'judul' : 'Log Data',
        'queryset': queryset,
    }
    return render(request, 'log.html', context)