
student = {
    "name": "Ali",
    "age": 15,
    "city": "Hyderabad"
}

print(f"\nName: {student['name']}")
print(f"Age: {student['age']}")
print(f"City: {student['city']}")

new_city = input("\nEnter a new city to update: ")
student["city"] = new_city

print("\n--- Updated Dictionary ---")
print(f"Name: {student['name']}")
print(f"Age: {student['age']}")
print(f"City: {student['city']}\n")