import pandas as pd
import os
from datetime import datetime

# Used to convert a CSV file to MBOX format
# Made by Dr. Gibran Ali for MBTT use.
# Feel free to modify and use as needed.

def convert_to_mbox(df, output_file_path):
    with open(output_file_path, 'w') as file:
        for _, row in df.iterrows():
            # Get the email details, using placeholders if fields are empty
            subject = row.get('Subject', '(No Subject)')
            from_name = row.get('From: (Name)', 'Unknown Sender')
            from_address = row.get('From: (Address)', 'unknown@example.com')
            to_name = row.get('To: (Name)', 'Unknown Recipient')
            to_address = row.get('To: (Address)', 'unknown@example.com')
            date = datetime.now().strftime("%a, %d %b %Y %H:%M:%S")  # Current date if missing
            body = row.get('Body', '')

            # MBOX "From " separator (start of a new email)
            file.write(f"From {from_address} {date}\n")
            file.write(f"Subject: {subject}\n")
            file.write(f"From: {from_name} <{from_address}>\n")
            file.write(f"To: {to_name} <{to_address}>\n")
            file.write(f"Date: {date}\n")
            file.write("\n")  # Empty line between headers and body
            file.write(f"{body}\n")
            file.write("\n")  # Blank line between messages

# Get the current script directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Prompt the user for input and output filenames (without paths)
input_filename = input("Enter the name of the input CSV file (must be in the same directory): ")
output_filename = input("Enter the name for the output MBOX file (will be saved in the same directory): ")

# Construct full paths by combining with the current directory
csv_file_path = os.path.join(current_dir, input_filename)
mbox_file_path = os.path.join(current_dir, output_filename)

# Load the CSV file
df = pd.read_csv(csv_file_path)

# Clean column names to remove any problematic characters
df.columns = [col.replace("���\"", "").strip() for col in df.columns]

# Convert and save as MBOX
convert_to_mbox(df, mbox_file_path)

print(f"Conversion complete. File saved as {mbox_file_path}.")
