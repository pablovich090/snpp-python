from django.contrib import admin

# Register your models here.   REGISTRANDO EL MODELO EN ADMIN XD
from django.contrib import admin 
from .models import Post

admin.site.register(Post)
