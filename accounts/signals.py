from .models import User, UserProfile
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def post_save_create_profile_receiver(sender, instance, created, **kwargs):
    print(created)
    if created:
        UserProfile.objects.create(user=instance)
        print('user profile is created successfully')
    else:
        try:
            profile = UserProfile.objects.get(user=instance)
            profile.save()
        except:
            # Create the user profile if not exists
            UserProfile.objects.create(user=instance)
            print('User profile was not exists, but I created one')
        print('user is updated')

@receiver(pre_save, sender=User)
def pre_save_profile_receiver(sender, instance, **kwargs):
    print(instance.username, 'This user is being saved successfully')

# post_save.connect(post_save_create_profile_receiver, sender=User)