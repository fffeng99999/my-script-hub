import os
import time
import requests
import pyperclip
import splitWebp as sW
import cmbGptNoCache as cGtNC
from urllib.parse import urlparse

def download_webp(url, save_dir="images/webps"):
    os.makedirs(save_dir, exist_ok=True)
    filename = os.path.basename(urlparse(url).path)
    save_path = os.path.join(save_dir, filename)

    if os.path.exists(save_path):
        print(f"[跳过] 已存在: {filename}")
        return save_path

    print(f"[下载] {url}")
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    try:
        resp = requests.get(url, headers=headers)
        if resp.status_code == 200:
            with open(save_path, "wb") as f:
                f.write(resp.content)
            print(f"[保存] 成功: {save_path}")
            return save_path
        else:
            print(f"[错误] 下载失败，状态码: {resp.status_code}")
            return None
    except Exception as e:
        print(f"[异常] 下载失败: {e}")
        return None

def process_webp_to_gif(webp_path, gif_dir="images/gifs"):
    os.makedirs(gif_dir, exist_ok=True)
    base_name = os.path.splitext(os.path.basename(webp_path))[0]
    gif_path = os.path.join(gif_dir, base_name + ".gif")

    print(f"[转换] WebP 转 GIF: {gif_path}")
    images, durations = sW.split_webp_to_pngs(webp_path, 0, 0)
    cGtNC.images_to_gif(images, durations, gif_path)
    print(f"[完成] 已保存 GIF\n")

def main():
    print("📋 监控剪贴板中 .webp 链接，按 Ctrl+C 退出")
    seen_links = set()
    last_text = ""

    try:
        while True:
            text = pyperclip.paste().strip()
            if text != last_text:
                last_text = text
                if text.lower().endswith(".webp") and text not in seen_links:
                    seen_links.add(text)
                    webp_path = download_webp(text)
                    if webp_path:
                        process_webp_to_gif(webp_path)
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n🛑 监控停止，程序已退出。")

if __name__ == "__main__":
    main()
