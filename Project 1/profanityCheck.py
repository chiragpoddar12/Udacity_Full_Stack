import urllib

def readFile():
    quotes = open("C:\Chirag\Udacity Full Stack Web Development\Project 1\movie_quotes.txt")
    content = quotes.read()
    check_profanity(content)
    quotes.close()

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    response = connection.read()
    if "true" in response:
        print "Profanity Alert"
    else:
        print "No Profanity"

    connection.close()
readFile()
