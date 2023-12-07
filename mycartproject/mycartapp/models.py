from django.db import models


class BaseProduct(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()

    class Meta:
        abstract = True


class CPU(BaseProduct):
    cores = models.PositiveIntegerField()
    clock_speed = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.cores} Cores, {self.clock_speed} GHz"


class GPU(BaseProduct):
    memory_size = models.PositiveIntegerField()
    gpu_speed = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.memory_size} GB, {self.gpu_speed} GHz"



