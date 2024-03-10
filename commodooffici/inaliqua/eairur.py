# A dictionary that stores the names and ages of some people
self.data = {"Alice": 25, "Bob": 30, "Charlie": 35}

# A key to look for
key = "Bob"

# Check if the key is in the dictionary
if key in self.data:
    # If yes, print the value associated with the key
    print(f"{key} is {self.data[key]} years old.")
else:
    # If no, print a message
    print(f"{key} is not in the dictionary.")
