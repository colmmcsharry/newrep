from flask import Flask, render_template, request, jsonify
import requests


app = Flask(__name__)

@app.route('/')
def template():
	return render_template('index.html')

@app.route('/hackernews')
def hackernews():
	
	response = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty')
	storiesid = response.json()[:10] #get the storie id of the first 5 top stories 

	titles = [] 

	stories = []



	for id in storiesid:
	    curr_story_api_url = 'https://hacker-news.firebaseio.com/v0/item/{}.json?print=pretty'.format(id)
	    curr_story = requests.get(curr_story_api_url)
	    stories.append(curr_story.json())

	for ids in stories:
	    current_url = 'https://hacker-news.firebaseio.com/v0/item/{}.json?print=pretty'.format(ids)
	    currenttitles = requests.get(current_url)
	    if 'kids' in ids:
	        title = ids['title']
	        titles.append(title) 
	        titles.sort()

	return jsonify(titles)

if __name__ == '__main__':
	app.run()