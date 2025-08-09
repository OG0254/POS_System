def search_file(file_path, keyword): # file_path: the path to the text file you're searching in. AND keyword: the word or phrase you're looking for.
    try:
        with open(file_path, "r") as file:   # This tries to open the file in read mode ("r"). AND If successful, it reads all content into the variable content.

            content = file.read()
    except FileNotFoundError:     # If the file path is wrong or missing if the the file it prints the message you want
        print("File not found.")
        return []

    # Clean content and split by separator
    items = content.strip().split("-" * 40) # content.strip() removes whitespace from the beginning and end of the file
    results = []                                # .split("-" * 40) splits the text into separate project records, assuming your file uses ------- as a separator between projects.
                                                # Creates an empty list to store matching projects.
    for item in items:                    # Loops through each project.
        if keyword.lower() in item.lower():        # item and items pull from item.txt
            results.append(item.strip())

    return results                               # Once done checking all projects, it returns the matching list.
