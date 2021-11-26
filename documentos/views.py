from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView
from .models import DocumentosPregao

def index(request):
    documentos=DocumentosPregao.objects.filter(usuario=request.user)
    return render(request,'documentos/index.html',{'documentos':documentos})


class cadastrar_documentos(CreateView):
    model = DocumentosPregao
    fields = ['nome', 'cpf', 'contrato_social' ]

    success_url = '/'
    template_name = 'documentos/cadastrar_documentos.html'

    #Pega automaticamente o nome do usuário que fez o cadastro
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)