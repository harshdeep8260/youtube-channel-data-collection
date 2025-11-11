import os
import pandas
from dotenv import load_dotenv
from googleapiclient.discovery import build

load_dotenv()

channel_id = input("Enter channel ID: ")
api_key = api_key = os.getenv("API_KEY")

youtube = build("youtube", "v3", developerKey = api_key)

request = youtube.channels().list(
    id = channel_id,
    part = "contentDetails"
)

response = request.execute()
uploads_playlist_id = response["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]

video_ids = []
next_page_token = None

while True:
    request = youtube.playlistItems().list(
        maxResults = 50,
        part = "snippet",
        pageToken = next_page_token,
        playlistId = uploads_playlist_id
    )

    response = request.execute()

    for item in response["items"]:
        video_ids.append(item["snippet"]["resourceId"]["videoId"])

    next_page_token = response.get("nextPageToken")

    if not next_page_token:
        break

details = []

for i in range(0, len(video_ids), 50):
    batch = video_ids[i:i+50]
    ids_string = ','.join(batch)

    request = youtube.videos().list(
        id = ids_string,
        part = "snippet,statistics,contentDetails"
    )

    response = request.execute()

    for item in response["items"]:
        video_info = {
            "title": item["snippet"]["title"],
            "upload_date": item["snippet"]["publishedAt"],
            "description": item["snippet"]["description"],
            "channel_name": item["snippet"]["channelTitle"],
            "thumbnail_url": item["snippet"]["thumbnails"]["default"]["url"],

            "likes": item["statistics"].get("likeCount", None),
            "views": item["statistics"].get("viewCount", None),
            "comments": item["statistics"].get("commentCount", None),

            "duration": item["contentDetails"]["duration"]
        }

        details.append(video_info)

df = pandas.DataFrame(details)
df.to_parquet("data.parquet", engine = "pyarrow")
