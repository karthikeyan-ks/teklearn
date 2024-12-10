from django.contrib.auth.models import User

def create_superuser():
    username = 'admin'
    email = 'admin@example.com'
    password = 'adminpassword'
    
    if not User.objects.filter(username=username).exists():
        user = User.objects.create_superuser(username=username, email=email, password=password)
        print(f"Superuser created: {user}")
    else:
        print("Superuser already exists.")

if __name__ == '__main__':
    create_superuser()
