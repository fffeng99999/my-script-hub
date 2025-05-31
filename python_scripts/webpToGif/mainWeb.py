import os
import requests
import splitWebp as sW
import cmbGptNoCache as cGtNC

def download_webp(url, save_dir="images/webps"):
    os.makedirs(save_dir, exist_ok=True)
    filename = os.path.basename(url)
    save_path = os.path.join(save_dir, filename)

    if os.path.exists(save_path):
        print(f"文件已存在，跳过下载: {save_path}")
        return save_path

    print(f"开始下载: {url}")
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        with open(save_path, "wb") as f:
            f.write(resp.content)
        print(f"保存成功: {save_path}")
        return save_path
    else:
        print(f"下载失败，状态码: {resp.status_code}")
        return None

def main():
    webp_dir = "images/webps"
    gif_dir = "images/gifs"
    os.makedirs(gif_dir, exist_ok=True)

    print("输入webp链接，输入exit()退出")

    while True:
        url = input("请输入webp链接: ").strip()
        if url.lower() == "exit()":
            print("退出程序。")
            break
        if not url.lower().endswith(".webp"):
            print("请输入有效的webp链接")
            continue

        webp_path = download_webp(url, webp_dir)
        if not webp_path:
            continue

        base_name = os.path.splitext(os.path.basename(webp_path))[0]
        gif_path = os.path.join(gif_dir, base_name + ".gif")

        print("开始转换webp为gif...")

        # 用内存方式拆分webp并生成gif（不缓存PNG文件）
        images, durations = sW.split_webp_to_pngs(webp_path, 0, 0)
        cGtNC.images_to_gif(images, durations, gif_path)

if __name__ == "__main__":
    main()
