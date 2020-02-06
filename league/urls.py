from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from rest_framework.routers import DefaultRouter

from .api import PointsViewSet, PlayerViewSet, FixtureViewSet, MatchViewSet, TeamViewSet, FixViewSet, \
    TeamPlayersViewSet, TeamAPIView, FixturesAPIView, ListTeamView, CompletedMatchView, PendingMatchView

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
    url('allteam/', TeamAPIView.as_view()),
    url('allfixture/', FixturesAPIView.as_view()),
    url('vteam/', ListTeamView.as_view()),
    url('completed_match/', CompletedMatchView.as_view()),
    url('pending_match/', PendingMatchView.as_view()),

]
