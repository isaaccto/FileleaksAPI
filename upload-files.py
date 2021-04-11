import requests


try:

    # upload files.
    files = {
        "file": ("filename", "filepath", "rb")
    }

    upload = requests.post("https://api.fileleaks.com/upload", files=files)

    try:

        # get download link 
        x = upload.json()
        url = x["data"]["file"]["url"]["short"]
        print(url)
        input()
    
    except Exception as e:
        print(e)
        # can't get download link.
  
except Exception as e:
    print(e)
    # your file can't be uploaded.