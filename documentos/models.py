from django.db import models

# Create your models here.
# Create your models here.
class DocumentosPregao(models.Model):
    nome=models.CharField(max_length=200,blank=True)
    cpf=models.CharField(max_length=18,blank=True)
    contrato_social = models.FileField(null=True, blank=True, upload_to='files')
    procuracao_IPP = models.FileField(blank=True, upload_to='files')
    termo_de_credenciamento = models.FileField(blank=True, upload_to='files')
    declaracao_de_PARH = models.FileField(blank=True, upload_to='files')
    declaracao_de_MEPP = models.FileField(blank=True, upload_to='files')



    class Meta:
        verbose_name_plural = 'Documentos Pregão'