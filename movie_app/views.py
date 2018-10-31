from django.shortcuts import render
from movie_app.models import *
from get_api import *
# Create your views here.

def index(request):
	is_cached=('titles' in request.session)
	if not is_cached:
		movies=get_top_rated_movies()
		titles=[]
		if movies!=None:		
			for i in range(len(movies)):
				titles.append(movies[i]['title'])
				print(titles[i])
		request.session['titles']=titles

	titles=request.session['titles']
	videos=Videos.objects.all()
	context={'videos':videos,'titles':titles,'is_cached':is_cached}
	return render(request, "movie_app/index.html",context)

def detail(request,slug):
	#video=Videos.objects.get(slug=slug)
	video=slug
	return render(request, 'movie_app/detail.html',{'video':video,})

