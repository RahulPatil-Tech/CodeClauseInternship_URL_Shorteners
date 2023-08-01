## URL Shortener
A simple URL shortener application built in Python using SQLite for data storage and hashlib for URL shortening.

## Getting Started
1. Clone the repository:
```bash
Copy code
git clone https://github.com/RahulPatil-Tech/CodeClauseInternship_URL_Shorteners.git
```
2. Change into the project directory:
```bash
cd url-shortener
```
3. Install the required dependencies. Make sure you have Python and pip installed.
```bash
pip install sqlite3
```
## Usage
1. Run the application:
```bash
url_shortener.py
```

2. You will see the URL Shortener menu:
<b>
URL Shortener</br>
1. Shorten URL</br>
2. Retrieve URL</br>
3. Exit</br>
Enter your choice: </B></br>

3. To shorten a URL, choose option 1 and enter the original URL:
<b></br>
Enter the URL to shorten: https://www.example.com/some/long/url</br>
Shortened URL: abcd1234</b></br>

4. To retrieve the original URL, choose option 2 and enter the short URL:
<b>
Enter the short URL: abcd1234</br>
Original URL: https://www.example.com/some/long/url</b></br>

## How It Works
The URL shortener application uses a simple SQLite database to store the original URL and its corresponding short URL. When you enter a URL to shorten, it generates an MD5 hash of the original URL, takes the first 8 characters of the hash, and uses it as the short URL.

## Contributing
Contributions are welcome! If you find any bugs or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License.

