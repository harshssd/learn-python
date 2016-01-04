import urllib.request

def read_text(path):
    quotes_file = open(path)
    quotes = quotes_file.read()
    quotes_file.close()
    return quotes

def check_profanity(text):
    url = "http://www.wdyl.com/profanity?q="+urllib.parse.quote(text)
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    output = response.read().decode('UTF-8')
    return output
    
text = read_text("/Users/somash/Workspace/Python/movie_quotes.txt")
output = check_profanity(text)
if "true" in output:
    print("Profanity Alert!!!")
elif "false" in output:
    print("The file is clean")
else:
    print("Unable to read the file")
