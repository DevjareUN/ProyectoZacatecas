from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Set up initial user groups and assign users to groups'

    def handle(self, *args, **kwargs):
        # Create groups
        admin_group, created = Group.objects.get_or_create(name='admin')
        acnid_group, created = Group.objects.get_or_create(name='acnid')
        ml_group, created = Group.objects.get_or_create(name='medicina_legal')

        # User model
        User = get_user_model()

        # Create and assign users to groups
        users = [
            {'username': 'admin', 'password': 'adminpass', 'groups': [admin_group]},
            {'username': 'UsrAcnid', 'password': 'acnidpass', 'groups': [acnid_group]},
            {'username': 'UsrMl', 'password': 'mlpass', 'groups': [ml_group]},
            {'username': 'devjare', 'password': 'admin', 'groups': []},
        ]

        for user_data in users:
            user, created = User.objects.get_or_create(username=user_data['username'])
            if created:
                user.set_password(user_data['password'])
                if user_data['username'] == 'devjare':
                    user.is_staff = user_data.get('is_staff', False)
                    user.is_superuser = user_data.get('is_superuser', False)

                user.save()
                self.stdout.write(self.style.SUCCESS(f'Created user {user_data["username"]}'))

            for group in user_data['groups']:
                user.groups.add(group) # type: ignore
                self.stdout.write(self.style.SUCCESS(f'Assigned user {user_data["username"]} to group {group.name}'))

        self.stdout.write(self.style.SUCCESS('Successfully set up groups and assigned users.'))

