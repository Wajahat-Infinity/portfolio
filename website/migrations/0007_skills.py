# Generated by Django 4.2.5 on 2024-01-01 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_sociallinks_tiktok_sociallinks_youtube_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=50)),
                ('icon', models.ImageField(blank=True, null=True, upload_to='images/SkillsIcon')),
            ],
        ),
    ]