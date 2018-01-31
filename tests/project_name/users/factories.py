import factory
import factory.django
from django.utils import timezone
from faker import Factory as FakerFactory

from yom.apps.users.models import User


faker = FakerFactory.create()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    email = factory.LazyAttribute(lambda x: faker.email())
    first_name = 'Test'
    last_name = 'User'
    last_login = factory.LazyAttribute(lambda x: timezone.now())
    password = factory.PostGenerationMethodCall('set_password', 'password')
    is_active = True


class AdminUserFactory(UserFactory):

    is_admin = True


class SuperUserFactory(AdminUserFactory):

    is_superuser = True
