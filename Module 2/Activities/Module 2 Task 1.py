role = input("Enter your role (admin / employee / guest): ").strip().lower()
clearance_level = int(input("Enter clearance level (1 to 5): "))
is_active = input("Is the account active? (yes/no): ").strip().lower() == "yes"

if not is_active:
    print("Access Denied: Account is inactive.")
elif role == "admin":
    print("Access Granted: Full administrative access.")
elif role == "employee" and clearance_level >= 3:
    print("Access Granted: Standard employee access.")
elif role == "guest" and clearance_level == 1:
    print("Access Granted: Guest view access.")
else:
    print("Access Denied: Insufficient permissions.")


# In[ ]:





