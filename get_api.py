import http.client
import config
import json

def get_top_rated_movies():
	conn = http.client.HTTPSConnection("api.themoviedb.org")
	payload = "{}"
	conn.request("GET", "/3/movie/top_rated?page=1&language=en-US&api_key={0}".format(config.api_key), payload)
	res = conn.getresponse()
	data = res.read()
	print("TOP RATED MOVIES")
	info=data.decode("utf-8")
	movies = json.loads(info)['results']
	return movies	


def print_movies(movies):
	for i in range(len(movies)):
		print("title ",movies[i]['title'])
		print("overview",movies[i]['overview'])
		print("poster path ","http://image.tmdb.org/t/p/w185//"+movies[i]['poster_path'])
		print('release_date ',movies[i]['release_date'])
		print('id ',movies[i]['id'])
		print('rating ',movies[i]['vote_average'])


#get_top_rated_movies()
def print_json():
	data=json.load('movie_data.json')
	print(data[0]['title'])
	'''for i in range(len(movies)):
		print("title ",movies[i]['title'])
		print("overview",movies[i]['overview'])
		print("poster path ","http://image.tmdb.org/t/p/w185//"+movies[i]['poster_path'])
		print('release_date ',movies[i]['release_date'])
		print('id ',movies[i]['id'])
		print('rating ',movies[i]['vote_average'])'''

#print_json()	