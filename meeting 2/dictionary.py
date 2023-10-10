movie ={
    'title' : "Avangers : End Game",
    'year' : 2019,
    'genre' : 'Advanture'
}

print(movie)
print(movie["year"])

movie.update({'viewers ' : 900000000})
movie["title"] = "Avangers : Infinity war"


print(movie)
del movie["year"]

print(movie)


movies = [{
    "title" : "Frozen",
    "year" : 2014,
    "viewers" : 900000000
}, {
    "title" : "Thor Ragnarok",
    "year" : 2018,
    "viewers" : 123213
}, {
    "title" : "Little Woman",
    "year" : 2019,
    "viewers" : 21234444
}]

print(movies)

print(movies[1]['title'])