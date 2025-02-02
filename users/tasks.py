from datetime import timedelta

from django.conf import settings
from django.utils import timezone
from loguru import logger
from tqdm import tqdm

from .models import User


def refresh_mastodon_data_task(user_id, token=None):
    user = User.objects.get(pk=user_id)
    if not user.mastodon_username:
        logger.info(f"{user} mastodon data refresh skipped")
        return
    if token:
        user.mastodon_token = token
    if user.refresh_mastodon_data():
        logger.info(f"{user} mastodon data refreshed")
    else:
        logger.warning(f"{user} mastodon data refresh failed")
