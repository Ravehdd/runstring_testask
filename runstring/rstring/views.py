from django.http import FileResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from moviepy.editor import TextClip, CompositeVideoClip, ColorClip
import tempfile
from .models import *
import os
import math
# os.environ['IMAGE_MAGICK_BINARY'] = r'C:\Program Files\ImageMagick-7.1.1-Q16\magick.exe'


class RunStringAPIVew(APIView):
    def post(self, request):
        text = request.data["text"]
        serializer = TextSerializer(data=request.data)
        if serializer.is_valid():
            background = ColorClip((800, 600), col=(255, 255, 255), duration=3)
            txt_clip = TextClip(text, fontsize=500, color='black').set_duration(3)

            speed = len(text) / (math.sqrt(len(text)) * 1.3)

            def position(t):
                return int(800 - speed * 600 * t), 'center'

            txt_clip = txt_clip.set_pos(lambda t: position(t))
            final_clip = CompositeVideoClip([background, txt_clip])

            temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.mp4')
            final_clip.write_videofile(temp_file.name, fps=24)

            video_obj = GeneratedVideo(video_file=temp_file.name, text_request=text)
            video_obj.save()
            data = GeneratedVideo.objects.all().values()
            print(data)
            return FileResponse(open(temp_file.name, 'rb'), content_type='video/mp4')
        else:
            return Response({"Status": "400", "Response": "Bad request"})


class RunStringDBAPIVew(APIView):
    def get(self, request):
        v = GeneratedVideo.objects.all().values()
        return Response({"requests": v})