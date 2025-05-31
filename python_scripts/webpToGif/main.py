import splitWebp as sW
import cmbGpt as cGt
import cmbGptNoCache as cGtNC
import os

if __name__ == "__main__":
    webp_dir = "images/webps"  # 存放 webp 的目录
    output_gif_dir = os.path.join(webp_dir, "../gifs")  # 输出 gif 的目录
    os.makedirs(output_gif_dir, exist_ok=True)  # 自动创建 gifs 文件夹

    bool_cache = 1
    frame_cache = bool_cache
    duration_cache = bool_cache

    for filename in os.listdir(webp_dir):
        if filename.lower().endswith(".webp"):
            webp_path = os.path.join(webp_dir, filename)
            print(f"\n处理文件: {webp_path}")

            base_name = os.path.splitext(filename)[0]
            webp_dir_path = os.path.join(webp_dir, base_name + "_frames")
            gif_output_path = os.path.join(output_gif_dir, base_name + ".gif")

            if frame_cache == 1 and duration_cache == 1:
                durations = sW.split_webp_to_pngs(webp_path, frame_cache, duration_cache)
                print("使用缓存方式，生成了 durations。")
                cGt.pngs_to_gif(webp_dir_path, output_path=gif_output_path)
            else:
                images, durations = sW.split_webp_to_pngs(webp_path, frame_cache, duration_cache)
                print("使用内存方式，直接生成 GIF。")
                cGtNC.images_to_gif(images, durations, gif_output_path)
