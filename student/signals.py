from django.db.models.signals import post_save
from django.dispatch import receiver
from core.models import User
from .models import Student

@receiver(post_save, sender=User)
def create_student_profile(sender, instance, created, **kwargs):
    if created:
        Student.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_student_profile(sender, instance, **kwargs):
    if hasattr(instance, 'student'):
        instance.student.save()