from flask import Flask


import json
import os
import requests
import openai
import re
from apikeys import TAVILY_APIKEY, OPENAI_APIKEY
from article_selection import get_five_articles


# from scraper import get_body_text_from_urls
os.environ["OPENAI_API_KEY"] = "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"
openai.api_key = "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"


from flask import Flask
app = Flask(__name__)

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

# @app.route('/get_articles')
# def articles():
#     # Base URL and endpoint
#     base_url = "https://api.tavily.com/"
#     endpoint = "search"

#     topic = "iSRAEL pALESTINE CONFLICT"

#     tsummary_payload = {
#         "query": f"Explain the topic '{topic}' by giving past history, and providing context on recent events.",
#         "search_depth": "basic",
#         "include_answer": True,
#         "include_raw_content": False,
#         "exclude_domains": ["wikipedia.com", "apnews.com/hub"],
#         "max_results": 10,
#         "api_key": TAVILY_APIKEY
#     }

#     article_payload = {
#         "query": f"Give news articles discussing the topic '{topic}' with a wide range of perspectives. No government websites. Do not include a media outlet domain as a source more than once",
#         "search_depth": "basic",
#         "include_answer": False,
#         "include_raw_content": True,
#         "exclude_domains": ["wikipedia.com", "apnews.com/hub"],
#         "max_results": 10,
#         "api_key": TAVILY_APIKEY
#     }

#     article_payload_json = json.dumps(article_payload)
#     tsummary_payload_json = json.dumps(tsummary_payload)

#     headers = {
#         "Content-Type": "application/json"
#     }

#     print("Getting topic summary")
#     tsummary = requests.post(f"{base_url}{endpoint}",
#                             data=tsummary_payload_json, headers=headers)

#     print("Getting articles on topic")
#     articles = requests.post(f"{base_url}{endpoint}",
#                             data=article_payload_json, headers=headers)

#     result_list = []
#     links = []
#     topic_summary = tsummary.json()["answer"].split("\nSource")[0]
    

#     messages = [{
#         "role": "system",
#         "content": "You are a professional news interpreter and political scientist. You will perform two tasks.\nWhat I will send:\n1. a query in the format \\\"search topic = [TOPIC, TOPIC SUMMARY]\\\". \n2. queries in the format \\\"title = [TITLE], url = [URL], article = [ARTICLE]\\\". [TITLE] is the title of the article, [URL] is the article's url, and [ARTICLE] contains raw texts from an article about [TOPIC].\nWhat you will do:\nUsing 1., You will generate the two main points of view (pov) on [TOPIC] based on the given description [TOPIC SUMMARY]. Then, for each [ARTICLE], you will give a descriptive summary, get the media outlet name, and rank the article on a scale of FIVE levels of opinions on [TOPIC], 1 being the first main point of view, 3 being a balanced point of view, and 5 being the second main point of view. \nSummarize all this information in a JSON format using this template with propper formatting:\n{\n  \"povs\": [\n    {\"pov_title\": \"POV1 TITLE\", \"description\": \"POV1 DESCRIPTION\"},\n    {\"pov_title\": \"POV2 TITLE\", \"description\": \"POV2 DESCRIPTION\"}\n  ],\n  \"scale\": [\n    {\"level_title\": \"LEVEL1 NUMBER AND TITLE\", \"description\": \"LEVEL1 DESCRIPTION\"},\n    {\"level_title\": \"LEVEL2 NUMBER AND TITLE\", \"description\": \"LEVEL2 DESCRIPTION\"},\n    {\"level_title\": \"LEVEL3 NUMBER AND TITLE\", \"description\": \"LEVEL3 DESCRIPTION\"},\n    {\"level_title\": \"LEVEL4 NUMBER AND TITLE\", \"description\": \"LEVEL4 DESCRIPTION\"},\n    {\"level_title\": \"LEVEL5 NUMBER AND TITLE\", \"description\": \"LEVEL5 DESCRIPTION\"}\n  ],\n  \"articles\": [\n    {\"title\": \"ARTICLE TITLE\", \"url\": \"ARTICLE URL\", \"media\": \"MEDIA NAME\", \"summary\": \"ARTICLE SUMMARY\", \"level\": \"SCALE LEVEL NUMBER\"},\n    // ... (for each article)\n  ]\n}"
#         },
#         {
#         "role": "user",
#         "content": f"search topic = {topic}, {topic_summary}"
#     }]
#     cap = 2650
#     if articles.status_code != 200:
#         print(f"Error: {articles.status_code}")
#         print(articles.text)
#     else:
#         search_results = articles.json()
#         results = search_results["results"]
#         # print(results)
#         i = 0 
#         for result in results:
#             data = (result["title"], result["url"], result["raw_content"])
#             # print(data)
#             result_list.append(data)
#             if (len(data[2]) >= cap):
#                 messages.append({
#                     "role": "user",
#                     "content": f"title = {data[0]}, url = {data[1]}, article = {data[2][:cap]}"
#                 })
#             else:
#                 messages.append({
#                     "role": "user",
#                     "content": f"title = {data[0]}, url = {data[1]}, article = {data[2]}"
#                 })
#             # print(f"nb of articles: {i}")

