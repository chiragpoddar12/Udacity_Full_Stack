import webbrowser

class Movie():
    def __init__(self, title, desc, poster_image_url, trailer_youtube_url):
        self.title = title
        self.desc = desc
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        webbrowser.open(self.url)
