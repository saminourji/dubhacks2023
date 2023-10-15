from flask import Flask


import json
import requests
import os
import openai
import re
from apikeys import TAVILY_APIKEY, OPENAI_APIKEY
from article_selection import get_five_articles
# from scraper import get_body_text_from_urls

app = Flask(__name__)

os.environ["OPENAI_API_KEY"] = OPENAI_APIKEY
openai.api_key = OPENAI_APIKEY

@app.route('/get_text')
def get_text():
    # Base URL and endpoint
    base_url = "https://api.tavily.com/"
    endpoint = "search"

    topic = "Israel Palestine Conflict"

    tsummary_payload = {
        "query": f"Explain the topic '{topic}' by giving past history, and providing context on recent events.",
        "search_depth": "basic",
        "include_answer": True,
        "include_raw_content": False,
        "exclude_domains": ["wikipedia.com", "apnews.com/hub"],
        "max_results": 10,
        "api_key": TAVILY_APIKEY
    }

    tsummary_payload_json = json.dumps(tsummary_payload)

    headers = {
        "Content-Type": "application/json"
    }

    print("Getting topic summary")
    tsummary = requests.post(f"{base_url}{endpoint}",
                            data=tsummary_payload_json, headers=headers)

    topic_summary = tsummary.json()["answer"].split("\nSource")[0]
    return topic_summary

@app.route('/get_articles')
def get_articles():
    # Base URL and endpoint
    base_url = "https://api.tavily.com/"
    endpoint = "search"

    topic = "Israel Palestine Conflict"

    tsummary_payload = {
        "query": f"Explain the topic '{topic}' by giving past history, and providing context on recent events.",
        "search_depth": "basic",
        "include_answer": True,
        "include_raw_content": False,
        "exclude_domains": ["wikipedia.com", "apnews.com/hub"],
        "max_results": 10,
        "api_key": TAVILY_APIKEY
    }

    article_payload = {
        "query": f"Give news articles discussing the topic '{topic}' with a wide range of perspectives. No government websites. Do not include a media outlet domain as a source more than once",
        "search_depth": "basic",
        "include_answer": False,
        "include_raw_content": True,
        "exclude_domains": ["wikipedia.com", "apnews.com/hub"],
        "max_results": 10,
        "api_key": TAVILY_APIKEY
    }


    

    article_payload_json = json.dumps(article_payload)
    tsummary_payload_json = json.dumps(tsummary_payload)

    headers = {
        "Content-Type": "application/json"
    }

    print("Getting topic summary")
    tsummary = requests.post(f"{base_url}{endpoint}",
                            data=tsummary_payload_json, headers=headers)

    print("Getting articles on topic")
    articles = requests.post(f"{base_url}{endpoint}",
                            data=article_payload_json, headers=headers)

    result_list = []
    links = []
    topic_summary = tsummary.json()["answer"].split("\nSource")[0]
    

    messages = [{
        "role": "system",
        "content": "You are a professional news interpreter and political scientist. You will perform two tasks.\nWhat I will send:\n1. a query in the format \\\"search topic = [TOPIC, TOPIC SUMMARY]\\\". \n2. queries in the format \\\"title = [TITLE], url = [URL], article = [ARTICLE]\\\". [TITLE] is the title of the article, [URL] is the article's url, and [ARTICLE] contains raw texts from an article about [TOPIC].\nWhat you will do:\nUsing 1., You will generate the two main points of view (pov) on [TOPIC] based on the given description [TOPIC SUMMARY]. Then, for each [ARTICLE], you will give a descriptive summary, get the media outlet name, and rank the article on a scale of FIVE levels of opinions on [TOPIC], 1 being the first main point of view, 3 being a balanced point of view, and 5 being the second main point of view. \nSummarize all this information in a JSON format using this template with propper formatting:\n{\n  \"povs\": [\n    {\"pov_title\": \"POV1 TITLE\", \"description\": \"POV1 DESCRIPTION\"},\n    {\"pov_title\": \"POV2 TITLE\", \"description\": \"POV2 DESCRIPTION\"}\n  ],\n  \"scale\": [\n    {\"level_title\": \"LEVEL1 NUMBER AND TITLE\", \"description\": \"LEVEL1 DESCRIPTION\"},\n    {\"level_title\": \"LEVEL2 NUMBER AND TITLE\", \"description\": \"LEVEL2 DESCRIPTION\"},\n    {\"level_title\": \"LEVEL3 NUMBER AND TITLE\", \"description\": \"LEVEL3 DESCRIPTION\"},\n    {\"level_title\": \"LEVEL4 NUMBER AND TITLE\", \"description\": \"LEVEL4 DESCRIPTION\"},\n    {\"level_title\": \"LEVEL5 NUMBER AND TITLE\", \"description\": \"LEVEL5 DESCRIPTION\"}\n  ],\n  \"articles\": [\n    {\"title\": \"ARTICLE TITLE\", \"url\": \"ARTICLE URL\", \"media\": \"MEDIA NAME\", \"summary\": \"ARTICLE SUMMARY\", \"level\": \"SCALE LEVEL NUMBER\"},\n    // ... (for each article)\n  ]\n}"
        },
        {
        "role": "user",
        "content": f"search topic = {topic}, {topic_summary}"
    }]
    cap = 2650
    if articles.status_code != 200:
        print(f"Error: {articles.status_code}")
        print(articles.text)
    else:
        search_results = articles.json()
        results = search_results["results"]
        # print(results)
        i = 0 
        for result in results:
            data = (result["title"], result["url"], result["raw_content"])
            # print(data)
            result_list.append(data)
            if (len(data[2]) >= cap):
                messages.append({
                    "role": "user",
                    "content": f"title = {data[0]}, url = {data[1]}, article = {data[2][:cap]}"
                })
            else:
                messages.append({
                    "role": "user",
                    "content": f"title = {data[0]}, url = {data[1]}, article = {data[2]}"
                })
            # print(f"nb of articles: {i}")


    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages,
        temperature=1,
        max_tokens=2049,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    data = response['choices'][0]['message']['content']
    json_data = json.loads(data)
    five_articles = get_five_articles(json_data)
    print("DONE")
    return five_articles

if (__name__ == '__main__'):
    app.run(debug=True)