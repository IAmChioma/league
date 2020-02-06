# Generated by Django 3.0.3 on 2020-02-06 20:42

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Fixtures',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('short_name', models.CharField(blank=True, max_length=25, null=True)),
                ('goal_opponent_one', models.IntegerField(default=0)),
                ('goal_opponent_two', models.IntegerField(default=0)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('completed', 'Completed')], help_text='Status', max_length=11)),
                ('match_date', models.DateField()),
                ('match_time', models.TimeField()),
                ('date_created', models.DateField(auto_now=True, null=True)),
                ('time_created', models.TimeField(auto_now=True, null=True)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('unique_link', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField(default=0)),
                ('position', models.CharField(max_length=120)),
                ('shirt_no', models.IntegerField()),
                ('nationality', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
                ('image', models.ImageField(default='default.png', max_length=50, upload_to='player')),
                ('date_created', models.DateField(auto_now=True, null=True)),
                ('time_created', models.TimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('logo', models.ImageField(blank=True, default='default.png', max_length=50, null=True, upload_to='team')),
                ('players', django.contrib.postgres.fields.jsonb.JSONField()),
                ('date_created', models.DateField(auto_now=True, null=True)),
                ('time_created', models.TimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TeamPlayers',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('team_id', models.IntegerField()),
                ('player_id', models.CharField(max_length=150)),
                ('player_name', models.CharField(max_length=100)),
                ('player_age', models.CharField(max_length=150)),
                ('player_position', models.CharField(max_length=120)),
                ('player_shirt_no', models.CharField(max_length=150)),
                ('player_nationality', models.CharField(max_length=150)),
                ('player_phone', models.CharField(max_length=15)),
                ('player_image', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('image', models.ImageField(blank=True, default='default.png', max_length=50, null=True, upload_to='profile')),
                ('last_modified', models.DateTimeField(auto_now_add=True, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('is_staff', models.CharField(choices=[('Us', 'Users'), ('Ad', 'Admin')], default='Us', help_text='User Status', max_length=3)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Points',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('played', models.IntegerField()),
                ('goal_difference', models.IntegerField()),
                ('point', models.IntegerField()),
                ('fixture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fixture', to='league.Fixtures')),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('lost', models.IntegerField()),
                ('won', models.IntegerField()),
                ('date_created', models.DateField(auto_now=True, null=True)),
                ('time_created', models.TimeField(auto_now=True, null=True)),
                ('fixture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='match_fixture', to='league.Fixtures')),
            ],
        ),
        migrations.AddField(
            model_name='fixtures',
            name='opponent_one',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='opponent_one', to='league.Team'),
        ),
        migrations.AddField(
            model_name='fixtures',
            name='opponent_two',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='opponent_two', to='league.Team'),
        ),
    ]
