from django.shortcuts import redirect
from functools import wraps

def role_required(allowed_roles=[]):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect('login')
            if hasattr(request.user, 'userprofile'):
                if request.user.userprofile.role not in allowed_roles:
                    return redirect('dashboard')  # or a "permission denied" page
            else:
                return redirect('login')
            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator
