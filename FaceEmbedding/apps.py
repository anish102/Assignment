from django.apps import AppConfig


# Configuration class for the FaceEmbedding Django app, setting the default primary key field type and app name
class FaceembeddingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'FaceEmbedding'
