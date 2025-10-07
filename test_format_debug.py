#!/usr/bin/env python3
"""
Debug script to test what format the test expects vs what we return
"""

from apputil import Genius

# Initialize Genius with your token
genius = Genius(access_token="vw58dWIGES4DS1hb7pYPdbSyEIR_klztMKLcOgK3HtH2qFCn9EESV5p7xs96IiQc")

print("🔍 Testing get_artist return format...")
print("=" * 60)

# Test the current implementation
result = genius.get_artist("Radiohead")
print("Current implementation returns:")
print(f"Type: {type(result)}")
print(f"Keys: {list(result.keys()) if isinstance(result, dict) else 'Not a dict'}")
print(f"Has 'response' key: {'response' in result if isinstance(result, dict) else False}")
print(f"Has 'name' key: {'name' in result if isinstance(result, dict) else False}")
print(f"Artist name: {result.get('name', 'Not found') if isinstance(result, dict) else 'N/A'}")

print("\n" + "=" * 60)
print("If test expects 'response' key, the test wants raw API format.")
print("If test expects direct artist data, our implementation is correct.")

# Show what raw API response would look like
print("\nRaw API response would have structure:")
print("{'meta': {...}, 'response': {'artist': {...}}}")
print("Where the artist data is nested under response.artist")