# SlashTags
Use SlashTags to chose the tags for your next video, or just stare at the stats and press some buttons.

![](https://github.com/huhmit/slashtags/blob/master/app/src/assets/ludtags.gif)

## Overview
SlashTags was created as an experiment to gauge the importance of description hashtags, which some YouTube SEO tools ignore. SlashTags currently ranks tags based on the density of a tag in the sample taken, however other methods such as autocomplete or sampling recommended videos are being considered.

Built with Vuetify to make it look nice!

<img src="https://github.com/CharltonC98/slash-tags/blob/master/app/src/assets/slash_logo_outerglow.png" width="40%">

## Prerequisites
A Google API key with access to the YouTube Data API service is required. 

You will also need to install the following:

* Python 3 [[^](https://www.python.org/)]
* Node.js [[^](https://nodejs.org/en/)]
* Goggle API Client [[^](https://github.com/googleapis/google-api-python-client)]
* Flask [[^](https://flask.palletsprojects.com/en/1.1.x/quickstart/)]
* Pandas [[^](https://pypi.org/project/pandas/)]

## Usage
The api 'Tags.py' needs to be running alongside the app, cd to the api directory and run:

```
python tags.py
```

Navigate to the 'app' directory and run:

```
npm install
```
then
```
npm run serve
```

## Contact
Cameron Charlton - CharltonC98@gmail.com
