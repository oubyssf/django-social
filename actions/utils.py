from .models import Action
from django.utils import timezone
from django.contrib.contenttypes.models import ContentType


def create_action(user, verb, target=None):
    now = timezone.now()
    lastminute = now - timezone.timedelta(seconds=60)
    similar_actions = Action.objects.filter(
        user=user,
        verb=verb,
        created__gt=lastminute
    )

    if target:
        target_ct = ContentType.objects.get_for_model(target)
        similar_actions = similar_actions.filter(
            target_ct=target_ct,
            target_id=target.id
        )

    if not similar_actions:
        Action.objects.create(
            user=user,
            verb=verb,
            target=target
        )
        return True

    return False