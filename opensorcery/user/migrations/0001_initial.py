from django.db import migrations
from django.conf import settings

"""
TODO: Remove this migration once you have setup github SSO, it won't be needed
"""


def create_data(apps, schema_editor):
    User = apps.get_model(settings.AUTH_USER_MODEL)
    user = User(
        pk=1,
        username="auth0user",
        is_active=True,
        email="admin@techiediaries.com"
    )
    user.save()


class Migration(migrations.Migration):
    dependencies = [
    ]
    operations = [
        migrations.RunPython(create_data),
    ]
