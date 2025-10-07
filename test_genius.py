# Quick test of your Genius API implementation
from apputil import Genius

# Initialize with your token
genius = Genius(access_token="vw58dWIGES4DS1hb7pYPdbSyEIR_klztMKLcOgK3HtH2qFCn9EESV5p7xs96IiQc")

print("🚀 Testing your Genius API implementation...")
print("=" * 50)

# Test Exercise 2
print("🎵 Exercise 2: get_artist() method")
result = genius.get_artist("Adele")
print(f"Artist: {result.get('name')}")
print(f"ID: {result.get('id')}")
print(f"Followers: {result.get('followers_count')}")
print()

# Test Exercise 3
print("📊 Exercise 3: get_artists() method")
df = genius.get_artists(["Drake", "Taylor Swift"])
print(df)
print(f"\nDataFrame shape: {df.shape}")
print("=" * 50)
print("✅ All tests completed!")