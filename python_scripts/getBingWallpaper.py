import requests
import sys
import os
  
from datetime import datetime
  
def get_bing_wallpaper_url():
  
    url = "https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US"
  
    response = requests.get(url)
  
    data = response.json()
  
    image_url = "https://www.bing.com" + data['images'][0]['url']
  
    return image_url
  
  
def download_wallpaper(url, save_path):
  
    response = requests.get(url, stream=True)
  
    if response.status_code == 200:
  
        with open(save_path, 'wb') as f:
  
            for chunk in response.iter_content(1024):
  
                f.write(chunk)
  
    else:
  
        print("Failed to download wallpaper.")
  
  
def generate_save_path_with_date(base_path):
  
    current_date = datetime.now().strftime("%Y-%m-%d")
  
    filename = f"bing_wallpaper_{current_date}.jpg"
  
    return os.path.join(base_path, filename)
  
  
def main():

    # 传递路径

    if len(sys.argv) != 2:
        print("Usage: python3 demo.py /path/to/save")
        sys.exit(1)

    wallpaper_url = get_bing_wallpaper_url()

    base_save_path = sys.argv[1]
  
    save_path_with_date = generate_save_path_with_date(base_save_path)
  
    download_wallpaper(wallpaper_url, save_path_with_date)
  
    print(f"Wallpaper downloaded and saved to {save_path_with_date}")
  
  
if __name__ == "__main__":
  
    main()