#     print("startGPT")
#     response = openai.ChatCompletion.create(
#         model="gpt-4",
#         messages=messages,
#         temperature=1,
#         max_tokens=2049,
#         top_p=1,
#         frequency_penalty=0,
#         presence_penalty=0
#     )
#     print("got response")
#     data = response['choices'][0]['message']['content']
#     json_data = json.loads(data)
#     data = json_data
#     print("DONE")

#     i = 0
#     medias = []
#     levels = []
#     selected = []
#     #preliminary selection of unique (media, level) pairs
#     for article in data["articles"]:
#         media = article["media"]
#         match = re.search(r'\d+', article["level"])
#         if match:
#           article["level"] = match.group()
#         level = int(article["level"])
#         # level = int(article["level"])
#         if media not in medias or level not in levels:
#             print(f"Just included: {media}: {media in medias}, {level}: {level in levels}")
#             selected.append(article)
#             levels.append(level) 
#             medias.append(media)
#         else:
#             print(f"Already included: {media}: {media in medias}, {level}: {level in levels}")

#     five_selections1 = []
#     selected_medias1 = []
#     # five_selections2 = []
#     # selected_medias2 = []
#     #for each level, include first article pair, none if nothing; no duplicate medias
#     for i in range(1,6):
#         # print(levels)
#         if i in levels:
#             position = levels.index(i)
#             while (medias[position] in selected_medias1 and (position != len(levels)-1 and i in levels[position+1:])):
#                 position = levels[position+1:].index(i)
            
#             # if (position == len(levels)-1 or i not in levels[position+1:]):
#             #     five_selections1.append(None)
#             #     print(f"{i} not levels")
#             # else:
#             five_selections1.append(selected[position])
#             selected_medias1.append(selected[position]['media'])
#             print(f"Included media {selected[position]['media']} for level {selected[position]['level']}")

#         else:
#             five_selections1.append({"title": "None", "url": "", "media": "None", "summary": "", "level": "3"})
#             print(f"{i} not levels")

#     # for i in range(5, 0, -1):
#     #     if i in levels:
#     #         position = levels.index(i)
#     #         while (
#     #             selected[position]["media"] in selected_medias2
#     #             and (position != len(levels) - 1 and i in levels[position + 1 :])
#     #         ):
#     #             position = levels[position + 1 :].index(i)

#     #         five_selections2.append(selected[position])
#     #         selected_medias2.append(selected[position]["media"])
#     #         print(f"Included media {selected[position]['media']} for level {selected[position]['level']}")
#     #     else:
#     #         five_selections2.append(None)
#     #         print(f"{i} not in levels")

#     # print(selected_medias1)
#     # print(selected_medias2)

#     # if (len(list(set(selected_medias1))) >= len(list(set(selected_medias2)))):
        
#     return five_selections1


    # return five_articles

if (__name__ == '__main__'):
    app.run(debug=True)
# print(articles())