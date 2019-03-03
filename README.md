# Check WordPress Stats with Selenium

## What?
Tool ini berguna untuk login ke WP secara otomatis menggunakan Selenium dan melihat halaman stats di `/wp-admin/index.php?page=stats`.

## How?
### Masukkan credentials
Rename `credentials.json.ex` -> `credentials.json`, kemudian isikan:
- url
- username
- password
  
### Buat venv
```python3 -m venv env```

### Install Requirements
```pip install -r requirements.txt```

### Setting Selenium

#### Download Chrome webdriver disini:
```https://sites.google.com/a/chromium.org/chromedriver/downloads```

#### Tambahkan Path ke Chrome bin dan Chrome web driver di `env/bin/activate` atau di `~/.bashrc`:

```
export CHROME_DRIVER=/path/to/chromedriver 
export GOOGLE_CHROME_BIN=/path/to/google-chrome
```

### Jalankan Script
```python main.py```