from collections.abc import Collection

from django.db import models

from src.utils.strings import _, __


class Field(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, default="")

    def __str__(self):
        return f"{_(self.name)} : {_(self.description)}"


class FieldValue(models.Model):
    portfolio = models.OneToOneField("Portfolio", on_delete=models.CASCADE, null=True, blank=True)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name=_("children"))

    field = models.ForeignKey(Field, on_delete=models.CASCADE, null=True, blank=True)
    value = models.TextField()

    def __str__(self):
        return f"{self.parent.field.name if self.parent else '/'}.{self.field.name} = {_(self.value)}"

    def clean(self) -> None:
        # TODO : validate various combinations of field and value, along with cyclic references
        ...


class Portfolio(models.Model):
    name = models.CharField(max_length=200, blank=True, default="")

    def __str__(self):
        return f"PortFolio {self.pk}"
