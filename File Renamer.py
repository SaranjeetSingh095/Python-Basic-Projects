import os

old_name = input("Old file name: ")
new_name = input("New file name: ")

os.rename(old_name, new_name)

print("Renamed Successfully.")
