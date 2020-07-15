from apiclient.discovery import build 
import operator
import re
   
DEVELOPER_KEY = "AIzaSyAgIIprwuI3TbBBpPW1AB_sdo-CVq5FkVQ" 
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
   
youtube_object = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, 
                                        developerKey = DEVELOPER_KEY) 
   
# returns list of video descriptions from youtube search request
def youtube_search_keyword(query, max_results):    
    search_request = youtube_object.search().list(
    q=query,
    part='id,snippet',
    maxResults=max_results).execute()

    videos = []
    descriptions = []

    for search_result in search_request.get('items', []):
        if search_result['id']['kind'] == 'youtube#video':
            videos.append(search_result['id']['videoId'])

    for video in videos:
        video_request = youtube_object.videos().list(
            part="snippet,contentDetails,statistics",
            id= video)
    
        response = video_request.execute()
        descriptions.append(response['items'][0]['snippet']['description'])

    return descriptions

# returns list of tags found in video descriptions
def extract_desc_tags(descriptions):
    hashtags = []
    for desc in descriptions:
        hashtags.append(re.findall(r"#(\w+)", desc))

    return hashtags

# returns a dictionary of tags and their frequency
def desc_tags_freq(tags):
    tagDict = {}

    for tag in tags:
        if tag:
            for x in range (0,len(tag)):
                if tag[x].lower() not in tagDict:
                    tagDict[tag[x]] = 1
                else:
                    tagDict[tag[x].lower()] += 1

    return sorted(tagDict.items(), reverse = True, key=operator.itemgetter(1))

print(desc_tags_freq(extract_desc_tags(youtube_search_keyword('valorant', 100))))