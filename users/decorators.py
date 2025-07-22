from django.http import HttpResponseForbidden

def role_required(allowed_roles=[]):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            if request.user.is_authenticated and request.user.userprofile.role in allowed_roles:
                return view_func(request, *args, **kwargs)
            return HttpResponseForbidden("Not authorized")
        return wrapper
    return decorator
