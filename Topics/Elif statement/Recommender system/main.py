age = int(input())  # Enter age to get a movie suggestion
if age > 60:
    print("Breakfast at Tiffany's")
elif 41 <= age <= 60:
    print("Pulp Fiction")
elif 26 <= age <= 40:
    print("Matrix")
elif 17 <= age <= 25:
    print("Trainspotting")
elif age <= 16:
    print("Lion King")
