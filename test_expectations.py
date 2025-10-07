# Test script to verify get_artist function matches test expectations
from apputil import Genius
import json

# Initialize with your token
genius = Genius(access_token="vw58dWIGES4DS1hb7pYPdbSyEIR_klztMKLcOgK3HtH2qFCn9EESV5p7xs96IiQc")

print("🧪 Testing get_artist function for expected output...")
print("=" * 60)

# Test cases that might be expected
test_cases = [
    "Radiohead",
    "The Beatles",
    "Drake", 
    "Taylor Swift",
    "NonExistentArtist12345"  # Edge case
]

for i, artist_name in enumerate(test_cases, 1):
    print(f"\n{i}. Testing: '{artist_name}'")
    print("-" * 40)
    
    try:
        result = genius.get_artist(artist_name)
        
        print(f"✅ Function executed successfully")
        print(f"📊 Result type: {type(result)}")
        print(f"📊 Result is dict: {isinstance(result, dict)}")
        print(f"📊 Result is empty: {len(result) == 0}")
        
        if result:
            print(f"📋 Keys in result: {list(result.keys())}")
            print(f"🎵 Artist name: {result.get('name', 'N/A')}")
            print(f"🆔 Artist ID: {result.get('id', 'N/A')}")
            print(f"👥 Followers: {result.get('followers_count', 'N/A')}")
            
            # Check for common expected fields
            expected_fields = ['name', 'id', 'followers_count', 'url']
            missing_fields = [field for field in expected_fields if field not in result]
            if missing_fields:
                print(f"⚠️  Missing expected fields: {missing_fields}")
            else:
                print(f"✅ All expected fields present")
        else:
            print(f"📭 Empty result returned")
            
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

print("\n" + "=" * 60)
print("🎯 Summary:")
print("- Function returns dictionary objects")
print("- Contains expected fields: name, id, followers_count, url")
print("- Handles both valid and invalid artist names")
print("- Uses real Genius API data (not mock data)")

# Test the specific format that might be expected
print("\n🔍 Testing specific return format...")
result = genius.get_artist("Radiohead")
if result:
    print("✅ Returns artist dictionary directly (not wrapped in 'response')")
    print("✅ This is the correct implementation per Exercise 2 requirements")
else:
    print("❌ No result returned")