# # Create your tests here.
# import unittest
#
# from django.core.files.uploadedfile import SimpleUploadedFile
# from django.test import TestCase
#
# from .models import Player
#
# class PlayerTest(TestCase):
#
#     """ Test module for Player model """
#
#     def setUp(self):
#         newImage = SimpleUploadedFile(name='test_image.jpg', content=open('media/default.png', 'rb').read(), content_type='image/jpeg')
#         Player.objects.create(name = 'Casper', age = 31, position = 'Striker', shirt_no = 8, nationality = 'Nigerian',
#                               phone = '09098783', image = newImage)
#         Player.objects.create(name = 'Muffin', age = 31, position = 'Striker', shirt_no = 8, nationality = 'Nigerian',
#                               phone = '09098783', image = newImage)
#
#     def test_player_details(self):
#
#         player_casper = Player.objects.get(name='Casper')
#         player_muffin = Player.objects.get(name='Muffin')
#         self.assertEqual(
#             player_casper.get_details(), "Casper is a Nigerian.")
#         self.assertEqual(player_muffin.get_details(), "Muffin is a Nigerian.")
#
# if __name__ == '__main__':
#     unittest.main()

# Create your tests here.
import unittest
import json

from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from .models import Player, Team, Fixtures


# Create your tests here.

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
    """ Test module for Player model """

    def setUp(self):
        newImage = SimpleUploadedFile(name='test_image.jpg', content=open('media/default.png', 'rb').read(),
                                      content_type='image/jpeg')
        Team.objects.create(name='Arsenal', logo=newImage, players=json.loads({
            'id': 1,
            'age': 32,
            'name': 'Mpape gSantiago',
            'image': 'http://127.0.0.1:8000/media/player/default.jpg',
            'phone': '09098765678',
            'position': 'midfield',
            "shirt_no": 8,
            "nationality": 'Czech',
        }))
        Team.objects.create(name='Chelsea', logo=newImage, players=
        [{
            'id': 1,
            'age': 32,
            'name': 'Mpape gSantiago',
            'image': 'http://127.0.0.1:8000/media/player/default.jpg',
            'phone': '09098765678',
            'position': 'midfield',
            "shirt_no": 8,
            "nationality": 'Czech',
        }])

    def test_team_details(self):
        player_arsenal = Team.objects.get(name='Arsenal')
        player_chelsea = Player.objects.get(name='Chelsea')
        self.assertEqual(
            player_arsenal.get_details(), "Arsenal created successfully.")
        self.assertEqual(player_chelsea.get_details(), "Chelsea created successfully..")


# class FixtureTest(TestCase):
#     """ Test module for Player model """
#
#     def setUp(self):
#
#         newImage = SimpleUploadedFile(name='test_image.jpg', content=open('media/default.png', 'rb').read(),
#                                       content_type='image/jpeg')
#         Player.objects.create(name='Casper', age=31, position='Striker', shirt_no=8, nationality='Nigerian',
#                               phone='09098783', image=newImage)
#         Player.objects.create(name='Muffin', age=31, position='Striker', shirt_no=8, nationality='Nigerian',
#                               phone='09098783', image=newImage)
#
#     def test_player_details(self):
#         player_casper = Player.objects.get(name='Casper')
#         player_muffin = Player.objects.get(name='Muffin')
#         self.assertEqual(
#             player_casper.get_details(), "Casper is a Nigerian.")
#         self.assertEqual(player_muffin.get_details(), "Muffin is a Nigerian.")
#

