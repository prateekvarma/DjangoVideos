from django.shortcuts import render
from . models import Video


def index(request):
    return render(request, 'video/index.html')


def video(request):
    queried_video = Video.objects.get(pk=1)
    return render(request, 'video/video.html', {'queried_video': queried_video})
