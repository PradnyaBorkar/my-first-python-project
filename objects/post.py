class Post:
    def __init__(self, author, message):
        self.author = author
        self.message = message

    def print_post(self):
        print(f"Post '{self.message}' written by {self.author} \n")
