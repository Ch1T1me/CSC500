class DeveloperTraits:
    def __init__(self):
        # Traits, attributes, and behaviors
        self.traits = {
            "Problem-Solving": {
                "Attributes": ["Critical Thinking", "Logical Reasoning"],
                "Behaviors": ["Debugging", "Analyzing Requirements"]
            },
            "Team Collaboration": {
                "Attributes": ["Communication Skills", "Empathy"],
                "Behaviors": ["Knowledge Sharing", "Conflict Resolution"]
            },
            "Adaptability": {
                "Attributes": ["Curiosity", "Flexibility"],
                "Behaviors": ["Learning New Technologies", "Applying Feedback"]
            }
        }

    def display_traits(self):
        # Format and print traits
        print("Traits of Excellent Software Developers")
        print("=" * 40)
        for trait, details in self.traits.items():
            print(f"\nTrait: {trait}")
            print(f"  Attributes: {', '.join(details['Attributes'])}")
            print(f"  Behaviors: {', '.join(details['Behaviors'])}")

if __name__ == "__main__":
    # Run the program
    developer_traits = DeveloperTraits()
    developer_traits.display_traits()
