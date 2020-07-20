from apiclient.discovery import build 
import pandas as pd
import numpy as np
import operator
import re
   
DEVELOPER_KEY = "" 
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
   
youtube_object = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, 
                                        developerKey = DEVELOPER_KEY) 
   
# returns a dataframe of video information from a search query
def youtube_search_keyword(query, max_results):    
    search_request = youtube_object.search().list(
    q=query,
    part='id,snippet',
    maxResults=max_results).execute()

    videosDf = pd.DataFrame(columns = ['videoId', 'description', 'descriptionTags', 'tags', 'viewCount', 'likeCount', 'dislikeCount'])

    for search_result in search_request.get('items', []):
        if search_result['id']['kind'] == 'youtube#video':
            videosDf = videosDf.append({'videoId' : search_result['id']['videoId']}, ignore_index=True)

    for (_ , row) in videosDf.iterrows():
        video_request = youtube_object.videos().list(
        part="snippet,statistics",
        id= row['videoId'])

        response = video_request.execute()

        videosDf.loc[videosDf.videoId == row['videoId'], ['description', 'tags', 'viewCount', 'likeCount', 'dislikeCount']] = \
                                                                              response['items'][0]['snippet']['description'], \
                                                                                     response['items'][0]['snippet']['tags'], \
                                                                             response['items'][0]['statistics']['viewCount'], \
                                                                             response['items'][0]['statistics']['likeCount'], \
                                                                          response['items'][0]['statistics']['dislikeCount']  

    return videosDf

# populates description tags from video descriptions
def extract_desc_tags(df):
    for (_ , row) in df.iterrows():
        tempDesc = re.findall(r"#(\w+)", row['description'])
        testStr = ', '.join(tempDesc)
        df.loc[df.description == row['description'], 'descriptionTags'] = testStr

    return df

# returns a dictionary of tags and their frequency
def desc_tags_freq(df):
    tagDict = {}
    for (_ , row) in df.iterrows():
        for match in re.findall(r"[^,\s][^\,]*[^,\s]*", row['descriptionTags']):
            if match:
                if match.lower() not in tagDict:
                    tagDict[match] = 1
                else:
                    tagDict[match.lower()] += 1

    return sorted(tagDict.items(), reverse = True, key=operator.itemgetter(1))

# test run
print(desc_tags_freq(extract_desc_tags(youtube_search_keyword('valorant', 50))))