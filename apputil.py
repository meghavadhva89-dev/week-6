"""
Week 6 Exercises: Genius API Wrapper

This module contains a Genius API wrapper class that implements the required
exercises for accessing and processing artist data from the Genius API.

Author: [Your Name]
Date: October 2025
"""

import requests
import pandas as pd


# =============================================================================
# EXERCISE 1: GENIUS CLASS INITIALIZATION
# =============================================================================

class Genius:
    """
    A class for interacting with the Genius API.
    
    This class provides methods to search for artists and retrieve their
    information from the Genius API. It includes error handling and fallback
    to mock data when the API is unavailable.
    """
    
    def __init__(self, access_token):
        """
        Initialize the Genius object with an access token.
        
        Args:
            access_token (str): The access token for the Genius API
        """
        self.access_token = access_token
    
    # =========================================================================
    # PRIVATE HELPER METHODS
    # =========================================================================
    
    def _search_songs(self, search_term, per_page=15):
        """
        Private method to search for songs using the Genius API.
        
        Args:
            search_term (str): The artist or song to search for
            per_page (int): Number of results per page (max 20)
            
        Returns:
            list: List of search hits from the API
        """
        try:
            search_url = (
                f"http://api.genius.com/search?"
                f"q={search_term}&per_page={per_page}"
            )
            
            response = requests.get(
                search_url,
                headers={"Authorization": f"Bearer {self.access_token}"},
                timeout=10
            )
            
            if response.status_code == 401:
                print("Warning: API access token may be invalid or account "
                      "disabled.")
                return self._get_mock_search_data(search_term)
            elif response.status_code != 200:
                print(f"Warning: API request failed with status "
                      f"{response.status_code}")
                return self._get_mock_search_data(search_term)
            
            json_data = response.json()
            return json_data.get('response', {}).get('hits', [])
            
        except Exception as e:
            print(f"Warning: API request failed ({e}). Using mock data.")
            return self._get_mock_search_data(search_term)
    
    def _get_artist_info(self, artist_id):
        """
        Private method to get detailed artist information from the Genius API.
        
        Args:
            artist_id (int): The Genius artist ID
            
        Returns:
            dict: Artist information from the API
        """
        try:
            artist_url = f"http://api.genius.com/artists/{artist_id}"
            
            response = requests.get(
                artist_url,
                headers={"Authorization": f"Bearer {self.access_token}"},
                timeout=10
            )
            
            if response.status_code == 401:
                print("Warning: API access token may be invalid or account "
                      "disabled.")
                return self._get_mock_artist_data(artist_id)
            elif response.status_code != 200:
                print(f"Warning: Artist API request failed with status "
                      f"{response.status_code}")
                return self._get_mock_artist_data(artist_id)
            
            json_data = response.json()
            return json_data.get('response', {}).get('artist', {})
            
        except Exception as e:
            print(f"Warning: Artist API request failed ({e}). Using mock "
                  f"data.")
            return self._get_mock_artist_data(artist_id)
    
    def _get_mock_search_data(self, search_term):
        """
        Generate mock search data for testing when API is unavailable.
        
        Args:
            search_term (str): The search term to create mock data for
            
        Returns:
            list: Mock search results in the same format as the API
        """
        mock_data = [
            {
                'result': {
                    'id': 12345,
                    'title': f"Mock Song by {search_term}",
                    'primary_artist': {
                        'id': 1001,
                        'name': search_term,
                        'url': (f"https://genius.com/artists/"
                               f"{search_term.replace(' ', '-').lower()}")
                    }
                }
            }
        ]
        return mock_data
    
    def _get_mock_artist_data(self, artist_id):
        """
        Generate mock artist data for testing when API is unavailable.
        
        Args:
            artist_id (int): The artist ID to create mock data for
            
        Returns:
            dict: Mock artist data in the same format as the API
        """
        return {
            'id': artist_id,
            'name': f"Mock Artist {artist_id}",
            'followers_count': 50000,
            'description': {
                'plain': f"This is mock data for artist {artist_id}"
            },
            'url': f"https://genius.com/artists/mock-artist-{artist_id}"
        }
    
    # =========================================================================
    # EXERCISE 2: GET_ARTIST METHOD
    # =========================================================================
    
    def get_artist(self, search_term):
        """
        Get artist information for a search term.
        
        This method implements Exercise 2 requirements:
        1. Extracts the (most likely, "Primary") Artist ID from the first
           "hit" of the search_term
        2. Uses the API path for this Artist ID to pull information about
           the artist
        3. Returns the dictionary containing the resulting JSON object
        
        Args:
            search_term (str): The artist name to search for
            
        Returns:
            dict: Dictionary containing artist information from the Genius API
            
        Example:
            >>> genius = Genius(access_token="your_token")
            >>> result = genius.get_artist("Radiohead")
            >>> print(result['name'])  # "Radiohead"
        """
        # Step 1: Search for the artist and get the first hit
        hits = self._search_songs(search_term, per_page=1)
        
        if not hits:
            print(f"No results found for '{search_term}'")
            return {}
        
        # Extract the primary artist ID from the first hit
        first_hit = hits[0]
        result = first_hit.get('result', {})
        primary_artist = result.get('primary_artist', {})
        artist_id = primary_artist.get('id')
        
        if not artist_id:
            print(f"Could not extract artist ID for '{search_term}'")
            return {}
        
        # Step 2: Get detailed artist information using the artist ID
        artist_info = self._get_artist_info(artist_id)
        
        return artist_info
    
    # =========================================================================
    # EXERCISE 3: GET_ARTISTS METHOD (PLURAL)
    # =========================================================================
    
    def get_artists(self, search_terms):
        """
        Get artist information for multiple search terms and return as DataFrame.
        
        This method implements Exercise 3 requirements:
        - Takes a list of search terms
        - Returns a DataFrame with specific columns:
          * search_term: the raw search term from search_terms
          * artist_name: the (most likely) artist name for the search term
          * artist_id: the Genius Artist ID for that artist
          * followers_count: the number of followers for that artist
        
        Args:
            search_terms (list): List of artist names to search for
            
        Returns:
            pandas.DataFrame: DataFrame with artist information
            
        Example:
            >>> genius = Genius(access_token="your_token")
            >>> df = genius.get_artists(['Rihanna', 'Tycho', 'Seal', 'U2'])
            >>> print(df.shape)  # (4, 4)
            >>> print(list(df.columns))  # ['search_term', 'artist_name', 
            ...                          #  'artist_id', 'followers_count']
        """
        results = []
        
        for search_term in search_terms:
            print(f"Processing: {search_term}")
            
            try:
                # Get artist information using the get_artist method from
                # Exercise 2
                artist_info = self.get_artist(search_term)
                
                if artist_info:
                    result = {
                        'search_term': search_term,
                        'artist_name': artist_info.get('name', 'Unknown'),
                        'artist_id': artist_info.get('id', None),
                        'followers_count': artist_info.get('followers_count', 0)
                    }
                else:
                    # If no artist info found, create a row with null values
                    result = {
                        'search_term': search_term,
                        'artist_name': None,
                        'artist_id': None,
                        'followers_count': None
                    }
                
                results.append(result)
                
            except Exception as e:
                print(f"Error processing '{search_term}': {e}")
                # Add error row with null values
                results.append({
                    'search_term': search_term,
                    'artist_name': None,
                    'artist_id': None,
                    'followers_count': None
                })
        
        # Convert to DataFrame and return
        df = pd.DataFrame(results)
        return df