# # Create your tests here.
# import unittest
#
# from django.core.files.uploadedfile import SimpleUploadedFile
# from django.test import TestCase
# from ..models import Player, Team, Fixtures, Match, Points, UserProfile, TeamPlayers
#
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
#
#
# class TeamTest(TestCase):
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
#
#
# class FixtureTest(TestCase):
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
#
# class MatchTest(TestCase):
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
#
# class PointTest(TestCase):
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
#
#
# class TeamPlayerTest(TestCase):
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
#
#
# class UserProfileTest(TestCase):
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
#
# if __name__ == '__main__':
#     unittest.main()
