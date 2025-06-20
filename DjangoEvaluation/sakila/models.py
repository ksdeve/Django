from django.db import models

class Country(models.Model):
    country_id = models.AutoField(primary_key=True)
    country = models.CharField(max_length=50, unique=True)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'country'
        ordering = ['country']
        managed = False


    def __str__(self):
        return self.country

class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=50, unique=True)
    country = models.ForeignKey('Country', on_delete=models.CASCADE)
    capital = models.IntegerField()  # 0 ou 1, directement mapping TINYINT
    last_update = models.DateTimeField(auto_now=True)
    picture = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'city'
        ordering = ['city']
        managed = False

    def is_capital(self):
        return self.capital == 1


