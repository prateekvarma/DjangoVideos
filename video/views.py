from django.shortcuts import render
from . models import Video


def index(request):
    return render(request, 'video/index.html')


def video(request, video_id):
    queried_video = Video.objects.get(pk=video_id)
    return render(request, 'video/video.html', {'queried_video': queried_video})
