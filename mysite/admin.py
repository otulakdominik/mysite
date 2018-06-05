from django.conf import settings
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import login, authenticate

# the same filter that I called in the template
from .templatetags import logic


def login_as_user(request, user_id):

    request_hash = request.GET.get("hash", "")
    if request_hash != logic.hash("user", user_id):
        raise Exception("invalid hash value")

    user = User.objects.get(id=user_id)

    user = authenticate(
        username=user.username, password=settings.ADMIN_HASH_SECRET
    )
    login(request, user)

    return HttpResponseRedirect(reverse("home"))
