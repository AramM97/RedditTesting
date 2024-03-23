import praw

# Authenticate with Reddit API
reddit = praw.Reddit(

)

# Assuming you have the URL of the post where you want to comment
post_url = 'https://www.reddit.com/r/QAutomation/comments/1biuyuz/test_collections_post_1/'

# Fetching the submission object using the URL
submission = reddit.submission(url=post_url)

# Add your comment
comment_text = "comment posting test ."

# Post the comment
submission.reply(comment_text)

print("Comment posted successfully!")
