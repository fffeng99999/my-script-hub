from PIL import Image
import os

def images_to_gif(images, durations, output_path, loop=0):
    """
    直接把Image对象列表转成GIF，使用对应的durations列表，并保留透明背景
    """
    if not images:
        print("没有图片传入")
        return

    converted = []
    for im in images:
        alpha = im.getchannel('A')

        # 转为P模式（调色板图像）
        p = im.convert('P', palette=Image.ADAPTIVE, colors=255)

        # 设置透明区域为调色板索引255
        mask = Image.eval(alpha, lambda a: 255 if a <= 128 else 0)
        p.paste(255, mask)
        p.info['transparency'] = 255

        converted.append(p)

    # 用处理好的 converted 进行保存，避免黑底
    converted[0].save(
        output_path,
        save_all=True,
        append_images=converted[1:],  # ✅ 使用 converted 而不是 images
        duration=durations,
        loop=loop,
        disposal=2,
        transparency=255
    )

    print(f"GIF已保存: {output_path}")
