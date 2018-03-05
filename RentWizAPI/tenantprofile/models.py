from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


# Signal to generate authentication tokens when users are added
# -http://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication
@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


# Model for RentWiz Tenants
# - Extends Django's in-built user model
# - May be extended in future to also incorporate all non-admin users
# - Example extension: foreign key relation to 'UserType' Model
# - UserType may include Tenant/Landlord
class Tenant(models.Model):
    phone = models.CharField(max_length=11, blank=True, null=True)
    profile_picture = models.CharField(max_length=500, blank=True, null=True)
    payment_method = models.CharField(max_length=50, blank=True, null=True)
    payment_token = models.CharField(max_length=150, blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def delete(self, *args, **kwargs):
        self.user.delete()
        super(Tenant, self).delete(*args, **kwargs)

    # Declare __str__ and __unicode__ methods for use within Django Rest Framework
    # - allows clear representation in admin panel
    # - conventional practice for Django applications
    def __str__(self):
        return self.user.username + ": " + self.user.first_name + " " + self.user.last_name

    def __unicode__(self):
        return self.user.username + ": " + self.user.first_name + " " + self.user.last_name
