from django.db import models
from application.storage_backends import *
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings 

user_model = settings.AUTH_USER_MODEL

# Create your models here.

class tclInput(models.Model):
    meshFile = models.FileField(storage=PublicMediaStorage())
    kernelType = models.CharField(max_length=255)
    packetCount = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(0)])
    user = models.ForeignKey(user_model,
                             default = 0,
                             null = True,
                             on_delete=models.CASCADE
                             )

class tclScript(models.Model):
    script = models.FileField(storage=PublicMediaStorage())
    user = models.ForeignKey(user_model,
                             default = 0,
                             null = True,
                             on_delete=models.CASCADE
                             )

class fullmonteOutput(models.Model):
    outputVtk = models.FileField(storage=PublicMediaStorage())
    outputFluence = models.FileField(storage=PublicMediaStorage())
    user = models.ForeignKey(user_model,
                             default = 0,
                             null = True,
                             on_delete=models.CASCADE
                             )

class preset(models.Model):
    presetMesh = models.FileField(storage=PublicMediaStorage())
    layerDesc = models.TextField(blank=True, null=True)

class Material(models.Model):
    material_name = models.CharField(max_length=50)
    scattering_coeff = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0)])
    absorption_coeff = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0)])
    refractive_index = models.FloatField(null=True, blank=True, validators=[MinValueValidator(1)])
    anisotropy = models.FloatField(null=True, blank=True, validators=[MinValueValidator(-1), MaxValueValidator(1)])

    objects = models.Manager()

    def __str__(self):
        return self.material_name
