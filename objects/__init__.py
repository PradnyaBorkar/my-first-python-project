from objects.post import Post
from objects.user import User

user = User("Pradnya", "Borkar", "test@gmail.com", 1257, "developer", "123")
user.print_user_details()
user.change_job_title("Architect")
user.print_user_details()

post = Post(user.first_name, "This is my first post")
post.print_post()
