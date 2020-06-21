from django.db import models

#Empezamos a trabajar sobre la base de datos

class Task(models.Model):
    Title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    CreatedDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Title

'''
Posterior a crear uno o mas modelos, corremos un makemigrations y despues
un migrate para cargarlo todo a la app
'''