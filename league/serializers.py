import base64
import uuid

import six
from django.core.files.base import ContentFile
from rest_framework import serializers

from .models import Player, Team, Fixtures, Match, Points, UserProfile, TeamPlayers


class Base64ImageField(serializers.ImageField):

    def to_internal_value(self, data):

        # Check if this is a base64 string
        if isinstance(data, six.string_types):
            # Check if the base64 string is in the "data:" format
            if 'data:' in data and ';base64,' in data:
                # Break out the header from the base64 content
                header, data = data.split(';base64,')

            # Try to decode the file. Return validation error if it fails.
            try:
                decoded_file = base64.b64decode(data)
            except TypeError:
                self.fail('invalid_image')

            # Generate file name:
            file_name = str(uuid.uuid4())[:12]  # 12 characters are more than enough.
            # Get the file name extension:
            file_extension = self.get_file_extension(file_name, decoded_file)

            complete_file_name = "%s.%s" % (file_name, file_extension,)

            data = ContentFile(decoded_file, name=complete_file_name)

        return super(Base64ImageField, self).to_internal_value(data)

    def get_file_extension(self, file_name, decoded_file):
        import imghdr

        extension = imghdr.what(file_name, decoded_file)
        extension = "jpg" if extension == "jpeg" else extension

        return extension


class PlayerSerializer(serializers.ModelSerializer):
    image = Base64ImageField()

    class Meta:
        model = Player
        fields = '__all__'


class TeamSerializer(serializers.ModelSerializer):
    logo = Base64ImageField()

    class Meta:
        model = Team
        fields = '__all__'
    #  depth = 2


class FixtureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fixtures
        fields = '__all__'


class PointsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Points
        fields = '__all__'


class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'


class UserProfileSerializer(serializers.ModelSerializer):
    image = Base64ImageField()

    class Meta:
        model = UserProfile
        fields = '__all__'


class FixSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Fixtures
        fields = ('id', 'short_name', 'opponent_one', 'opponent_two', 'goal_opponent_one', 'goal_opponent_two', 'slug',
                  'status', 'match_date', 'match_time', 'date_created', 'time_created')
        lookup_field = 'slug'
        # extra_kwargs = {
        #     'url': {'lookup_field': 'slug'}
        # }


class TeamPlayersSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamPlayers
        fields = '__all__'
