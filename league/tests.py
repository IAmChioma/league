
import unittest
import json

from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from .models import Player, Team, Fixtures
from .serializers import TeamSerializer, PlayerSerializer, PointsSerializer, UserProfileSerializer, FixtureSerializer, \
    MatchSerializer, FixSerializer, TeamPlayersSerializer


# Create your tests here.
client = APIClient()


class PlayerTest(TestCase):
    """ Test module for Player model """

    def setUp(self):
        newImage = SimpleUploadedFile(name='test_image.jpg', content=open('media/default.png', 'rb').read(),
                                      content_type='image/jpeg')
        Player.objects.create(name='Casper', age=31, position='Striker', shirt_no=8, nationality='Nigerian',
                              phone='09098783', image=newImage)
        Player.objects.create(name='Muffin', age=31, position='Striker', shirt_no=8, nationality='Nigerian',
                              phone='09098783', image=newImage)

    def test_player_details(self):
        player_casper = Player.objects.get(name='Casper')
        player_muffin = Player.objects.get(name='Muffin')
        self.assertEqual(
            player_casper.get_details(), "Casper is a Nigerian.")
        self.assertEqual(player_muffin.get_details(), "Muffin is a Nigerian.")


class TeamTest(TestCase):
    """ Test module for Team model """

    def setUp(self):
        newImage = SimpleUploadedFile(name='test_image.jpg', content=open('media/default.png', 'rb').read(),
                                      content_type='image/jpeg')
        Team.objects.create(name='Arsenal', logo=newImage, players=json.dumps({
            'id': 1,
            'age': 32,
            'name': 'Mpape gSantiago',
            'image': 'http://127.0.0.1:8000/media/player/default.jpg',
            'phone': '09098765678',
            'position': 'midfield',
            'shirt_no': 8,
            'nationality': 'Czech',
        }))

    def test_team_details(self):
        player_arsenal = Team.objects.get(name='Arsenal')
        self.assertEqual(
            player_arsenal.get_details(), "Arsenal created successfully.")


class FixtureTest(TestCase):
    """ Test module for Fixture model """

    def setUp(self):
        newImage = SimpleUploadedFile(name='test_image.jpg', content=open('media/default.png', 'rb').read(),
                                      content_type='image/jpeg')

        team_one = Team.objects.create(name='Arsenal', logo=newImage, players=json.dumps({
            'id': 1,
            'age': 32,
            'name': 'Mpape gSantiago',
            'image': 'http://127.0.0.1:8000/media/player/default.jpg',
            'phone': '09098765678',
            'position': 'midfield',
            'shirt_no': 8,
            'nationality': 'Czech',
        }))
        team_two = Team.objects.create(name='Chelsea', logo=newImage, players=json.dumps({
            'id': 1,
            'age': 32,
            'name': 'Mpape gSantiago',
            'image': 'http://127.0.0.1:8000/media/player/default.jpg',
            'phone': '09098765678',
            'position': 'midfield',
            'shirt_no': 8,
            'nationality': 'Czech',
        }))

        Fixtures.objects.create(short_name='',opponent_one=team_one, opponent_two=team_two, goal_opponent_one=0,
                                goal_opponent_two=0, status='pending', match_date='2020-02-07', match_time='07:41:50',
                                slug='', unique_link='')

    def test_fixture_details(self):
        player_pending = Player.objects.get(name='pending')
        self.assertEqual(
            player_pending.get_details(), "pending created successfully.")


class GetAllPlayer(TestCase):
    def setUp(self):
        newImage = SimpleUploadedFile(name='test_image.jpg', content=open('media/default.png', 'rb').read(),
                                      content_type='image/jpeg')
        Player.objects.create(name='Casper', age=31, position='Striker', shirt_no=8, nationality='Nigerian',
                              phone='09098783', image=newImage)
        Player.objects.create(name='Muffin', age=31, position='Striker', shirt_no=8, nationality='Nigerian',
                              phone='09098783', image=newImage)

    def test_get_all_players(self):
        client.login(username='lauren', password='secret')

        response = client.get(reverse('plist'))
        players = Player.objects.all()
        serializer = PlayerSerializer(players, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


if __name__ == '__main__':
    unittest.main()
