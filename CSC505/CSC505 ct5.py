class PHTRS:
    def __init__(self):
        self.actors = [
            "Citizen", 
            "Public Works Employee", 
            "Repair Crew", 
            "Administration"
        ]
        self.use_cases = {
            "Citizen": ["Report Pothole", "Log Damage Claims"],
            "Public Works Employee": ["Assign Work Orders", "Track Repairs", 
                                      "Update Repair Status"],
            "Administration": ["Generate Reports"]
        }

    def display_actors(self):
        print("\n--- PHTRS Actors ---")
        for actor in self.actors:
            print(f"- {actor}")

    def display_use_cases(self):
        print("\n--- Use Cases for Each Actor ---")
        for actor, use_cases in self.use_cases.items():
            print(f"{actor}:")
            for use_case in use_cases:
                print(f"  * {use_case}")

if __name__ == "__main__":
    print("Welcome to the PHTRS System Overview\n")
    phtrs = PHTRS()
    phtrs.display_actors()
    phtrs.display_use_cases()
