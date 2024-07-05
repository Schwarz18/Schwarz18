import requests
import json
from datetime import datetime

LEETCODE_USERNAME = 'Sudeep_hm18'

def fetch_leetcode_streak(username):
    url = f'https://leetcode-stats-api.herokuapp.com/{username}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['streak']
    else:
        return 0

def generate_svg(streak):
    svg = f"""
    <svg width="200" height="60" xmlns="http://www.w3.org/2000/svg">
        <rect width="200" height="60" fill="white" />
        <text x="10" y="35" font-size="24" fill="black">LeetCode Streak: {streak}</text>
    </svg>
    """
    with open("streak.svg", "w") as file:
        file.write(svg)

if __name__ == "__main__":
    streak = fetch_leetcode_streak(LEETCODE_USERNAME)
    generate_svg(streak)
