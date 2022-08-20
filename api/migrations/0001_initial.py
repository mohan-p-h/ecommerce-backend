from django.db import migrations
from api.user.models import CustomUser

class Migration(migrations.Migration):
    def seed_data(apps, schema_editor):
        user = CustomUser(name="mohan", email="mohan@gmail.com", is_staff=True, is_superuser=True, phone="7676551300", gender="Male")
        user.set_password("123456")
        user.save()

    dependencies = [

    ]

    operations = [
        migrations.RunPython(seed_data),
    ]
