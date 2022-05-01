from flask import Flask,render_template
# from app import app
from newsapi import NewsApiClient


app = Flask(__name__)

@app.route('/')
def index():

    newapi = NewsApiClient(api_key="7497b8a3477240c181b4b85f120d9d24") 
    topheadlines = newapi.get_top_headlines(sources="bbc-news")
    articles = topheadlines['articles']


    news = []
    description = []
    link = []
    image = []
    time = []
    content = []

    for i in range(len(articles)):
        myarticles = articles [i]
        news.append(myarticles['title'])
        description.append(myarticles['description'])
        link.append(myarticles['url'])
        image.append(myarticles['urlToImage'])
        time.append(myarticles['publishedAt'])
        content.append(myarticles ['content'])

    my_list = zip( news,description,link,image,time,content)

    return render_template('index.html',context=my_list)

@app.route('/homepage')
def homepage():
    return render_template('homepage.html')
    
# sports route
@app.route('/sports')
def sports():

    newapi = NewsApiClient(api_key="7497b8a3477240c181b4b85f120d9d24") 
    topheadlines = newapi.get_top_headlines(sources="ESPN")

    articles = topheadlines['articles']
    news = []
    description = []
    link = []
    image = []
    time = []
    content = []

    for i in range(len(articles)):
        myarticles = articles [i]
        news.append(myarticles['title'])
        description.append(myarticles['description'])
        link.append(myarticles['url'])
        image.append(myarticles['urlToImage'])
        time.append(myarticles['publishedAt'])
        content.append(myarticles ['content'])

    my_list = zip( news,description,link,image,time,content)

    return render_template('sports.html',context=my_list)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)