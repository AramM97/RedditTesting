import praw

from Infra.utils import Utils

class CollecttionReddit:

    def __init__(self, reddit):
        self.reddit = reddit
        self.utils = Utils()
        self.config_file = self.utils.get_config_file()
        self.subreddit = self.utils.get_subreddit_name(self.config_file)

    def create_collection(self):
        self.my_sub = self.reddit.subreddit(self.subreddit)
        self.new_collection = self.my_sub.collections.mod.create(
                title="Title", description="desc", display_layout="GALLERY"
            )
        self.new_collection.mod.add_post("1biuyuz")

    def add_post_to_collection(self):
        collection = self.reddit.subreddit(self.subreddit).collections("some_uuid")
        collection.mod.add_post("1biuyuz")

    def upvote_post(self,submission):
        # Upvote the submission
        submission.upvote()

    def downvote_post(self, submission):
        # Downvote the submission
        submission.downvote()

    def refresh_votes(self, submission):
        # Refresh the submission object to see the updated vote counts
        submission.refresh()

    def print_votes(self, submission):
        # Print the updated vote counts
        print("Upvotes:", submission.ups)
        print("Downvotes:", submission.downs)