import requests

BASE_URL = "http://jsonplaceholder.typicode.com"

def get_users():
    response = requests.get(f"{BASE_URL}/users")
    return response.json()

def get_todos():
    response = requests.get(f"{BASE_URL}/todos")
    return response.json()

def get_posts():
    response = requests.get(f"{BASE_URL}/posts")
    return response.json()

def get_comments():
    response = requests.get(f"{BASE_URL}/comments")
    return response.json()

def get_albums():
    response = requests.get(f"{BASE_URL}/albums")
    return response.json()

def get_photos():
    response = requests.get(f"{BASE_URL}/photos")
    return response.json()

