from googleapiclient.discovery import build 
from flask_cors import CORS, cross_origin
from flask import request, jsonify
import pandas as pd
import numpy as np
import operator
import flask
import re

app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config['CORS_HEADERS'] = 'Content-Type'

cors = CORS(app, resources={r"/tags/api/videos": {"origins": "http://localhost:port"}})
   
DEVELOPER_KEY = "AIzaSyAgIIprwuI3TbBBpPW1AB_sdo-CVq5FkVQ" 
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
   
youtube_object = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, 
                                        developerKey = DEVELOPER_KEY) 

@app.route('/', methods=['GET'])
def home():
    return '''<h1>SlashTags</h1>
    <p>An API for retriving videos from a keyword search, and extracting tags.</p>'''
   
# returns a dataframe of video information from a search query
@app.route('/tags/api/videos', methods=['GET'])
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def youtube_search_keyword():
    
    if 'query' in request.args:
        query = str(request.args['query']) 
        max_results = 25

        search_request = youtube_object.search().list(
        q=query,
        part='id,snippet',
        maxResults=max_results).execute()

        videosDf = pd.DataFrame(columns = ['videoId', 'thumbnail', 'description', 'descriptionTags', 'tags', 'viewCount', 'likeCount', 'dislikeCount'])

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

        return videosDf.to_json(orient = "records")
    else:
        return "Error: No query field provided. Please specify a query."

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

app.run()