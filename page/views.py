from django.views.generic import RedirectView


class RedirectToAdmin(RedirectView):
    url = "admin/"
