"""Fetch YouTube video transcript and metadata via DataForSEO API.

Usage: python fetch_youtube_transcript.py <video_url_or_id> [output_file]

Outputs transcript and metadata to stdout and optionally to a markdown file.
"""
import os, sys, json, requests
from dotenv import load_dotenv

scripts_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(scripts_dir, ".env"))

DATAFORSEO_API_KEY = os.getenv("DATAFORSEO_API_KEY")

def extract_video_id(url_or_id):
    if "youtube.com" in url_or_id:
        if "v=" in url_or_id:
            return url_or_id.split("v=")[1].split("&")[0]
    if "youtu.be/" in url_or_id:
        return url_or_id.split("youtu.be/")[1].split("?")[0]
    return url_or_id

def get_transcript(video_id):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Basic {DATAFORSEO_API_KEY}'
    }
    post_data = dict(language_code="en", location_code=2840, video_id=video_id)
    resp = requests.post(
        "https://api.dataforseo.com/v3/serp/youtube/video_subtitles/live/advanced",
        data=json.dumps([post_data]),
        headers=headers
    )
    return resp.json()

def get_metadata(video_id):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Basic {DATAFORSEO_API_KEY}'
    }
    post_data = dict(language_code="en", location_code=2840, video_id=video_id)
    resp = requests.post(
        "https://api.dataforseo.com/v3/serp/youtube/video_info/live/advanced",
        data=json.dumps([post_data]),
        headers=headers
    )
    data = resp.json()
    try:
        return data['tasks'][0]['result'][0]['items'][0]
    except (KeyError, IndexError, TypeError):
        return data

def format_transcript(subtitles_data):
    try:
        items = subtitles_data['tasks'][0]['result'][0]['items']
    except (KeyError, IndexError, TypeError):
        return "No subtitles found."
    lines = []
    for item in items:
        start = round(item.get('start_time', 0))
        mins, secs = divmod(start, 60)
        text = item.get('text', '').strip()
        if text:
            lines.append(f"[{mins}:{secs:02d}] {text}")
    return "\n".join(lines)

def main():
    if len(sys.argv) < 2:
        print("Usage: python fetch_youtube_transcript.py <video_url_or_id> [output_file]")
        sys.exit(1)
    if not DATAFORSEO_API_KEY:
        print("Error: DATAFORSEO_API_KEY not found. Set it in scripts/ env file.")
        sys.exit(1)

    video_id = extract_video_id(sys.argv[1])
    output_file = sys.argv[2] if len(sys.argv) > 2 else None

    print(f"Fetching metadata for {video_id}...")
    metadata = get_metadata(video_id)
    title = metadata.get('title', 'Unknown')
    channel = metadata.get('channel_name', 'Unknown')
    description = metadata.get('description', '')
    views = metadata.get('views_count', 'N/A')
    timestamp = metadata.get('timestamp', 'N/A')
    print(f"Title: {title}")
    print(f"Channel: {channel}")
    print(f"Views: {views}")
    print(f"Published: {timestamp}")

    print(f"\nFetching subtitles...")
    subtitles = get_transcript(video_id)
    transcript = format_transcript(subtitles)
    print(f"\nTranscript ({len(transcript)} chars):\n")
    print(transcript[:3000])
    if len(transcript) > 3000:
        print(f"\n... [{len(transcript) - 3000} more chars]")

    if output_file:
        with open(output_file, 'w') as f:
            f.write(f"# {title}\n\n")
            f.write(f"**Channel:** {channel}  \n")
            f.write(f"**Views:** {views}  \n")
            f.write(f"**Published:** {timestamp}  \n")
            f.write(f"**URL:** https://www.youtube.com/watch?v={video_id}\n\n")
            if description:
                f.write(f"## Description\n\n{description}\n\n")
            f.write(f"## Transcript\n\n{transcript}\n")
        print(f"\nSaved to {output_file}")

if __name__ == '__main__':
    main()
