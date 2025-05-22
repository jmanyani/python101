from functools import wraps

def login_required(func):
    """A decorator to ensure the user is logged in before accessing a protected function."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        if kwargs.get('logged_in'):
            print(" Access granted. User is authenticated.")
            return func(*args, **kwargs)
        else:
            print(" Access denied. Please log in to continue.")
    return wrapper

@login_required
def show_user_profile(user_id, **kwargs):
    print(f" Displaying profile for user ID: {user_id}")

# Simulate calls

# Case 1: User is logged in
show_user_profile(101, logged_in=True)

print()  # Just for clean output separation

# Case 2: User is not logged in
show_user_profile(102, logged_in=False)
