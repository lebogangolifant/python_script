# Import necessary libraries
import csv
import requests

# Function to get and print the status code for each URL
def check_urls_from_csv(file_path):
    try:
        # Open and read the CSV file
        with open(file_path, mode='r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                url = row[0]  # Extract the URL from the first column
                try:
                    # Make an HTTP GET request to check the URL
                    response = requests.get(url, timeout=5)
                    # Print the status code and the corresponding URL
                    print(f"({response.status_code}) {url}")
                except requests.exceptions.RequestException:
                    # If an error occurs, print 000 as the status code
                    print(f"(000) {url}")  # Using 000 for unreachable URLs
    except FileNotFoundError:
        # Handle the case where the file does not exist
        print(f"File {file_path} not found!")

# Run the function
check_urls_from_csv("Task_2_Intern.csv")

