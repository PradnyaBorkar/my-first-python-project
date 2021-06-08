class User:
    def __init__(self, first_name, last_name, email, emp_id, job_title, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.empId = emp_id
        self.job_title = job_title
        self.password = password

    def change_password(self, new_password):
        self.password = new_password

    def change_job_title(self, new_job_title):
        self.job_title = new_job_title

    def print_user_details(self):
        print(f"User : {self.first_name} {self.last_name} currently works as {self.job_title}" )


