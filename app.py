# app.py

from flask import Flask, jsonify, render_template
import requests
from collections import Counter

app = Flask(__name__)

def fetch_repos(username, token):
    url = f'https://api.github.com/users/{username}/repos'
    headers = {'Authorization': f'token {token}'}
    response = requests.get(url, headers=headers)
    repos = response.json()
    return repos

def fetch_languages(repo, token):
    url = repo['languages_url']
    headers = {'Authorization': f'token {token}'}
    response = requests.get(url, headers=headers)
    return response.json()

def main(username, token):
    repos = fetch_repos(username, token)

    language_counter = Counter()
    for repo in repos:
        languages = fetch_languages(repo, token)
        language_counter.update(languages)

    # Convert Counter to a dictionary for easy JSON serialization
    language_data = dict(language_counter)
    return language_data

@app.route('/data')
def data():
    # Replace 'your-github-username' and 'your-github-token' with your actual GitHub credentials and remove the hashtag
    # username = ''
    # token = ''
    data = main(username, token)
    return jsonify(data)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
