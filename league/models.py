from django.db import models
from io import BytesIO
from django.db import connection
from django.contrib.auth.models import User
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
from django.contrib.postgres.fields import JSONField
import collections

# Create your models here.
from django.template.defaultfilters import slugify
import collections
import sys
from io import BytesIO

from PIL import Image
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import connection
from django.db import models
# Create your models here.
from django.template.defaultfilters import slugify

mySite = 'http://127.0.0.1:8000/league/fix/'


class Player(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    position = models.CharField(max_length=120)
    shirt_no = models.IntegerField()
    nationality = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    image = models.ImageField(upload_to='player', max_length=50, default='default.png')
    date_created = models.DateField(auto_now=True, null=True, blank=True)
    time_created = models.TimeField(auto_now=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        # Opening the uploaded image
        im = Image.open(self.image)

        output = BytesIO()

        # Resize/modify the image
        im = im.resize((200, 200))

        # after modifications, save it to the output
        im.save(output, format='PNG', quality=95, optimize=True, dpi=(200, 200))
        output.seek(0)

        # change the imagefield value to be the newley modifed image value
        self.image = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % self.image.name.split('.')[0],
                                          'image/jpeg',
                                          sys.getsizeof(output), None)

        super(Player, self).save(*args, **kwargs)

    def get_details(self):
        return self.name + ' is a ' + self.nationality + '.'

    def __str__(self):
        return "{}".format(self.name)


class Team(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='team', max_length=50, null=True, blank=True, default='default.png')
    players = JSONField()
    date_created = models.DateField(auto_now=True, null=True, blank=True)
    time_created = models.TimeField(auto_now=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        # Opening the uploaded image
        im = Image.open(self.logo)

        output = BytesIO()

        # Resize/modify the image
        im = im.resize((200, 200))

        # after modifications, save it to the output
        im.save(output, format='PNG', quality=95, optimize=True, dpi=(200, 200))
        output.seek(0)

        # change the imagefield value to be the newley modifed image value
        self.logo = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % self.logo.name.split('.')[0],
                                         'image/jpeg',
                                         sys.getsizeof(output), None)

        super(Team, self).save(*args, **kwargs)

    def get_details(self):
        return self.name + ' created successfully.'

    def __str__(self):
        return "{}".format(self.name)


class Fixtures(models.Model):
    id = models.AutoField(primary_key=True)
    short_name = models.CharField(max_length=25, null=True, blank=True)
    opponent_one = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="opponent_one")
    opponent_two = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="opponent_two")
    goal_opponent_one = models.IntegerField(default=0)
    goal_opponent_two = models.IntegerField(default=0)
    OPTIONS = (
        ('pending', 'Pending'),
        ('completed', 'Completed'),

    )

    status = models.CharField(max_length=11, choices=OPTIONS, help_text='Status')
    match_date = models.DateField()
    match_time = models.TimeField()
    date_created = models.DateField(auto_now=True, null=True, blank=True)
    time_created = models.TimeField(auto_now=True, null=True, blank=True)
    slug = models.SlugField(null=False, blank=True, unique=True)
    unique_link = models.CharField(max_length=200, null=True, blank=True)

    def save(self, *args, **kwargs):
        try:

            cur = connection.cursor()
            cur.callproc('alphanumericserial')
            rows = cur.fetchall()
            print('testing', rows)
            field_names = [i[0] for i in cur.description]

            objects_list = []
            for row in rows:
                d = collections.OrderedDict()
                d[field_names[0]] = row[0]
                self.short_name = row[0]
                self.unique_link = mySite + row[0]
                self.slug = slugify(self.short_name)
                if not self.slug:
                    self.slug = slugify(self.short_name)
                objects_list.append(d)
            print(objects_list)

            super(Fixtures, self).save(*args, **kwargs)
        except Fixtures.DoesNotExist:
            return None

        # if not self.slug:
        #     self.slug = slugify(self.short_name)
        # return super().save(*args, **kwargs)

    def __str__(self):
        return "{}".format(self.status)


class Match(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    fixture = models.ForeignKey(Fixtures, on_delete=models.CASCADE, related_name="match_fixture")
    lost = models.IntegerField()
    won = models.IntegerField()
    date_created = models.DateField(auto_now=True, null=True, blank=True)
    time_created = models.TimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return "{}".format(self.name)


class Points(models.Model):
    id = models.AutoField(primary_key=True)
    fixture = models.ForeignKey(Fixtures, on_delete=models.CASCADE, related_name="fixture")
    played = models.IntegerField()
    goal_difference = models.IntegerField()
    point = models.IntegerField()

    def __str__(self):
        return "{}".format(self.point)


class UserProfile(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='profile', max_length=50, default='default.png', null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    last_modified = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    email = models.EmailField()
    STATUSES = (
        ('Us', 'Users'),
        ('Ad', 'Admin'),
    )

    is_staff = models.CharField(max_length=3, choices=STATUSES, default='Us', help_text='User Status')

    def save(self, *args, **kwargs):
        # Opening the uploaded image
        im = Image.open(self.image)

        output = BytesIO()

        # Resize/modify the image
        im = im.resize((200, 200))

        # after modifications, save it to the output
        im.save(output, format='PNG', quality=95, optimize=True, dpi=(200, 200))
        output.seek(0)

        # change the imagefield value to be the newley modifed image value
        self.image = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % self.image.name.split('.')[0],
                                          'image/jpeg',
                                          sys.getsizeof(output), None)

        super(UserProfile, self).save(*args, **kwargs)


class TeamPlayers(models.Model):
    id = models.AutoField(primary_key=True)
    team_id = models.IntegerField()
    player_id = models.CharField(max_length=150)
    player_name = models.CharField(max_length=100)
    player_age = models.CharField(max_length=150)
    player_position = models.CharField(max_length=120)
    player_shirt_no = models.CharField(max_length=150)
    player_nationality = models.CharField(max_length=150)
    player_phone = models.CharField(max_length=15)
    player_image = models.CharField(max_length=150)

    def __str__(self):
        return "{}".format(self.player_name)
