from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from core.models import Video, HtmlContent


# def home(request):
#     return render(request, 'base.html')


def home(request):
    video_objects = Video.objects.all()
    print(video_objects)
    # urls = []
    # for vid in video_objects: 
    #     video_url = settings.MEDIA_URL + vid.name
    # getting full url -
    # # video_url = settings.MEDIA_URL + file_name
    #     print(video_url)
    #     urls.append(video_url)
    context = {"video_objects": video_objects}
    html = render_to_string("main.html", context)
    print(html)
    HtmlContent.objects.create(content=html)

    # lst = [vi.vid for vi in video_objects]

    # str_lst = ','.join(lst)
    # with open('video_data.txt', 'w') as file:
    #     file.write(str_lst)
    return JsonResponse({"html": html})
    # return render(request, 'main.html', context)
