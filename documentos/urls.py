from django.contrib import admin
from django.urls import path, include
from .views import index,cadastrar_documentos

urlpatterns = [
      path('',index),
      path('cadastrar_documentos/',cadastrar_documentos.as_view(),name='cadastrar_documentos')
]