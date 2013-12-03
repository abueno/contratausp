from contratausp import settings
def context(request):
    from django.contrib.sites.models import Site
    debug = settings.DEBUG

    return {
        'debug': debug,
        'request': request,
        'site': Site.objects.get_current(),
    }