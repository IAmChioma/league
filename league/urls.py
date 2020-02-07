from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from rest_framework.routers import DefaultRouter

from .api import PointsViewSet, PlayerViewSet, FixtureViewSet, MatchViewSet, TeamViewSet, FixViewSet, \
    TeamPlayersViewSet, TeamAPIView, FixturesAPIView, ListTeamView, CompletedMatchView, PendingMatchView, ListPlayerView

router = DefaultRouter()
router.register(r'match', MatchViewSet)
router.register(r'fixture', FixtureViewSet)
router.register(r'team', TeamViewSet)
router.register(r'player', PlayerViewSet)
router.register(r'points', PointsViewSet)
router.register(r'test', FixViewSet)
router.register(r'tp', TeamPlayersViewSet)

urlpatterns = router.urls
urlpatterns += [

    #   url(r'viewteam', SelectTeamView.as_view(), cache_page(60 * 15)),
    url('allteam/', TeamAPIView.as_view(), name='allteam'),
    url('allfixture/', FixturesAPIView.as_view(), name='allfix'),
    url('vteam/', ListTeamView.as_view(), name='viewteam'),
    url('completed_match/', CompletedMatchView.as_view(), name='completed'),
    url('pending_match/', PendingMatchView.as_view(), name='pending'),
    url('vpl/', ListPlayerView.as_view(), name='plist'),

]
