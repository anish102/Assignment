from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import FaceEmbed
from .serializers import FaceEmbedSerializer


# Retrieve all FaceEmbed objects, serialize them, and return as a JSON response
@api_view(['GET'])
def face_embed_list(request):
    face_embeds = FaceEmbed.objects.all()
    serializer = FaceEmbedSerializer(face_embeds, many=True)
    return Response(serializer.data)
