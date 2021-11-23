from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView
from .models import DocumentosPregao

def index(request):
    documentos=DocumentosPregao.objects.all()
    return render(request,'documentos/index.html',{'documentos':documentos})


class cadastrar_documentos(CreateView):
    model = DocumentosPregao
    fields = '__all__'
    success_url = '/'
    template_name = 'documentos/cadastrar_documentos.html'