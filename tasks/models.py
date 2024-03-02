from django.db import models

class Status(models.TextChoices):
    TODO = "TODO", "A fazer"
    IN_PROGRESS = "IN_PROGRESS", "Em progresso"
    DONE = "DONE", "Concluída"


class Task(models.Model):

    title = models.CharField(
        verbose_name="Título",
        max_length=50
    )

    status = models.CharField(
        verbose_name="Situação",
        max_length=50,
        choices=Status.choices,
        default="TODO",
    )

    description = models.TextField(
        verbose_name="Descrição",
        max_length=250,
        null=True,
        blank=True
    )
