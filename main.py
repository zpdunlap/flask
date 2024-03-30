from flask import Flask, jsonify
import requests

app = Flask(__name__)

def get_latest_news_stories():
    # ' with your actual API key from News API
    api_key = '7f6e1db3470a441fbdd21e6ad146864f'
    base_url = 'https://newsapi.org/v2/top-headlines'
    params = {
        'apiKey': api_key,
        'country': 'us',
        'pageSize': 5
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        news_stories = response.json()
        for i, story in enumerate(news_stories[:5], start=1):
        news_dict[i] = {
            'title': story['title'],
            'description': story['description']
        }
return news_dict
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return []
    except (KeyError, TypeError) as e:
        print(f"Error: {e}")
        return []

@app.route('/api/news', methods=['GET'])
def get_news():
    # Call the news API here and convert the response to the desired format
    response = requests.get('https://news-api.com/top-stories')
    news = get_latest_news_stories()# process_news_response(response)
    return jsonify(news)
    #users = [{'id': 1, 'username': 'Alice'}, {'id': 2, 'username': 'Bob'}]
    #return jsonify(users, status=200, mimetype='application/json')

@app.route('/api/weather', methods=['GET'])
def get_weather():
    # Call the weather API here and convert the response to the desired format
    response = requests.get('https://weather-api.com/todays-weather')
    weather = process_weather_response(response)
    return jsonify(weather)

@app.route('/api/reddit', methods=['GET'])
def get_reddit():
    # Call the Reddit API here and convert the response to the desired format
    response = requests.get('https://reddit.com/highlights')
    reddit = process_reddit_response(response)
    return jsonify(reddit)

def process_news_response(response):
    # Implement the logic to convert the response from the news API to the desired format
    pass

def process_weather_response(response):
    # Implement the logic to convert the response from the weather API to the desired format
    pass

def process_reddit_response(response):
    # Implement the logic to convert the response from the Reddit API to the desired format
    pass

if __name__ == '__main__':
    app.run(debug=True)
