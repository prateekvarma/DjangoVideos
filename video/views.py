from django.shortcuts import render
from django.core.paginator import Paginator
from . models import Video


def index(request):
    video_list = Video.objects.all()
    videos = Paginator(video_list, 3) # 3 items on each page
    grouped_videos = []
    for page in videos.page_range: # page_rage gives total number of pages by paginator
        # videos.page takes a param, and returns that page.
        # object_list gives the list of all objects in that page
        page_objects = videos.page(page).object_list
        grouped_videos.append(page_objects)
    return render(request, 'video/index.html', {'videos': videos})


def video(request, video_id):
    queried_video = Video.objects.get(pk=video_id)
    return render(request, 'video/video.html', {'queried_video': queried_video})
