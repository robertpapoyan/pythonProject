#Here we are going to have deeper work with python



luckyNumbers = [156,12,12,54,987,54,54,75]
friends =["Aram", "Gago", "Musho", "Saqo", "Miqo"]

# Add luckyNumbers List to friends list
friends.extend(luckyNumbers)
print(friends)
# Adds an element to the list
friends.append("Brat")
print(friends)

# Adds an element to particular place
friends.insert(2, 123)
print(friends)

# Adding a list in the place where we want it to be
friends.insert(1, luckyNumbers)
print(friends)
# As you can see, if I am adding a list in particular place, the exact index is becoming a one list element
# So it means, in this case, the element with index 1 in friends list is a list.
print(friends[1])

# Remove elements from list
friends.remove("Brat")
print(friends)

friends.remove(luckyNumbers)
print(friends)

# Find an element in list
print(luckyNumbers.index(12))

# Find out how many of particular elements exist in this list
print(luckyNumbers.count(12))

# Sorting the list elements
luckyNumbers.sort()
print(luckyNumbers)

friends =["Aram", "Gago", "Musho", "Saqo", "Miqo"]
friends.sort()
print(friends)

# Making the list elements be displayed from last to first
friends.reverse()
print(friends)

luckyNumbers.reverse()
print(luckyNumbers)

luckyNumbers2 = luckyNumbers.copy()
print(luckyNumbers2)


