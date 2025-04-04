# Import necessary libraries
import csv
import requests
import sys

# Function to get and print the status code for each URL
def check_urls_from_csv(file_path):
    try:
        # Open and read the CSV file
        with open(file_path, mode='r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip the header row
            for row in csv_reader:
                url = row[0]  # Extract the URL from the first column
                try:
                    # Make an HTTP GET request to check the URL
                    response = requests.get(url, timeout=5)
                    # Print the status code and the corresponding URL
                    print(f"({response.status_code}) {url}")
                except requests.exceptions.RequestException as e:
                    # Print 000 and the exception name for unreachable URLs
                    print(f"(000 - {e.__class__.__name__}) {url}")
    except FileNotFoundError:
        # Handle the case where the file does not exist
        print(f"File {file_path} not found!")

# Run the function
check_urls_from_csv("Task_2_Intern.csv")

# Check if the file path was provided as an argument
if len(sys.argv) < 2:
    print("Usage: python script.py <file_path>")
else:
    # Run the function with the file path from the command-line argument
    check_urls_from_csv(sys.argv[1])
