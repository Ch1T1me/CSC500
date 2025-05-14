class WaterfallModel:
    def __init__(self):
        self.phases = [
            "Communication (Requirement Gathering)",
            "Planning (Includes Risk Assessment)",
            "Modeling (Prototyping and Feedback)",
            "Construction (Incremental Testing)",
            "Deployment (User Feedback and Final Approval)"
        ]
        self.tasks = {}

    def gather_tasks(self):
        print("Welcome to the Modified Waterfall Model Program!")
        for phase in self.phases:
            task = input(f"Enter the key tasks for {phase}: ")
            self.tasks[phase] = task

    def display_model(self):
        print("\n--- Modified Waterfall Model ---")
        for phase, task in self.tasks.items():
            print(f"{phase}: {task}")

if __name__ == "__main__":
    model = WaterfallModel()
    model.gather_tasks()
    model.display_model()
