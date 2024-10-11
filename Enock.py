class JobApplicationSystem:
    def __init__(self):
        self.undo_stack = []
        self.application_queue = []
        self.job_postings = []

    def submit_application(self, application):
        self.undo_stack.append(application)
        self.application_queue.append(application)
        print(f"Application submitted: {application}")

    def undo_submission(self):
        if self.undo_stack:
            application = self.undo_stack.pop()
            self.application_queue.remove(application)
            print(f"Submission undone: {application}")
        else:
            print("No submissions to undo.")

    def process_application(self):
        if self.application_queue:
            application = self.application_queue.pop(0)
            print(f"Processing application: {application}")
        else:
            print("No applications to process.")

    def add_job_posting(self, job_posting):
        self.job_postings.append(job_posting)
        print(f"Job posting added: {job_posting}")

    def remove_job_posting(self, job_posting):
        if job_posting in self.job_postings:
            self.job_postings.remove(job_posting)
            print(f"Job posting removed: {job_posting}")
        else:
            print("Job posting not found.")
            
system = JobApplicationSystem()
system.add_job_posting("Software Engineer")
system.submit_application("John Doe's Application")
system.process_application()
system.undo_submission()
