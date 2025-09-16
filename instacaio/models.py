from django.db import models

# Create your models here.
class Post(models.Model):
    autor = models.CharField(max_length=40)
    imagem = models.ImageField(upload_to='posts')
    conteudo = models.TextField()
    data_postagem = models.DateTimeField(auto_now_add = True)
