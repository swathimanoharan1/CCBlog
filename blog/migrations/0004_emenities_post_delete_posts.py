# Generated by Django 4.2.14 on 2024-07-28 11:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0003_alter_posts_created_on'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emenities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateTimeField()),
                ('content', models.TextField()),
                ('metades', models.CharField(default='new post', max_length=300)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish'), (2, 'Delete')], default=0)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.DeleteModel(
            name='posts',
        ),
    ]
