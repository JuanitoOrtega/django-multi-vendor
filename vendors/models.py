from django.db import models
from accounts.models import User, UserProfile
from accounts.utils import send_notification


class Vendor(models.Model):
    user = models.OneToOneField(User, related_name='user', on_delete=models.CASCADE, verbose_name='Usuario')
    user_profile = models.OneToOneField(UserProfile, related_name='userprofile', on_delete=models.CASCADE, verbose_name='Perfil de usuario')
    vendor_name = models.CharField(max_length=50, verbose_name='Nombre del vendedor')
    vendor_license = models.ImageField(upload_to='vendor/license', blank=True, null=True, verbose_name='Licencia')
    is_approved = models.BooleanField(default=False, verbose_name='Aprobado')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Modificado')

    class Meta:
        verbose_name = 'Vendedor'
        verbose_name_plural = 'Vendedores'

    def save(self, *args, **kwargs):
        if self.pk is not None:
            # Update
            orig = Vendor.objects.get(pk=self.pk)
            if orig.is_approved != self.is_approved:
                mail_template = 'accounts/emails/admin_approval_email.html'
                context = {
                    'user': self.user,
                    'is_approved': self.is_approved,
                }
                if self.is_approved == True:
                    # Send notification email
                    mail_subject = 'Felicidades! Tu restaurante ha sido aprobado.'
                    send_notification(mail_subject, mail_template, context)
                else:
                    # Send notification email
                    mail_subject = '¡Lo sentimos! Por el momento no es elegible para publicar su menú de comida en nuestro sitio web.'
                    send_notification(mail_subject, mail_template, context)
        return super(Vendor, self).save(*args, **kwargs)

    def __str__(self):
        return self.vendor_name