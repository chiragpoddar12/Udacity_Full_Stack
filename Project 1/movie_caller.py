import fresh_tomatoes
import movie

#Movie 1
avatar = movie.Movie("Avatar",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")
#Movie 2
znmd = movie.Movie("Zindagi Na Milegi Dobara",
                   "https://upload.wikimedia.org/wikipedia/en/3/3d/Zindaginamilegidobara.jpg",
                   "https://www.youtube.com/watch?v=ifIBOKCfjVs")
#Movie 3
wows = movie.Movie("The Wolf of Wall Street",
                   "http://cdn1.bigcommerce.com/n-ou1isn/5irfm624/products/101/images/287/WolfofWallstreet_CastPoster__22694.1395356658.352.316.jpg?c=2",
                   "https://www.youtube.com/watch?v=iszwuX1AK6A")
#Movie 4
mib = movie.Movie("Men In Black",
                  "http://assets.flicks.co.nz/images/movies/poster/c9/c96c08f8bb7960e11a1239352a479053_500x735.jpg",
                  "https://www.youtube.com/watch?v=HYUd7AOw_lk")
#Movie 5
udaan = movie.Movie("Udaan",
                    "http://www.impawards.com/intl/india/2010/posters/udaan.jpg",
                    "https://www.youtube.com/watch?v=wEJxe2bE-cE")
#Movie 6
tzp = movie.Movie("Taare Zameen Par",
                  "https://images-na.ssl-images-amazon.com/images/M/MV5BNTVmYTk2NjAtYzY3MS00YjFjLTlkYzktYzg3YzMyZDQyOWRiXkEyXkFqcGdeQXVyNjQ2MjQ5NzM@._V1_QL50_SY1000_CR0,0,692,1000_AL_.jpg",
                  "https://www.youtube.com/watch?v=tn_2Ie_jtX8")

#Creating a list of all the above movies
movies = [avatar, znmd, wows, mib, udaan, tzp]

#using fresh_tomatoes to see the application in web browser
fresh_tomatoes.open_movies_page(movies)
