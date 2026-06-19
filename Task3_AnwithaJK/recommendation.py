items = {
    "AI": ["AI Basics", "Deep Learning", "Neural Networks"],
    "Python": ["Python Course", "Flask Development", "Automation Scripts"],
    "Machine Learning": ["ML Fundamentals", "Regression Models", "Classification Models"],
    "Data Science": ["Data Analysis", "Pandas Tutorial", "Data Visualization"],
    "Web Development": ["HTML & CSS", "JavaScript Basics", "React Development"]
}

print("=== AI Recommendation System ===")

user_input = input(
    "Enter interests separated by commas: "
)

interests = user_input.split(",")

recommendations = []

for interest in interests:
    interest = interest.strip()

    if interest in items:
        recommendations.extend(items[interest])

print("\nRecommended Items:")

for item in recommendations:
    print("-", item)