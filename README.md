# Python Script - Task 2

### Objective
This task create a Python script that reads a list of URLs from a CSV file and checks their HTTP status codes by making requests to each URL.

## Implementation Details  
The script reads a CSV file containing a list of URLs and sends an HTTP GET request to each. It then prints the response status code next to the URL as:  
```
(STATUS CODE) URL
```
Example:  
```
(200) http://www.bolabrasilmulher.com.br/conheca-a-chu-santos-atacante-convocada-pela-tecnica-emily-lima/
(000 - ConnectionError) http://www.futeboldabahia.com.br/Feminino.html
(000 - ReadTimeout) http://www.periodicos.letras.ufmg.br/index.php/fulia/issue/view/677/showToc  
```  

### Features  
- Reads a list of URLs from a CSV file provided as a command-line argument.  
- Skips the header row to avoid processing non-URL data.  
- Makes HTTP requests to check the status codes of the URLs.  
- Displays the status code and the URL in a readable format.  
- Uses `(000 - Exception)` to indicate unreachable URLs and prints the exception name (Timeout, ConnectionError).

### Prerequisites  
- Python 3  
- `requests` library  
   
### Install the `requests` library:  
```
pip install requests
```  
## Usage

1. Place the CSV file in the same directory as the script.  
2. Run the script using:  
   ```bash
   python get_status_code.py Task_2_Intern.csv
   ```  

## Example Output  
```
(200) http://www.bolabrasilmulher.com.br/conheca-a-chu-santos-atacante-convocada-pela-tecnica-emily-lima/
(000 - ConnectionError) http://www.futeboldabahia.com.br/Feminino.html
(000 - ReadTimeout) http://www.periodicos.letras.ufmg.br/index.php/fulia/issue/view/677/showToc
```  
