from django.contrib import admin

from .models import Player, Team, Fixtures, Match, Points, UserProfile


# Register your models here.


class PlayerAdmin(admin.ModelAdmin):
    readonly_fields = ('date_created', 'time_created')


admin.site.register(Player, PlayerAdmin)


class TeamAdmin(admin.ModelAdmin):
    readonly_fields = ('date_created', 'time_created')


admin.site.register(Team, TeamAdmin)


class MatchAdmin(admin.ModelAdmin):
    readonly_fields = ('date_created', 'time_created')


admin.site.register(Match, MatchAdmin)


#
# class PointAdmin(admin.ModelAdmin):
#     readonly_fields = ('created_date', 'time_created')
#
#
# admin.site.register(Points, PointAdmin)


class FixtureAdmin(admin.ModelAdmin):
    # list_display = ('title', 'body',)
    prepopulated_fields = {'slug': ('short_name',)}


admin.site.register(Fixtures, FixtureAdmin)

admin.site.register(UserProfile)
admin.site.register(Points)
# class UserProfileAdmin(admin.ModelAdmin):
#     readonly_fields = ('date', 'time_created')
#
#
# admin.site.register(UserProfile, UserProfileAdmin)
