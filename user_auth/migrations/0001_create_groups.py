from django.db import migrations, models
from django.contrib.auth.models import Group

def create_groups(apps,schema_editor):
    Group.objects.create(name="admins")
    Group.objects.create(name="students")

def delete_groups(apps, schema_editor):
    Group.objects.filter(name__in=['admins, students']).delete()
    
class Migration(migrations.Migration):
    dependencies = []
    
    operations = [
        migrations.RunPython(create_groups, delete_groups)
    ]