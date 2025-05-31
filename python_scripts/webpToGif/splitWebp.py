from PIL import Image
import os


def split_webp_to_pngs(webp_path, frame_cache, durations_cache):
    """
    将WebP图片拆分成多个PNG图片，并记录每帧的持续时间
    Args:
        webp_path: WebP图片的路径
    Returns:
        list: 所有生成的PNG文件路径列表
        :param webp_path:
        :param durations_cache:
        :param frame_cache:
    """
    if not os.path.exists(webp_path):
        raise FileNotFoundError(f"未找到文件: {webp_path}")

    if frame_cache:

        with Image.open(webp_path) as img:
            frames_count = getattr(img, 'n_frames', 1)

            if frames_count == 1:
                png_path = webp_path.replace('.webp', '.png')
                img.save(png_path, 'PNG')
                return [png_path]

            base_dir = os.path.splitext(webp_path)[0] + '_frames'
            os.makedirs(base_dir, exist_ok=True)

            png_files = []
            durations = []

            for frame_num in range(frames_count):
                img.seek(frame_num)

                if img.mode != 'RGBA':
                    img = img.convert('RGBA')

                frame_png_path = os.path.join(
                    base_dir,
                    f"{os.path.basename(os.path.splitext(webp_path)[0])}_frame_{frame_num:03d}.png"
                )

                img.save(frame_png_path, 'PNG')
                png_files.append(frame_png_path)

                # 获取当前帧的持续时间（单位：毫秒）
                duration = img.info.get("duration", 100)
                durations.append(duration)

            if durations_cache and frame_cache:
                # 保存持续时间信息到 durations.txt
                durations_txt_path = os.path.join(base_dir, 'durations.txt')
                with open(durations_txt_path, 'w') as f:
                    for d in durations:
                        f.write(f"{d}\n")

        try:
            print(f"成功拆分！生成了以下PNG文件：")
            for i, png_file in enumerate(png_files, 1):
                print(f"{i:03d}. {png_file}")
        except Exception as e:
            print(f"错误: {str(e)}")

        return durations

    else:
        images = []
        durations = []

        with Image.open(webp_path) as img:
            frames_count = getattr(img, 'n_frames', 1)

            for frame_num in range(frames_count):
                img.seek(frame_num)
                frame = img.convert('RGBA')  # 确保模式一致
                images.append(frame.copy())  # 拷贝一份，避免后续seek影响

                duration = img.info.get("duration", 100)
                durations.append(duration)

        return images, durations


# 使用示例
if __name__ == "__main__":
    webp_file = "images/webps/beaming-face-with-smiling-eyes_1f601.webp"
    split_webp_to_pngs(webp_file, 1, 1)
    #     png_files = split_webp_to_pngs(webp_file)
    #     print(f"成功拆分！生成了以下PNG文件：")
    #     for i, png_file in enumerate(png_files, 1):
    #         print(f"{i}. {png_file}")
    # except Exception as e:
    #     print(f"错误: {str(e)}")
