import sys


# Function to update the version number in the content
def update_version(content, version_index):
    old_version = now_version(content, version_index)
    # Increase the version number by 0.1 while retaining one decimal place
    new_version = round(old_version + 0.1, 1)

    # Update the version number and write it back to the file
    new_content = content.replace(str(old_version), str(new_version))
    with open("./version/version.py", "w") as f:
        f.write(new_content)
    return 0


# Function to retrieve the current version number from the content
def now_version(content, version_index):
    # Extract the line containing the version number
    version_line = content[version_index : content.find("\n", version_index)]
    old_version = float(version_line.split("=")[1].strip())
    return old_version


def main():
    # Read the contents of the 'version.py' file
    with open("./version/version.py", "r") as f:
        content = f.read()
    version_index = content.find("version =")
    if version_index != -1:
        # Check the command-line argument to determine the action
        action = sys.argv[1]
        if action == "update":
            update_version(content, version_index)
        elif action == "now":
            print("Now_version :", now_version(content, version_index))
    else:
        print("Error: Version number not found!")


if __name__ == "__main__":
    main()
