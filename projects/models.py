from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import Q


class User(AbstractUser):
  password = models.CharField(max_length=255)

  def __str__(self):
    return f"{self.first_name} {self.last_name}"


class Project(models.Model):
  name = models.CharField(max_length=255, unique=True)
  owner = models.ForeignKey(User, on_delete=models.CASCADE)
  employees = models.ManyToManyField(User, related_name="projects")
  estimated_budget = models.DecimalField(max_digits=10, decimal_places=2)

  def __str__(self):
    return f"{self.name}"

  class Meta:
    indexes = [
      models.Index(fields=["name"], name="name_idx")
    ]


class Feedback(models.Model):
  project = models.ForeignKey(Project, on_delete=models.CASCADE)
  employee = models.ForeignKey(User, on_delete=models.CASCADE)
  rating = models.IntegerField()
  comment = models.TextField(null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"{self.employee} - {self.project.name} - {self.rating}"

  class Meta:
    constraints = [
      models.CheckConstraint(
        condition=Q(rating__gte=1),
        name="rating_gte_1"
      ),
      models.CheckConstraint(
        condition=Q(rating__lte=5),
        name="rating_lte_5"
      )
    ]
