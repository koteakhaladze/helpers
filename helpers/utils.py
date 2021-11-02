import os
from django.utils import timezone


def get_object_or_false(model, **kwargs):
    try:
        return model.objects.get(**kwargs)
    except model.DoesNotExist:
        return False


def upload_path(instance, filename):
    now = timezone.now()
    return os.path.join(
        instance.__class__.__name__.lower(),
        "%s" % now.strftime('%Y'),
        filename
    )


def user_upload_path(instance, filename):
    now = timezone.now()
    return os.path.join(
        instance.__class__.__name__.lower(),
        "%s" % now.strftime('%Y'),
        instance.username,
        filename
    )

