import json
from apikeys.txt import APIKEY
from tavily import Client
tavily = Client(api_key=APIKEY)

# For advanced search:
results = tavily.search(query="Should I invest in Apple in 2024?", search_depth="advanced", max_results = 20)




# Parse the JSON data
parsed_data = json.loads(data)

# Now you can access the elements in the JSON data as Python dictionaries
print("Query:", parsed_data["query"])
print("Response Time:", parsed_data["response_time"])
print("Answer:", parsed_data["answer"])
print("Follow-up Questions:", parsed_data["follow_up_questions"])

# Accessing the results
results = parsed_data["results"]
for result in results:
    print("Result Content:", result["content"])
    print("Result URL:", result["url"])
    print("Result Score:", result["score"])
    print("Result Raw Content:", result["raw_content"])
