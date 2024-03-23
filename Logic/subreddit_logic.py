import praw

class SubReddit():

    URL = "'https://www.reddit.com/r/QAutomation/comments/1biuyuz/test_collections_post_1/'"

    def __init__(self, reddit):
        self.reddit = reddit

    def post_comment(self,post_url,comment):
        post_url = post_url
        # Fetching the submission object using the URL
        submission = self.reddit.submission(url=post_url)
        # Add your comment
        comment_text = comment
        # Post the comment
        submission.reply(comment_text)
        print("Comment posted successfully!")

    def create_post(self, subreddit, post_title, post_body):
        # Submit a text post
        subreddit = self.reddit.subreddit(subreddit)
        submission = subreddit.submit(post_title, selftext=post_body)
        print(f'Post created successfully! Here is the link: {submission.url}')
        return submission.url

