# Import HttpResponseForbidden to return a 403 Forbidden response if user is not allowed
from django.http import HttpResponseForbidden

# Define a custom decorator named 'role_required'
# It accepts a list of allowed roles (e.g., ['counsellor', 'principal'])
def role_required(allowed_roles=[]):
    
    # This is the actual decorator that wraps around a view function
    def decorator(view_func):
        
        # This is the inner wrapper function that runs when the view is called
        def wrapper(request, *args, **kwargs):
            # Check if the user is logged in AND their role is in the allowed list
            if request.user.is_authenticated and request.user.userprofile.role in allowed_roles:
                # If the role is allowed, proceed to the actual view
                return view_func(request, *args, **kwargs)
            
            # If the user's role is not allowed, return a 403 Forbidden response
            return HttpResponseForbidden("Not authorized")
        
        # Return the wrapper function to replace the original view
        return wrapper
    
    # Return the decorator function
    return decorator
