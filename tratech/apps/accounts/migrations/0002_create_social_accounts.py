# yourapp/migrations/000x_create_social_apps.py

from django.db import migrations
from config.settings import CLIENT_ID, CLIENT_SECRET, SITE_ID

def create_social_apps(apps, schema_editor):
    SocialApp = apps.get_model("socialaccount", "SocialApp")
    Site = apps.get_model("sites", "Site")

    site = Site.objects.get(id=SITE_ID)

    app, created = SocialApp.objects.get_or_create(
        provider="google",
        defaults={
            "name": "Google",
            "client_id": CLIENT_ID,
            "secret": CLIENT_SECRET,
        },
    )

    app.sites.add(site)


def delete_social_apps(apps, schema_editor):
    SocialApp = apps.get_model("socialaccount", "SocialApp")
    SocialApp.objects.filter(provider="google").delete()


class Migration(migrations.Migration):
    
    dependencies = [
        ("accounts", "0001_initial"),
        ("socialaccount", "0005_socialtoken_nullable_app")
    ]
     
    operations = [
        migrations.RunPython(create_social_apps, delete_social_apps),
    ]
