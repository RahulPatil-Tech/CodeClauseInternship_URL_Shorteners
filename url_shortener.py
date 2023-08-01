import hashlib
import sqlite3

conn = sqlite3.connect('urls.db')
cursor = conn.cursor()

# Create the 'urls' table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS urls (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        original_url TEXT NOT NULL,
        short_url TEXT NOT NULL
    )
''')

def generate_short_url(original_url):
    hash_object = hashlib.md5(original_url.encode())
    hash_digest = hash_object.hexdigest()
    short_url = hash_digest[:8]
    return short_url

def store_url(original_url, short_url):
    cursor.execute('INSERT INTO urls (original_url, short_url) VALUES (?, ?)', (original_url, short_url))
    conn.commit()

def get_original_url(short_url):
    cursor.execute('SELECT original_url FROM urls WHERE short_url = ?', (short_url,))
    result = cursor.fetchone()
    if result:
        return result[0]
    else:
        return None

while True:
    print('URL Shortener')
    print('1. Shorten URL')
    print('2. Retrieve URL')
    print('3. Exit')
    choice = input('Enter your choice: ')

    if choice == '1':
        original_url = input('Enter the URL to shorten: ')
        short_url = generate_short_url(original_url)
        store_url(original_url, short_url)
        print('Shortened URL:', short_url)
        print()

    elif choice == '2':
        short_url = input('Enter the short URL: ')
        original_url = get_original_url(short_url)
        if original_url:
            print('Original URL:', original_url)
        else:
            print('URL not found')
        print()

    elif choice == '3':
        break

conn.close()