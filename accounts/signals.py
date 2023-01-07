from .models import User, UserProfile
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def post_save_create_profile_receiver(sender, instance, created, **kwargs):
    print(created)
    if created:
        UserProfile.objects.create(user=instance)
        print('Perfil de usuario creado exitosamente')
    else:
        try:
            profile = UserProfile.objects.get(user=instance)
            profile.save()
        except:
            # Create the user profile if not exists
            UserProfile.objects.create(user=instance)
            print('El perfil de usuario no existía, pero se creó uno')
        print('Usuario actualizado')

@receiver(pre_save, sender=User)
def pre_save_profile_receiver(sender, instance, **kwargs):
    print(instance.username, 'Usuario guardado con éxito')

# post_save.connect(post_save_create_profile_receiver, sender=User)