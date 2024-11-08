import requests
import send_email as se

topic = 'anime'
api_key = 'fb63e499cc284155baae7a1541c6447b'
url = (f'https://newsapi.org/v2/everything?q={topic}&from=2024-11-01&to=2024-11-07&'
       'sortBy=relevancy&apiKey=fb63e499cc284155baae7a1541c6447b&language=en')

# Request url from given to a variable
request = requests.get(url)

# Convert request to a json file, creating a dict variable
content = request.json()

# Iterate over the articles in the variable content (dict), then message all top articles to user in one email
email_message = "Subject: Anime News \n"
for article in content['articles'][:20]:
    if article['title'] is None or article['description'] is None:
        continue
    email_message = email_message + article['title'] + "\n" + article['description'] + "\n" + article['url'] + 2*"\n"

se.send_email(email_message)
