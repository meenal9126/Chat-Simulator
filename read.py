file_name = "chat.txt"

try:
    # Open the file safely using 'with'
    with open(file_name, "r", encoding="utf-8") as file:
        # Read just the first 500 characters so we don't flood the screen
        content_snippet = file.read(500)
        
    print("--- SUCCESS: Python read the file! ---")
    print("Here is a preview of your raw text:\n")
    print(content_snippet)

except FileNotFoundError:
    print(f"❌ ERROR: Could not find '{file_name}'.")