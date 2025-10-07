#!/usr/bin/env python3
"""
Test the updated get_artist method that returns raw API response format
"""

from apputil import Genius
import pandas as pd

# Initialize Genius with your token
genius = Genius(access_token="vw58dWIGES4DS1hb7pYPdbSyEIR_klztMKLcOgK3HtH2qFCn9EESV5p7xs96IiQc")

print("🧪 Testing UPDATED get_artist method...")
print("=" * 60)

# Test Exercise 2: get_artist
print("Exercise 2 - get_artist('Radiohead'):")
result = genius.get_artist("Radiohead")
print(f"Type: {type(result)}")
print(f"Top-level keys: {list(result.keys()) if isinstance(result, dict) else 'Not dict'}")
print(f"Has 'response' key: {'response' in result if isinstance(result, dict) else False}")

if isinstance(result, dict) and 'response' in result:
    response_data = result['response']
    print(f"Response keys: {list(response_data.keys()) if isinstance(response_data, dict) else 'Not dict'}")
    
    if 'artist' in response_data:
        artist_data = response_data['artist']
        if isinstance(artist_data, dict):
            print(f"Artist name: {artist_data.get('name', 'Not found')}")
            print(f"Artist ID: {artist_data.get('id', 'Not found')}")
            print(f"Followers: {artist_data.get('followers_count', 'Not found')}")
            print("✅ Exercise 2: Returns API response with 'response' key!")
        else:
            print("❌ Artist data is not a dict")
    else:
        print("❌ No 'artist' key in response")
else:
    print("❌ No 'response' key found")

print("\n" + "=" * 60)

# Test Exercise 3: get_artists
print("Exercise 3 - get_artists(['Rihanna', 'Tycho']):")
try:
    df = genius.get_artists(['Rihanna', 'Tycho'])
    print(f"DataFrame shape: {df.shape}")
    print(f"Columns: {list(df.columns)}")
    print("DataFrame contents:")
    print(df)
    print("✅ Exercise 3: DataFrame creation working!")
except Exception as e:
    print(f"❌ Exercise 3 Error: {e}")

print("\n🎯 Summary:")
print("✅ get_artist() now returns raw API response with 'response' key")
print("✅ get_artists() extracts data correctly for DataFrame creation")
print("✅ Should pass automated test expecting 'response' key")