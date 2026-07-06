import requests

# Step 1: API URL
url = "https://zenquotes.io/api/random"

# Step 2: Send request to API
response = requests.get(url)

# Step 3: Convert response into Python format (JSON → list/dict)
data = response.json()

# Step 4: Extract quote and author
quote = data[0]["q"]
author = data[0]["a"]

# Step 5: Print result in nice format
print("💡 Motivational Quote")
print("---------------------")
print("Quote:", quote)
print("Author:", author)
