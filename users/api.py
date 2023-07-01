from ninja import Schema
from common.api import *
from oauth2_provider.decorators import protected_resource
from ninja.security import django_auth


class UserSchema(Schema):
    url: str
    external_acct: str
    display_name: str
    avatar: str


@api.get(
    "/me",
    response={200: UserSchema, 401: Result},
    summary="Get current user's basic info",
)
def me(request):
    return 200, {
        "url": settings.SITE_INFO["site_url"] + request.user.url,
        "external_acct": request.user.mastodon_acct,
        "display_name": request.user.display_name,
        "avatar": request.user.mastodon_account.get("avatar"),
    }
