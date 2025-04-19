from django.conf import settings

def global_constants(request):
    return {
        "NAV_LINKS": settings.NAV_LINKS
    }