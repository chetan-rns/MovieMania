# Generated by Django 2.1.2 on 2018-10-30 03:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Favourites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upvotes', models.IntegerField(default=0)),
                ('downvotes', models.IntegerField(default=0)),
                ('fav', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('user_name', models.CharField(max_length=250, unique=True)),
                ('password', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_title', models.CharField(max_length=250, unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('video_user', models.ManyToManyField(through='movie_app.Favourites', to='movie_app.Users')),
            ],
        ),
        migrations.AddField(
            model_name='favourites',
            name='user_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie_app.Users'),
        ),
        migrations.AddField(
            model_name='favourites',
            name='video_title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie_app.Videos'),
        ),
        migrations.AlterUniqueTogether(
            name='favourites',
            unique_together={('video_title', 'user_name')},
        ),
    ]
