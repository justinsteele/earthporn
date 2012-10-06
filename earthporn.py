import requests
import json
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def earthporn():
	r = requests.get('http://www.reddit.com/r/earthporn/new.json?sort=new')
	images = []
	for post in r.json['data']['children']:
		if post['data']['domain'] == 'i.imgur.com':
			images.append(post['data']['url'])
	return render_template('earthporn.html', images=images)

if __name__ == "__main__":
    app.debug = True
    app.run()