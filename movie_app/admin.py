from django.contrib import admin
from movie_app.models import Users,Videos,Favourites
# Register your models here.

class VideosAdmin(admin.ModelAdmin):
	model=Videos
	prepopulated_fields={'slug':('video_title',)}

admin.site.register(Users)
admin.site.register(Videos,VideosAdmin)
admin.site.register(Favourites)