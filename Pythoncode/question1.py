list_user = ["admin", "root", "superuser1"]
current_user = "admin"  # Change this to test different users

if current_user == "admin":
    print("Permissions: Read, Write, Delete, Create")
elif current_user == "root":
    print("Permissions: Read, Write, Delete")
elif current_user in list_user:
    print("Permissions: Read, Write, Delete")
else:
    print("Permissions: Read, View")