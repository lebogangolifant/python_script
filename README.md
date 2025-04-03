# Python Script - Outreachy Task 2

### Objective
This task create a Python script that reads a list of URLs from a CSV file and checks their HTTP status codes by making requests to each URL.

## Implementation Details  
The script reads a CSV file containing a list of URLs and sends an HTTP GET request to each. It then prints the response status code next to the URL as:  
```
(STATUS CODE) URL
```
Example:  
```
(200) https://www.nytimes.com/1999/07/04/sports/women-s-world-cup-sissi-of-brazil-has-right-stuff-with-left-foot.html  
(404) https://invalid-url.com  
(000) https://unreachable-site.com  
```
- If the URL is unreachable, the script will print `(000)` to indicate a connection error.  

### Features  
- Reads URLs from a CSV file.  
- Sends HTTP GET requests to check the status of each URL.  
- Prints the status code in the specified format.  
- Handles connection errors and prints `(000)` if a URL is unreachable.  

## Usage  

### Prerequisites  
- Python 3  
- `requests` library  
   
### Install the `requests` library:  
```
pip install requests
```  

### Running the Script  

#### Option 1: Locally on Your System  
1. Download the `Task_2_Intern.csv` file containing the list of URLs.  
2. Ensure the file is in the same directory as the Python script.  
3. Run the script using the following command:  
   ```bash
   python3 get_status_code.py
   ```
4. The script will print the status code for each URL in the specified format.  

