location = input("Enter vacuum location (A/B): ").upper()
status_A = input("Enter status of Room A (clean/dirty): ").lower()
status_B = input("Enter status of Room B (clean/dirty): ").lower()

print("\nInitial State:")
print("(", location, ",", status_A, ",", status_B, ")")

cost = 0

while status_A == "dirty" or status_B == "dirty":
    if location == "A":

        if status_A == "dirty":
            print("Action: Suck A")
            status_A = "clean"
            cost += 1
            print("State: (A,", status_A, ",", status_B, ")")
        else:
            print("Action: Move to B")
            location = "B"
            cost += 1
            print("State: (B,", status_A, ",", status_B, ")")

    else:
        if status_B == "dirty":
            print("Action: Suck B")
            status_B = "clean"
            cost += 1
            print("State: (B,", status_A, ",", status_B, ")")
        else:
            print("Action: Move to A")
            location = "A"
            cost += 1
            print("State: (A,", status_A, ",", status_B, ")")


print("\nFinal State:")
print("(", location, ",", status_A, ",", status_B, ")")

print("Cost:", cost)
