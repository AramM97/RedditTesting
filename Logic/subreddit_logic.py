import praw

from Infra.utils import Utils


class SubReddit():
    URL = "'https://www.reddit.com/r/QAutomation/comments/1biuyuz/test_collections_post_1/'"

    def __init__(self, reddit):
        self.reddit = reddit
        self.utils = Utils()
        self.config = self.utils.get_config_file()
        self.subreddit_name = self.utils.get_subreddit_name(self.config)

    def post_comment(self, post_url, comment):
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

    def subscribe_to_subreddit(self, subreddit_name):
        self.reddit.subreddit(subreddit_name).subscribe()

    def unsubscribe_from_subreddit(self, subreddit_name):
        self.reddit.subreddit(subreddit_name).unsubscribe()

    def get_subscribed_subreddits(self):
        # Get the list of subscribed subreddits
        subscribed_subreddits = self.reddit.user.subreddits(limit=None)
        return subscribed_subreddits

    # Iterate over the subscribed subreddits and print their names
    def get_subscribed_subreddits(self, subscribed_subreddits):
        for subreddit in subscribed_subreddits:
            print(subreddit.display_name)

    def get_top_posts(self, subreddit_name ,limit=5):
        # Get the top 5 posts from the subreddit
        top_posts = self.reddit.subreddit(subreddit_name).top(limit)
        # Print the top 5 posts
        for post in top_posts:
            print(post.title)
            print("Score:", post.score)
            print("URL:", post.url)
            print("--------------------")

    def get_sub_count(self, subreddit):
        subreddit = self.reddit.subreddit(subreddit)
        subscriber_count = subreddit.subscribers
        print("Subreddit subscriber count:", subscriber_count)

    def active_user_count(self, subreddit):
        subreddit = self.reddit.subreddit(subreddit)
        active_user_count = subreddit.active_user_count
        print("Active user count:", active_user_count)

