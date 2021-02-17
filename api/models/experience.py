from django.db import models
from django.contrib.auth import get_user_model

class Experience(models.Model):
  what = models.CharField(max_length=100)
  where = models.CharField(max_length=100)
  notes = models.CharField(max_length=250)
  owner = models.ForeignKey(
    get_user_model(),
    on_delete=models.CASCADE
  )

  def __str__(self):
    return f"{self.what} at {self.where}"

  def as_dict(self):
    """Returns dictionary version of Experience models"""
    return {
      'id': self.id,
      'what': self.what,
      'where': self.where,
      'notes': self.notes
    }