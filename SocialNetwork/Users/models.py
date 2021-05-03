from django.db import models

# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, gender, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            gender=gender,
            # date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password, first_name, last_name, gender):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
            first_name=first_name,
            last_name=last_name,
            gender=gender,
            # date_of_birth=date_of_birth,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    username = models.CharField(max_length=80)
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    gender = models.CharField(
        choices=[('male', 'male'), ('female', 'female')], max_length=50)
    # date_of_birth = models.DateField()
    profile_avatar = models.ImageField(
        upload_to='media/avatars', max_length=50, default="default.png")
    date_joined = models.DateTimeField(
        verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    # password                =
    REQUIRED_FIELDS = [
        'first_name', 'last_name', 'gender']
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    objects = MyAccountManager()

    def __str__(self):
        return self.email

    # For checking permissions. to keep it simple all admin have ALL permissons
    def has_perm(self, perm, obj=None):
        return self.is_admin

    # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True

    def __str__(self):
        return f"{self. email} email | {self.  username} username "

# # Create your models here.
# class UserDetails(models.Model):
#     user_id = models.ForeignKey(
#         User, related_name="details", on_delete=models.CASCADE)
#     gender = models.CharField(
#         choices=[('male', 'male'), ('female', 'female')], max_length=50)
#     date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
#     profile_avatar = models.ImageField(
#         upload_to='media/avatars', max_length=50, default="default.png")


class Friend(models.Model):
    user_id = models.ForeignKey(
        CustomUser, related_name="user", on_delete=models.CASCADE)
    friend_id = models.ForeignKey(
        CustomUser, related_name="userfriend", on_delete=models.CASCADE)


class FriendRequest(models.Model):
    Reciever = models.ForeignKey(
        CustomUser, related_name="reciever", on_delete=models.CASCADE)
    Sender = models.ForeignKey(
        CustomUser, related_name="sender", on_delete=models.CASCADE)
