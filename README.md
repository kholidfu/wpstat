# Check WordPress Stats with Selenium

## What?
Tool ini berguna untuk login ke WP secara otomatis menggunakan Selenium dan melihat halaman stats di `/wp-admin/index.php?page=stats`.

## Requirements?
- python 3.7
- python-wordpress-xmlrpc
- selenium

## How?
**1. Masukkan Credentials**
Rename `credentials.json.ex` -> `credentials.json`, kemudian isikan:
- url
- username
- password
  
**2. Buat Virtual Environment**
```
python3 -m venv env
```

**3. Install Requirements**
```
pip install -r requirements.txt
```

**4. Setting Selenium**

**4.a. Download Chrome Webdriver**
```
https://sites.google.com/a/chromium.org/chromedriver/downloads
```

**4.b. Tambahkan Path ke Chrome bin dan Chrome web driver di** `env/bin/activate` **atau di** `~/.bashrc`:

```
export CHROME_DRIVER=/path/to/chromedriver 
export GOOGLE_CHROME_BIN=/path/to/google-chrome
```

**5. Jalankan Script**
```python main.py```