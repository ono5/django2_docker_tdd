from django.http import HttpResponseBadRequest


def ajax_required(f):
    def wrap(request, *args, **kwargs):
        """
        is_ajax() checks whether the request is being made with XMLHttpRequest,
        which means it is an AJAX request.

        This value is set in the HTTP_X_REQUESTED_WITH HTTP header, which is included
        in AJAX requests by most JavaScript libraries.

        We will create a decorator for checking the HTTP_X_REQUESTED_WITH header in out views.

        # If you try to access http://127.0.0.1:8000/images/like directly with your browser,
          you will get an HTTP 400 response.
        """
        if not request.is_ajax():
            return HttpResponseBadRequest()
        return f(request, *args, **kwargs)
    wrap.__doc__=f.__doc__
    wrap.__name__=f.__name__
    return wrap
