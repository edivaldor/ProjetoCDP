from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Create your models here.
class DocumentosPregao(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True)
    nome = models.CharField(max_length=100,blank=True)
    cpf = models.CharField(max_length=14,blank=True)
    contrato_social = models.FileField(blank=True, upload_to='documentos')
    procuracao_IPP = models.FileField(blank=True, upload_to='documentos')
    termo_de_credenciamento = models.FileField(blank=True, upload_to='documentos')
    declaracao_de_PARH = models.FileField(blank=True, upload_to='documentos')
    declaracao_de_MEPP = models.FileField(blank=True, upload_to='documentos')
    prova_de_condicao_MEPP = models.FileField(blank=True, upload_to='documentos')
    proposta = models.FileField(blank=True, upload_to='documentos')




    class Meta:
        verbose_name_plural = 'Documentos Pregão'

    def __str__(self):
        return self.nome