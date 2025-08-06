import pandas as pd
import json

def load_data(uploaded_file):
    # Read the uploaded JSON content
    raw_data = uploaded_file.read().decode("utf-8")
    data = json.loads(raw_data)

    # Convert to DataFrame
    df = pd.DataFrame(data)

    # Filter only watched videos (skip likes, searches etc.)
    df = df[df['title'].str.startswith("Watched")]

    # Extract video title
    df['video_title'] = df['title'].str.replace("Watched ", "", regex=False)

    # Extract channel name if available
    df['channel'] = df['subtitles'].apply(lambda x: x[0]['name'] if isinstance(x, list) else None)

    # Parse datetime using flexible ISO 8601 support
    df['time'] = pd.to_datetime(df['time'], format='mixed', utc=True)

    # Extract additional time features
    df['year'] = df['time'].dt.year
    df['month'] = df['time'].dt.month_name()
    df['day'] = df['time'].dt.day
    df['hour'] = df['time'].dt.hour
    df['weekday'] = df['time'].dt.day_name()

    return df
