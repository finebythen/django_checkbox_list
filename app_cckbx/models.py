from django.db import models


class GapminderObjects(models.Model):
    id_gapminder = models.CharField(max_length=100, null=False, blank=False)
    country = models.CharField(max_length=100, null=False, blank=False)
    continent = models.CharField(max_length=100, null=False, blank=False)
    year = models.CharField(max_length=10, null=False, blank=False)
    user_created = models.CharField(max_length=50, null=False, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['country', 'continent']

    def __str__(self):
        return f"{self.id_gapminder}: {self.country} in {self.continent}"
