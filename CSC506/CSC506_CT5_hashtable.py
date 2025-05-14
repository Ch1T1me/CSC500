class ContentRecommendationSystem:
    def __init__(self, size=100):
        """Initialize the hash table with a fixed size."""
        self.size = size
        self.table = {}  # Using a dictionary for efficient key-value storage

    def add_user(self, user_id, preferences):
        """Add a user with their content preferences."""
        self.table[user_id] = preferences

    def update_preferences(self, user_id, new_preferences):
        """Update a user's content preferences."""
        if user_id in self.table:
            self.table[user_id] = new_preferences
        else:
            print(f"User {user_id} not found!")

    def recommend_content(self, user_id):
        """Retrieve content recommendations based on user preferences."""
        return self.table.get(user_id, [])

    def remove_user(self, user_id):
        """Remove a user from the system."""
        if user_id in self.table:
            del self.table[user_id]
        else:
            print(f"User {user_id} not found!")

# Simulated usage
recommendation_system = ContentRecommendationSystem()

# Adding users and their content preferences
recommendation_system.add_user(101, ["Technology", "AI", "Programming"])
recommendation_system.add_user(102, ["Fitness", "Health", "Nutrition"])
recommendation_system.add_user(103, ["Movies", "Music", "Entertainment"])

# Updating preferences
recommendation_system.update_preferences(102, ["Health", "Mental Wellness", "Yoga"])

# Getting recommendations
print("User 101 recommendations:", recommendation_system.recommend_content(101))
print("User 102 recommendations:", recommendation_system.recommend_content(102))
print("User 103 recommendations:", recommendation_system.recommend_content(103))

# Removing a user
recommendation_system.remove_user(103)
print("User 103 recommendations after removal:", recommendation_system.recommend_content(103))
