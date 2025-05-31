import os
from PIL import Image

DEFAULT_DURATION = 66

def pngs_to_gif(input_dir, output_path=None, duration=200, loop=0):
    # 获取 PNG 文件
    png_files = sorted([
        f for f in os.listdir(input_dir)
        if f.lower().endswith('.png')
    ])
    if not png_files:
        print("目录中没有 PNG 文件。")
        return

    # 自动输出路径
    if output_path is None:
        dir_base = os.path.basename(input_dir.rstrip("/\\"))
        if dir_base.endswith("_frames"):
            dir_base = dir_base[:-7]
        output_path = os.path.join(os.path.dirname(input_dir), f"{dir_base}.gif")

    # 尝试读取 durations.txt
    durations_path = os.path.join(input_dir, 'durations.txt')
    if os.path.exists(durations_path):
        with open(durations_path, 'r') as f:
            durations = [int(line.strip()) for line in f if line.strip().isdigit()]
        if len(durations) != len(png_files):
            print("警告：durations.txt 的帧数与 PNG 文件数不一致，使用默认时间。")
            durations = [duration] * len(png_files)
    else:
        durations = [duration] * len(png_files)

    # 加载所有图像，转为RGBA
    images = [Image.open(os.path.join(input_dir, f)).convert('RGBA') for f in png_files]

    # 转为P模式 + 设置透明色
    converted = []
    for im in images:
        alpha = im.getchannel('A')

        # 转P模式并保留透明色
        p = im.convert('P', palette=Image.ADAPTIVE, colors=255)

        # 设置透明区域为调色板索引 255
        mask = Image.eval(alpha, lambda a: 255 if a <= 128 else 0)
        p.paste(255, mask)
        p.info['transparency'] = 255

        converted.append(p)

    # 保存GIF
    converted[0].save(
        output_path,
        save_all=True,
        append_images=converted[1:],
        duration=durations,
        loop=loop,
        disposal=2,
        transparency=255
    )

    print(f"GIF 已保存到: {output_path}")

# 示例用法
if __name__ == "__main__":
    pngs_to_gif("images/beaming-face-with-smiling-eyes_1f601_frames", duration=DEFAULT_DURATION)
