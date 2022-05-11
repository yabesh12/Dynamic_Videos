from core.models import Content, Video


def dynamic_content(request):
    content_objs = Content.objects.last()
    # print(content_objs)
    return dict(dyna=content_objs)


def dynamic_video(request):
    videos_objs = Video.objects.all()
    # print(videos_objs)
    return dict(videos_objs=videos_objs)

