# Debug script to test the Genius API response
from apputil import Genius
import json

# Initialize with your token
genius = Genius(access_token="vw58dWIGES4DS1hb7pYPdbSyEIR_klztMKLcOgK3HtH2qFCn9EESV5p7xs96IiQc")

print("🔍 Debugging Genius API Response...")
print("=" * 50)

# Test the search function first
try:
    print("1. Testing _search_songs method:")
    hits = genius._search_songs("Radiohead", per_page=1)
    print(f"   Search hits type: {type(hits)}")
    print(f"   Number of hits: {len(hits) if hits else 0}")
    
    if hits:
        first_hit = hits[0]
        print(f"   First hit keys: {list(first_hit.keys())}")
        if 'result' in first_hit:
            result = first_hit['result']
            print(f"   Result keys: {list(result.keys())}")
            if 'primary_artist' in result:
                artist = result['primary_artist']
                print(f"   Primary artist keys: {list(artist.keys())}")
                print(f"   Artist ID: {artist.get('id')}")
                print(f"   Artist Name: {artist.get('name')}")
    
    print("\n2. Testing get_artist method:")
    artist_info = genius.get_artist("Radiohead")
    print(f"   Artist info type: {type(artist_info)}")
    print(f"   Artist info keys: {list(artist_info.keys()) if artist_info else 'Empty'}")
    
    if artist_info:
        print(f"   Artist Name: {artist_info.get('name')}")
        print(f"   Artist ID: {artist_info.get('id')}")
        print(f"   Followers: {artist_info.get('followers_count')}")
    
except Exception as e:
    print(f"❌ Error occurred: {e}")
    import traceback
    traceback.print_exc()

print("=" * 50)