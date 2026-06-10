import re

# Input and output file names
input_file = "input.txt"
output_file = "emails.txt"

try:
    # Read content from the input file
    with open(input_file, "r") as file:
        content = file.read()

    # Extract email addresses using regular expression
    emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', content)

    # Remove duplicate emails
    unique_emails = list(set(emails))

    # Save extracted emails to output file
    with open(output_file, "w") as file:
        for email in unique_emails:
            file.write(email + "\n")

    print("=" * 40)
    print("EMAIL EXTRACTION COMPLETED")
    print("=" * 40)
    print(f"Total Emails Found: {len(unique_emails)}")
    print(f"Emails saved to '{output_file}'")

except FileNotFoundError:
    print(f"Error: '{input_file}' not found.")
except Exception as e:
    print("An error occurred:", e)