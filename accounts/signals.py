# account -- signals

from django.dispatch import receiver
from .models import UserProfile

# third party auth --django all-auth
from allauth.account.signals import user_signed_up


@receiver(user_signed_up)
def create_user_profile(request, *args, **kwargs):
    user = kwargs['user']
    user_profile = UserProfile(user_created=user)
    user_profile.save()
    print(user_profile)
    return user_profile


def create_event_purchase(*args, **kwargs):
    # return something event services to the user
    pass


