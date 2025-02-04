class RestaurantRecommender:
    def __init__(self, restaurants, user_preferences):
        self.restaurants = restaurants
        self.user_preferences = user_preferences

    def calculate_utility(self, restaurant):
        weight_cuisine = 0.3
        weight_location = 0.3
        weight_rating = 0.4

        cuisine_score = 1 if restaurant['cuisine'] == self.user_preferences['cuisine'] else 0
        location_score = 1 if restaurant['location'] == self.user_preferences['location'] else 0
        rating_score = restaurant['rating'] / 5

        utility = (
            cuisine_score * weight_cuisine +
            location_score * weight_location +
            rating_score * weight_rating
        )
        return utility

    def recommend_restaurant(self):
        best_restaurant = None
        highest_utility = float('-inf')

        for restaurant in self.restaurants:
            utility = self.calculate_utility(restaurant)
            if utility > highest_utility:
                highest_utility = utility
                best_restaurant = restaurant
        
        return best_restaurant


restaurants = [
    {"name": "Pasta Place", "cuisine": "Italian", "location": "Downtown", "rating": 4.5},
    {"name": "Sushi Spot", "cuisine": "Japanese", "location": "Uptown", "rating": 4.8},
    {"name": "Taco Town", "cuisine": "Mexican", "location": "Downtown", "rating": 4.2}
]

user_preferences = {"cuisine": "Japanese", "location": "Uptown"}

agent = RestaurantRecommender(restaurants, user_preferences)
best_choice = agent.recommend_restaurant()

print(f"Recommended Restaurant: {best_choice['name']} with rating {best_choice['rating']}")

