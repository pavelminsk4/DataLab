from django.urls import reverse
import logging
from django.utils.deprecation import MiddlewareMixin
# django2


class DisableCSRF(MiddlewareMixin):
    """Middleware for disabling CSRF in an specified app name.
    """

    def process_request(self, request):
        """Preprocess the request.
        """
        logging.error('Your message: ', request.get_full_path())

        app_name = "api"
        if request.get_full_path().startswith('/api/auth/'):
            setattr(request, '_dont_enforce_csrf_checks', True)
        else:
            pass  # check CSRF token validation
