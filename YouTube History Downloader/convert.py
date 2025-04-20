import json

# Load the JSON data from the file with specified encoding
with open('watch-history.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

urls = []

# Extract the URLs from the JSON data
for item in data:
    if 'titleUrl' in item:
        urls.append(item['titleUrl'])
#    if 'subtitles' in item:
#        for subtitle in item['subtitles']:
#            if 'url' in subtitle:
#                urls.append(subtitle['url'])

# reverse it
#urls = reversed(urls)

# Save the URLs to a text file
with open('urls.txt', 'w') as file:
    for url in urls:
        file.write(url + '\n')
