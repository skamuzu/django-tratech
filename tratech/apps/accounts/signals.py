from django.dispatch import receiver
from django.db.models.signals import post_save
from allauth.socialaccount.models import SocialAccount
from .models import User

@receiver(post_save, sender=SocialAccount)
def update_user_profile_from_social(sender, instance, created, **kwargs):
    user = instance.user
    profile_image = instance.extra_data.get("picture")
    name = instance.extra_data.get("name")  
    
    if name:
        user.image = profile_image 
        user.name = name
        user.save(update_fields=["name","image"])
