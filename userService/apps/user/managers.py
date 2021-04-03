from django.contrib.auth.base_user import BaseUserManager


class CustomerUserManager(BaseUserManager):
    """
        Custom user manager to make email as the unique identifier instead of username
    """
    def create_user(self, email, password, **extra_fields):
        """
            Create and save user using email and password
        """
        extra_fields = extra_fields.get('extra_fields')
        if not email:
            raise ValueError('Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
            Create and save a Superuser with email and password
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        return self.create_user(email, password, extra_fields=extra_fields)
