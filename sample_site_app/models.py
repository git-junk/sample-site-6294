from django.db import models

class Word(models.Model):
  __tablename__ = "word"
  name = models.CharField(max_length=100)
  
  def __str__(self):
      return self.name
