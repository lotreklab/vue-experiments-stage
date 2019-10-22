# Generated by Django 2.2.6 on 2019-10-21 08:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('messagestext', '0002_messagetext_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messagetext',
            name='cover',
            field=models.ImageField(default='', upload_to='images/'),
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('body', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('messagetext', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='messagestext.MessageText')),
                ('voters', models.ManyToManyField(related_name='votes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
