import fresh_tomatoes
import movie

avatar = movie.Movie("Avatar", "Avatar Desc",
                     "https://www.google.co.in/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=0ahUKEwiFk7-1y4bTAhWDa7wKHRakCe4QjRwIBw&url=http%3A%2F%2Fwww.foxmovies.com%2Fmovies%2Favatar%2Fposters%2F251%2Favatar-poster-01&bvm=bv.151325232,d.dGc&psig=AFQjCNGpuLOZdADfZBwmLl38nMFaU_WVeg&ust=1491250557945408",
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")
movies = [avatar, avatar, avatar]

#fresh_tomatoes.open_movies_page(movies)

print movie.Movie.__name__
print movie.Movie.__doc__
print movie.Movie.__module__
