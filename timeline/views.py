import logging
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.translation import gettext_lazy as _
from django.http import HttpResponseBadRequest, HttpResponseServerError
from django.core.exceptions import ObjectDoesNotExist, PermissionDenied
from django.db import IntegrityError, transaction
from django.db.models import Count
from django.utils import timezone
from django.core.paginator import Paginator
from mastodon import mastodon_request_included
from mastodon.models import MastodonApplication
from mastodon.api import post_toot, TootVisibilityEnum
from common.utils import PageLinksGenerator
from .models import *
from django.conf import settings
import re
from users.models import User
from django.http import HttpResponseRedirect
from django.db.models import Q
import time


logger = logging.getLogger(__name__)
mastodon_logger = logging.getLogger("django.mastodon")
PAGE_SIZE = 20

@login_required
def timeline(request):
    if request.method != 'GET':
        return
    return render(
        request,
        'timeline.html',
        {
        }
    )


def data(request):
    if request.method != 'GET':
        return
    q = Q(owner_id__in=request.user.following, visibility__lt=2) | Q(owner_id=request.user.id)
    last = request.GET.get('last')
    if last:
        q = q & Q(created_time__lt=last)
    activities = Activity.objects.filter(q).order_by('-created_time')[:PAGE_SIZE]
    return render(
        request,
        'timeline_data.html',
        {
            'activities': activities,
        }
    )
