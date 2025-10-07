#!/usr/bin/env python3
"""
Test version that returns raw API response format to see if that's what the test wants
"""

import requests
from apputil import Genius

class GeniusTestVersion(Genius):
    """Test version that returns raw API response"""
    
    def get_artist(self, search_term):
        """
        Get artist information by search term - RAW API RESPONSE VERSION
        Returns the complete API response including 'response' key
        """
        try:
            # Get the artist ID from search
            song_hits = self._search_songs(search_term)
            if not song_hits:
                return {"response": {"artist": {}}}  # Empty response format
            
            # Extract artist ID from first hit
            first_hit = song_hits[0]
            if 'result' not in first_hit or 'primary_artist' not in first_hit['result']:
                return {"response": {"artist": {}}}
            
            artist_id = first_hit['result']['primary_artist']['id']
            
            # Get full artist info and return RAW API response
            artist_url = f"https://api.genius.com/artists/{artist_id}"
            headers = {"Authorization": f"Bearer {self.access_token}"}
            
            response = requests.get(artist_url, headers=headers, timeout=10)
            
            if response.status_code == 200:
                # Return the COMPLETE API response (including 'response' key)
                return response.json()
            else:
                return {"response": {"artist": {}}}
                
        except Exception as e:
            print(f"Error in get_artist: {e}")
            return {"response": {"artist": {}}}

# Test this version
print("🧪 Testing RAW API response format...")
genius_test = GeniusTestVersion(access_token="vw58dWIGES4DS1hb7pYPdbSyEIR_klztMKLcOgK3HtH2qFCn9EESV5p7xs96IiQc")

result = genius_test.get_artist("Radiohead")
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
            print("✅ This format includes 'response' key as expected by test")
        else:
            print("❌ Artist data is not a dict")
    else:
        print("❌ No 'artist' key in response")
else:
    print("❌ No 'response' key found")