from django.db import models

# Create your models here.

class Crop(models.Model):
    name = models.CharField(max_length=100)
    Region = models.TextField(default="No description")
    categories = models.TextField(default="No description")
    planting_date = models.DateField(default="No description")
    expected_yield = models.FloatField(default="No description")
    description = models.TextField(default="No description")
    optimal_conditions = models.TextField(default="no value")
    planting_guidelines = models.TextField(default="no value")
    pest_management = models.TextField(default="no value")
    nutritional_requirements = models.TextField(default="no value")
    harvesting_info = models.TextField(default="no value")
    sustainability_practices = models.TextField(default="no value")


    def __str__(self):
        return self.name

class YieldRecord(models.Model):
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    actual_yield = models.FloatField()
    harvest_date = models.DateField()

    def __str__(self):
        return f"{self.crop.name} - {self.harvest_date}"

class WasteReduction(models.Model):
    strategy = models.CharField(max_length=200)
    effectiveness = models.CharField(max_length=100)

    def __str__(self):
        return self.strategy