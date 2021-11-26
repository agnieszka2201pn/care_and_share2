from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password_1, password_2, **extra_fields):
        if not email:
            raise ValueError('Please enter a valid email')
        if not password_1 != password_2:
            raise ValueError('Passwords do not match')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password_1)
        user.save()
        return user


    def create_superuser(self, email, password_1, password_2, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('For Superuser set is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('For Superuser set is_superuser=True.')
        if password_1 != password_2:
            raise ValueError('Passwords do not match')
        return self.create_user(email, password_1, **extra_fields)