# class MatchTest(TestCase):
#
# """ Test module for Player model """
#
# def setUp(self):
# newImage = SimpleUploadedFile(name='test_image.jpg', content=open('media/default.png', 'rb').read(), content_type='image/jpeg')
# Player.objects.create(name = 'Casper', age = 31, position = 'Striker', shirt_no = 8, nationality = 'Nigerian',
# phone = '09098783', image = newImage)
# Player.objects.create(name = 'Muffin', age = 31, position = 'Striker', shirt_no = 8, nationality = 'Nigerian',
# phone = '09098783', image = newImage)
#
# def test_player_details(self):
#
# player_casper = Player.objects.get(name='Casper')
# player_muffin = Player.objects.get(name='Muffin')
# self.assertEqual(
# player_casper.get_details(), "Casper is a Nigerian.")
# self.assertEqual(player_muffin.get_details(), "Muffin is a Nigerian.")
#
#
# class PointTest(TestCase):
#
# """ Test module for Player model """
#
# def setUp(self):
# newImage = SimpleUploadedFile(name='test_image.jpg', content=open('media/default.png', 'rb').read(), content_type='image/jpeg')
# Player.objects.create(name = 'Casper', age = 31, position = 'Striker', shirt_no = 8, nationality = 'Nigerian',
# phone = '09098783', image = newImage)
# Player.objects.create(name = 'Muffin', age = 31, position = 'Striker', shirt_no = 8, nationality = 'Nigerian',
# phone = '09098783', image = newImage)
#
# def test_player_details(self):
#
# player_casper = Player.objects.get(name='Casper')
# player_muffin = Player.objects.get(name='Muffin')
# self.assertEqual(
# player_casper.get_details(), "Casper is a Nigerian.")
# self.assertEqual(player_muffin.get_details(), "Muffin is a Nigerian.")
#
#
# class TeamPlayerTest(TestCase):
# """ Test module for Player model """
#
# def setUp(self):
# newImage = SimpleUploadedFile(name='test_image.jpg', content=open('media/default.png', 'rb').read(), content_type='image/jpeg')
# Player.objects.create(name = 'Casper', age = 31, position = 'Striker', shirt_no = 8, nationality = 'Nigerian',
# phone = '09098783', image = newImage)
# Player.objects.create(name = 'Muffin', age = 31, position = 'Striker', shirt_no = 8, nationality = 'Nigerian',
# phone = '09098783', image = newImage)
#
# def test_player_details(self):
#
# player_casper = Player.objects.get(name='Casper')
# player_muffin = Player.objects.get(name='Muffin')
# self.assertEqual(
# player_casper.get_details(), "Casper is a Nigerian.")
# self.assertEqual(player_muffin.get_details(), "Muffin is a Nigerian.")
#
#
#
# class UserProfileTest(TestCase):
#
# """ Test module for Player model """
#
# def setUp(self):
# newImage = SimpleUploadedFile(name='test_image.jpg', content=open('media/default.png', 'rb').read(), content_type='image/jpeg')
# Player.objects.create(name = 'Casper', age = 31, position = 'Striker', shirt_no = 8, nationality = 'Nigerian',
# phone = '09098783', image = newImage)
# Player.objects.create(name = 'Muffin', age = 31, position = 'Striker', shirt_no = 8, nationality = 'Nigerian',
# phone = '09098783', image = newImage)
#
# def test_player_details(self):
#
# player_casper = Player.objects.get(name='Casper')
# player_muffin = Player.objects.get(name='Muffin')
# self.assertEqual(
# player_casper.get_details(), "Casper is a Nigerian.")
# self.assertEqual(player_muffin.get_details(), "Muffin is a Nigerian.")
#


class PlayerModelTestCase(TestCase):
    """This class defines the test suite for the bucketlist model."""

    def setUp(self):
        """Define the test client and other test variables."""
        # user = User.objects.create(username="nerd")
        newImage = SimpleUploadedFile(name='test_image.jpg', content=open('media/default.png', 'rb').read(),
                                      content_type='image/jpeg')
        self.name = "Anieka"
        self.age = 31
        self.position = "Midfielder"
        self.shirt_no = 8
        self.nationality = "Nigerian"
        self.phone = "0909877661"
        self.player = Player(name=self.name, age=self.age, position=self.position, shirt_no=self.shirt_no,
                             nationality=self.nationality, phone=self.phone, image=newImage)


class PlayerViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        user = User.objects.create(username="nerd")

        # Initialize client and force it to use authentication
        self.client = APIClient()

        newImage = SimpleUploadedFile(name='test_image.jpg', content=open('media/default.png', 'rb').read(),
                                      content_type='image/jpeg')

        self.player_data = {'name': 'Muffin', 'age': 31, 'position': 'Striker', 'shirt_no': 8,
                            'nationality': 'Nigerian',
                            'phone': '09098783', 'image': newImage}
        self.response = self.client.post(
            reverse('player'),
            self.player_data,
            format="json")

    def test_api_can_create_a_player(self):
        """Test the api has player creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_player(self):
        """Test the api can get a given list."""
        player = Player.objects.get(id=1)
        response = self.client.get(
            '/player/',
            kwargs={'pk': player.id}, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, player)

    def test_api_can_update_player(self):
        """Test the api can update a given Player."""
        player = Player.objects.get()
        change_player = {'name': 'Henry'}
        res = self.client.put(
            reverse('details', kwargs={'pk': player.id}),
            change_player, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_player(self):
        """Test the api can delete a Player."""
        player = Player.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': player.id}),
            format='json',
            follow=True)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)


class TeamViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        user = User.objects.create(username="nerd")

        # Initialize client and force it to use authentication
        self.client = APIClient()

        newImage = SimpleUploadedFile(name='test_image.jpg', content=open('media/default.png', 'rb').read(),
                                      content_type='image/jpeg')

        self.team_data = {'name': 'Manchester United', 'logo': newImage, 'players': {
            [{
                "id": 1,
                "age": 32,
                "name": "Mpape Santiago",
                "image": "http://127.0.0.1:8000/media/player/default.jpg",
                "phone": "09098765678",
                "position": "midfield",
                "shirt_no": 8,
                "nationality": "Czech",
            },
                {
                    "id": 2,
                    "age": 32,
                    "name": "Diego",
                    "image": "http://127.0.0.1:8000/media/player/default.jpg",
                    "phone": "09098765678",
                    "position": "Striker",
                    "shirt_no": 11,
                    "nationality": "Czech",
                },
            ]
        }}
        self.response = self.client.post(
            reverse('create'),
            self.team_data,
            format="json")

    def test_api_can_create_a_team(self):
        """Test the api has player creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

        def test_api_can_get_a_team(self):
            """Test the api can get a given bucketlist."""

        team = Team.objects.get(id=1)
        response = self.client.get(
            '/team/',
            kwargs={'pk': team.id}, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, team)

    def test_api_can_update_team(self):
        """Test the api can update a given Player."""
        team = Team.objects.get()
        change_team = {'name': 'Arsenal'}
        res = self.client.put(
            reverse('details', kwargs={'pk': team.id}),
            change_team, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_team(self):
        """Test the api can delete a Player."""
        team = Team.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': team.id}),
            format='json',
            follow=True)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)


class FixturesViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        newImage = SimpleUploadedFile(name='test_image.jpg', content=open('media/default.png', 'rb').read(),
                                      content_type='image/jpeg')

        team_one = Team.objects.create(name='Manchester United', logo=newImage, players={
            [{
                "id": 1,
                "age": 32,
                "name": "Mpape Santiago",
                "image": "http://127.0.0.1:8000/media/player/default.jpg",
                "phone": "09098765678",
                "position": "midfield",
                "shirt_no": 8,
                "nationality": "Czech",
                "date_created": "2020-02-05",
                "time_created": "03:58:22.967862"
            },
                {
                    "id": 2,
                    "age": 32,
                    "name": "Diego",
                    "image": "http://127.0.0.1:8000/media/player/default.jpg",
                    "phone": "09098765678",
                    "position": "Striker",
                    "shirt_no": 11,
                    "nationality": "Czech"
                },
            ]
        })
        team_two = Team.objects.create(name='Chelsea', logo=newImage, players={
            [{
                "id": 1,
                "age": 32,
                "name": "Mpape Santiago",
                "image": "http://127.0.0.1:8000/media/player/default.jpg",
                "phone": "09098765678",
                "position": "midfield",
                "shirt_no": 8,
                "nationality": "Czech"
            },
                {
                    "id": 2,
                    "age": 32,
                    "name": "Diego",
                    "image": "http://127.0.0.1:8000/media/player/default.jpg",
                    "phone": "09098765678",
                    "position": "Striker",
                    "shirt_no": 11,
                    "nationality": "Czech"
                },
            ]
        })

        # Initialize client
        self.client = APIClient()

        self.fixture_data = {'short_name': 'trsetg', 'opponent_one': team_one.id, 'opponent_two': team_two.id,
                             'goal_opponent_one': 0, 'goal_opponent_two': 0, 'status': 'pending',
                             'match_date': '08/08/2020',
                             'match_time': '09:00', 'slug': ''}
        self.response = self.client.post(
            reverse('create'),
            self.fixture_data,
            format="json")

    def test_api_can_create_a_fixture(self):
        """Test the api has player creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_fixture(self):
        """Test the api can get a given bucketlist."""
        fixture = Fixtures.objects.get(id=1)
        response = self.client.get(
            '/fixture/',
            kwargs={'pk': fixture.id}, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, fixture)

    def test_api_can_update_fixture(self):
        """Test the api can update a given Player."""
        fixture = Fixtures.objects.get()
        change_player = {'short_name': 'Hy34d'}
        res = self.client.put(
            reverse('details', kwargs={'pk': fixture.id}),
            change_player, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_fixture(self):
        """Test the api can delete a Player."""
        fixture = Fixtures.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': fixture.id}),
            format='json',
            follow=True)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)


if __name__ == '__main__':
    unittest.main()
