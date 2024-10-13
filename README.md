# Instagram Followers vs Following Comparison Script

This Python script allows you to compare your Instagram followers and the people you are following. It parses two HTML files (`followers.html` and `following.html`) that Instagram exports and then checks:
- Users you are following but who are not following you back.
- Users following you, but you are not following them back.

## Features

- Parses Instagram HTML exports (`followers.html` and `following.html`).
- Compares your followers and following lists.
- Displays:
  - Users you follow who don't follow you back.
  - Users who follow you but you don't follow back.

## Requirements

- Python 3.x
- `beautifulsoup4` and `lxml` libraries

You can install the required libraries using pip:

```bash
pip install beautifulsoup4 lxml
```

## How to Use

1. **Export your Instagram data:**
   - Download your Instagram followers and following list in HTML format.
     - Go to your Instagram profile on the web.
     - Click on "Settings" > "Privacy and Security" > "Data Download."
     - Select **HTML** as the format and download the data.
     - Once you have the data, locate the `followers.html` and `following.html` files.

2. **Clone this repository:**

   ```bash
   git clone https://github.com/yourusername/instagram-followers-following-compare.git
   cd instagram-followers-following-compare
   ```

3. **Place the HTML files:**
   - Place the `followers.html` and `following.html` files in the same directory as the script.

4. **Run the script:**

   ```bash
   python compare_instagram.py
   ```

5. **See the result:**
   - The script will output:
     - Users you follow who don’t follow you back.
     - Users who follow you, but you don’t follow them back.

## Example Output

```
Users not following you back (3):
- user1
- user2
- user3

Users you don't follow back (2):
- user4
- user5
```

## Contributing

Feel free to submit issues or pull requests if you have any ideas for improving the script.
