from django.test import TestCase
from django.db import IntegrityError
from django.core.exceptions import ValidationError

from .factories import UserFactory
from .factories import AdminUserFactory
from .factories import SuperUserFactory


class UserTestCase(TestCase):
    def test_create_user(self):
        user = UserFactory()

        self.assertTrue(user.email)
        self.assertTrue(user.password)
        self.assertTrue(user.first_name)
        self.assertTrue(user.last_name)
        self.assertTrue(user.creation_date)
        self.assertTrue(user.update_date)
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_admin)
        self.assertFalse(user.is_superuser)


    def test_user_fields_validation(self):
        with self.assertRaises(ValidationError):
            UserFactory(email='notanemail')

        with self.assertRaises(ValidationError):
            UserFactory(first_name='')

        with self.assertRaises(ValidationError):
            UserFactory(last_name='')

    def test_user_password(self):
        user = UserFactory(password='mypass')

        self.assertTrue(user.check_password('mypass'))

    def test_user_is_unique(self):
        user = UserFactory()

        with self.assertRaises(IntegrityError):
            UserFactory(email=user.email)

    def test_create_admin(self):
        admin = AdminUserFactory()

        self.assertTrue(admin.is_admin)

    def test_create_superuser(self):
        superuser = SuperUserFactory()

        self.assertTrue(superuser.is_admin)
        self.assertTrue(superuser.is_superuser)
