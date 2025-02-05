<!-- Project Title -->
# 🔗 URL Shortener

A simple yet efficient **URL Shortener** built with **Python**, using **SQLite** for data storage and **hashlib** for generating short URLs. 🚀  

![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)  
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)  
[![GitHub stars](https://img.shields.io/github/stars/RahulPatil-Tech/CodeClauseInternship_URL_Shorteners?style=social)](https://github.com/RahulPatil-Tech/CodeClauseInternship_URL_Shorteners)  

---

## ⚡ Features  
✅ **Shorten Long URLs** 📏  
✅ **Retrieve Original URLs** 🔄  
✅ **SQLite Database Storage** 🗄️  
✅ **Fast & Lightweight** ⚡  
✅ **Easy-to-Use CLI Interface** 🖥️  

---

## 🚀 Getting Started  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/RahulPatil-Tech/CodeClauseInternship_URL_Shorteners.git
cd CodeClauseInternship_URL_Shorteners
```
### 2️⃣ Install Dependencies
Ensure Python is installed, then run:

```bash
pip install sqlite3
```
### 3️⃣ Run the Application
```bash
python url_shortener.py
```
---

## 📌 Usage
### 🎯 URL Shortener Menu:
```
URL Shortener
1. Shorten URL
2. Retrieve URL
3. Exit

Enter your choice:
```
### 🔹 Shorten a URL:
```bash
Enter the URL to shorten: https://www.example.com/some/long/url
Shortened URL: abcd1234
```
### 🔹 Retrieve the Original URL:
```bash

Enter the short URL: abcd1234
Original URL: https://www.example.com/some/long/url
```
---

# 🔍 How It Works
- The application generates an MD5 hash of the original URL.
- The first 8 characters of the hash are used as the shortened URL.
- URLs are stored in an SQLite database for retrieval.
-----

# 🛠️ Technologies Used
- Python 🐍
- SQLite 🗄️ (for database)
- hashlib 🔐 (for URL shortening)

------

# 🤝 Contributing
- Contributions are welcome! 🎉
- Fork the repo 🍴
- Create a new branch 🌿
- Commit your changes ✅
- Submit a PR 🚀
---------

# 📜 License
This project is licensed under the MIT License.

-------

# 📩 Contact
## 👤 Rahul Patil
### 📧 Email: rp3252154@gmail.com
### 🔗 LinkedIn: [Rahul_Patil](https://linkedin.com/in/rahul-patil-4bb533209/)  

------

Made with ❤️ by Rahul Patil 🚀
