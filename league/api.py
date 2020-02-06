from django.db import connection
import collections
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.db import connection
from rest_framework import filters
from rest_framework import status, views, generics, viewsets, permissions
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle
from rest_framework.viewsets import ModelViewSet

from premier import settings
from .models import Player, Team, Fixtures, Match, Points, UserProfile, TeamPlayers
from .serializers import TeamSerializer, PlayerSerializer, PointsSerializer, UserProfileSerializer, FixtureSerializer, \
    MatchSerializer, FixSerializer, TeamPlayersSerializer

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


class TeamAPIView(generics.ListCreateAPIView):
    search_fields = ['name', 'logo', 'players']
    filter_backends = (filters.SearchFilter,)
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    throttle_classes = [UserRateThrottle]


class FixturesAPIView(generics.ListCreateAPIView):
    search_fields = ['short_name', 'opponent_one__name', 'opponent_two__name', 'status', 'match_date', 'match_time']
    filter_backends = (filters.SearchFilter,)
    queryset = Fixtures.objects.all()
    serializer_class = FixtureSerializer
    throttle_classes = [UserRateThrottle]


# @method_decorator(user_passes_test(lambda u: Group.objects.get(name='Admin') in u.groups.all()),
#                   name='dispatch')
class FixtureViewSet(ModelViewSet):
    queryset = Fixtures.objects.all()
    serializer_class = FixtureSerializer
    throttle_classes = [UserRateThrottle]
    # permission_classes = (permissions.IsAuthenticated,)


class MatchViewSet(ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
    throttle_classes = [UserRateThrottle]
    # permission_classes = (permissions.IsAuthenticated,)


class TeamViewSet(ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    throttle_classes = [UserRateThrottle]
    # permission_classes = (permissions.IsAuthenticated,)


class UserProfileViewSet(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (permissions.IsAuthenticated,)
    throttle_classes = [UserRateThrottle]


class PointsViewSet(ModelViewSet):
    queryset = Points.objects.all()
    serializer_class = PointsSerializer
    permission_classes = (permissions.IsAuthenticated,)
    throttle_classes = [UserRateThrottle]


class PlayerViewSet(ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    permission_classes = (permissions.IsAuthenticated,)
    throttle_classes = [UserRateThrottle]


class TeamPlayersViewSet(ModelViewSet):
    queryset = TeamPlayers.objects.all()
    serializer_class = TeamPlayersSerializer
    throttle_classes = [UserRateThrottle]
    # permission_classes = (permissions.IsAuthenticated,)


class ListTeamView(generics.ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    throttle_classes = [UserRateThrottle]
    #
    # def get(self, request):
    #     # Note the use of `get_queryset()` instead of `self.queryset`
    #     serializer = TeamSerializer
    #     team = Team.objects.all()
    #     return Response(team)


class FixViewSet(viewsets.ModelViewSet):
    queryset = Fixtures.objects.all()
    serializer_class = FixSerializer
    lookup_field = 'slug'


class checkTeam(object):

    def get_category(team_id):
        try:
            cur = connection.cursor()
            cur.callproc('select_team', [team_id])
            rows = cur.fetchall()

            field_names = [i[0] for i in cur.description]

            objects_list = []
            for row in rows:
                d = collections.OrderedDict()
                d[field_names[0]] = row[0]
                d[field_names[1]] = row[1]
                d[field_names[2]] = row[2]
                d[field_names[3]] = row[3]
                d[field_names[4]] = row[4]
                d[field_names[5]] = row[5]
                d[field_names[6]] = row[6]

                objects_list.append(d)

            print(objects_list)
            return objects_list
        except Team.DoesNotExist:
            return None


# @cache_page(CACHE_TTL)
class SelectTeamView(views.APIView):
    # permission_classes = (permissions.IsAuthenticated,)
    def post(self, request):
        team = checkTeam.get_category(
            team_id=request.data.get("team_id"),

        )
        print(team)
        if team is None:
            return Response({
                'status': 'No such team',
                'message': 'Team not found'
            }, status=status.HTTP_404_NOT_FOUND)

        else:
            return Response(team)


class checkMatch(object):

    def get_category():
        try:
            cur = connection.cursor()
            cur.callproc('completed_match')
            rows = cur.fetchall()

            field_names = [i[0] for i in cur.description]

            objects_list = []
            for row in rows:
                d = collections.OrderedDict()
                d[field_names[0]] = row[0]
                d[field_names[1]] = row[1]
                d[field_names[2]] = row[2]
                d[field_names[3]] = row[3]
                d[field_names[4]] = row[4]
                d[field_names[5]] = row[5]
                d[field_names[6]] = row[6]
                d[field_names[7]] = row[7]
                d[field_names[8]] = row[8]
                d[field_names[9]] = row[9]
                d[field_names[10]] = row[10]

                objects_list.append(d)

            print(objects_list)
            return objects_list
        except Team.DoesNotExist:
            return None


class CompletedMatchView(views.APIView):
    # permission_classes = (permissions.IsAuthenticated,)
    def get(self, request):
        team = checkMatch.get_category()
        print(team)
        if team is None:
            return Response({
                'status': 'No such team',
                'message': 'Team not found'
            }, status=status.HTTP_404_NOT_FOUND)

        else:
            return Response(team)


class checkPendingMatch(object):

    def get_category():
        try:
            cur = connection.cursor()
            cur.callproc('pending_match')
            rows = cur.fetchall()

            field_names = [i[0] for i in cur.description]

            objects_list = []
            for row in rows:
                d = collections.OrderedDict()
                d[field_names[0]] = row[0]
                d[field_names[1]] = row[1]
                d[field_names[2]] = row[2]
                d[field_names[3]] = row[3]
                d[field_names[4]] = row[4]
                d[field_names[5]] = row[5]
                d[field_names[6]] = row[6]
                d[field_names[7]] = row[7]
                d[field_names[8]] = row[8]
                d[field_names[9]] = row[9]
                d[field_names[10]] = row[10]

                objects_list.append(d)

            print(objects_list)
            return objects_list
        except Fixtures.DoesNotExist:
            return None


# cache_page(CACHE_TTL)
class PendingMatchView(views.APIView):
    # permission_classes = (permissions.IsAuthenticated,)
    def get(self, request):
        pending_match = checkPendingMatch.get_category()
        print(pending_match)
        if pending_match is None:
            return Response({
                'status': 'No such match',
                'message': 'Match not found'
            }, status=status.HTTP_404_NOT_FOUND)

        else:
            return Response(pending_match)
