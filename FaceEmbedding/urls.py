# urls.py
from django.urls import path

from .views import face_embed_list

# URL pattern for the FaceEmbed API endpoint, mapped to the face_embed_list view
urlpatterns = [
    path('api/face_embed/', face_embed_list, name='face_embed_list'),
]
