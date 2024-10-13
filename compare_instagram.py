from bs4 import BeautifulSoup

# Function to parse Instagram usernames from the HTML file
def parse_usernames(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'lxml')
        # Find all 'a' tags since usernames are in anchor tags in Instagram HTML exports
        usernames = [a.text for a in soup.find_all('a')]
        return set(usernames)

# Load followers and following from their respective HTML files
followers = parse_usernames('followers.html')
following = parse_usernames('following.html')

# Find users who don't follow back
not_following_back = following - followers

# Find users you don't follow back
not_followed_back = followers - following

# Print results
print(f"Users not following you back ({len(not_following_back)}):")
for user in not_following_back:
    print(user)

print(f"\nUsers you don't follow back ({len(not_followed_back)}):")
for user in not_followed_back:
    print(user)
