from django.db import models


class Address(models.Model):
    street = models.CharField(max_length=50)
    street_two = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    zip_code = models.IntegerField()

    def __str__(self):
        return f'{self.street} {self.street_two}\n{self.city}, {self.state} {self.zip_code}'
    
    def line_one(self):
        line = f'{self.street}'
        if self.street_two:
            line += f', {self.street_two}'
        return line
    
    def line_two(self):
        return f'{self.city}, {self.state} {self.zip_code}'

class Cafe(models.Model):
    id = models.CharField(primary_key=True, unique=True, max_length=10)
    name = models.CharField(max_length=50)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    wifi = models.BooleanField()
    seating = models.IntegerField(default=0)
    outdoor_seating = models.IntegerField(default=0)
    bathrooms = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
    def get_amenities(self):
        amenities = {}
        if self.wifi:
            amenities['Wifi'] = self.wifi
        if self.seating:
            amenities['Seating'] = self.seating
        if self.outdoor_seating:
            amenities['Outdoor Seating'] = self.outdoor_seating
        if self.bathrooms:
            amenities['Bathrooms'] = self.bathrooms

        return amenities

class User(models.Model):
    email = models.EmailField(primary_key=True, unique=True)
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=250)

    def __str__(self):
        return self.email
