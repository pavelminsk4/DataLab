from django.utils.deprecation import MiddlewareMixin

class DisableCSRF(MiddlewareMixin):

    def process_request(self, request):
        #Preprocess the request.
        
        if ("Authorization" in request.headers) or (request.get_full_path().startswith('/api/auth/')):
            setattr(request, '_dont_enforce_csrf_checks', True)
        else:
            pass  # check CSRF token validation
