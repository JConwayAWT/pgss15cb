from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from datetime import datetime
from django.core.exceptions import ValidationError
from django.dispatch import receiver
from django.db.models.signals import post_save, post_init
from django.utils.translation import ugettext as _
from userena.models import UserenaBaseProfile

class DemoObject(models.Model):
  object_name = models.CharField(max_length = 255, null = True, blank = True, verbose_name = "Object Name")
  object_description = models.CharField(max_length = 255, null = True, blank = True, verbose_name = "Object Description")
  object_number = models.CharField(max_length = 255, null = True, blank = True, verbose_name = "Object Number")

  def __unicode__(self):
    return "{}".format(self.object_name or self.object_description or "N/A")

class UserProfile(UserenaBaseProfile):
  user = models.OneToOneField(User)

  organization = models.CharField(max_length = 255, null = True, blank = True, verbose_name = "Organization Name")
  scientific_field = models.CharField(max_length = 255, null = True, blank = True, verbose_name = "Field")

  def __unicode__(self):
      return "Profile information for {}".format(self.user.email)

  class Meta:
      verbose_name = "Profile"
      verbose_name_plural = "Profiles"

  def create_user_profile(sender, instance, created, **kwargs):
      if created:
          UserProfile.objects.create(user=instance)


class AlgorithmRun(models.Model):
  user_profile = models.OneToOneField(UserProfile, null = True)
  name = models.CharField(max_length = 255, null = True, blank = True, verbose_name = "Name")
  description = models.CharField(max_length = 2048, null = True, blank = True, verbose_name = "Description")
  input_file = models.FileField(upload_to = "documents/%Y/%m/%d")