#!/usr/bin/env python3
"""
Delta NES Skin PDF Generator v2
使用 PIL/Pillow 生成兼容 Delta 的 PDF 文件
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_rounded_rectangle_mask(size, radius):
    """创建圆角矩形遮罩"""
    mask = Image.new('L', size, 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle([(0, 0), size], radius=radius, fill=255)
    return mask

def draw_button(draw, x, y, width, height, label, color, alpha=128):
    """绘制一个半透明按钮"""
    # 创建按钮图层
    button_img = Image.new('RGBA', (int(width), int(height)), (0, 0, 0, 0))
    button_draw = ImageDraw.Draw(button_img)

    # 绘制圆角矩形背景
    button_draw.rounded_rectangle(
        [(0, 0), (width-1, height-1)],
        radius=5,
        fill=(*color, alpha),
        outline=(255, 255, 255, int(alpha * 1.2)),
        width=2
    )

    # 添加文字
    try:
        font_size = int(min(width, height) * 0.4)
        # 尝试使用系统字体
        try:
            font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", font_size)
        except:
            font = ImageFont.load_default()
    except:
        font = ImageFont.load_default()

    # 获取文字边界框
    bbox = button_draw.textbbox((0, 0), label, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    text_x = (width - text_width) / 2
    text_y = (height - text_height) / 2 - bbox[1]

    button_draw.text((text_x, text_y), label, fill=(255, 255, 255, 200), font=font)

    return button_img

def draw_dpad(width, height):
    """绘制方向键"""
    dpad_img = Image.new('RGBA', (int(width), int(height)), (0, 0, 0, 0))
    draw = ImageDraw.Draw(dpad_img)

    center_x = width / 2
    center_y = height / 2
    arm_width = width * 0.35
    arm_length = height * 0.45

    color = (70, 70, 70, 128)  # 深灰色，半透明
    outline = (255, 255, 255, 150)

    # 绘制十字形状的各个部分
    # 上
    draw.rectangle(
        [(center_x - arm_width/2, center_y - arm_length),
         (center_x + arm_width/2, center_y)],
        fill=color, outline=outline, width=2
    )

    # 下
    draw.rectangle(
        [(center_x - arm_width/2, center_y),
         (center_x + arm_width/2, center_y + arm_length)],
        fill=color, outline=outline, width=2
    )

    # 左
    draw.rectangle(
        [(center_x - arm_length, center_y - arm_width/2),
         (center_x, center_y + arm_width/2)],
        fill=color, outline=outline, width=2
    )

    # 右
    draw.rectangle(
        [(center_x, center_y - arm_width/2),
         (center_x + arm_length, center_y + arm_width/2)],
        fill=color, outline=outline, width=2
    )

    # 中心圆
    r = arm_width / 2
    draw.ellipse(
        [(center_x - r, center_y - r), (center_x + r, center_y + r)],
        fill=color
    )

    # 添加方向箭头
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 14)
    except:
        font = ImageFont.load_default()

    draw.text((center_x - 5, center_y - arm_length + 5), "↑", fill=(255, 255, 255, 200), font=font)
    draw.text((center_x - 5, center_y + arm_length - 20), "↓", fill=(255, 255, 255, 200), font=font)
    draw.text((center_x - arm_length + 5, center_y - 10), "←", fill=(255, 255, 255, 200), font=font)
    draw.text((center_x + arm_length - 15, center_y - 10), "→", fill=(255, 255, 255, 200), font=font)

    return dpad_img

def generate_portrait_pdf(output_file):
    """生成竖屏 PDF (375x812)"""
    print(f"正在生成竖屏布局: {output_file}")

    # 创建透明背景的图像
    width, height = 375, 812
    img = Image.new('RGBA', (width, height), (0, 0, 0, 0))

    # 绘制方向键 (45, 520, 100x100)
    dpad = draw_dpad(100, 100)
    img.paste(dpad, (45, 520), dpad)

    # 绘制 A 按钮 (313, 540, 47x47) - 红色
    a_button = draw_button(None, 0, 0, 47, 47, "A", (231, 76, 60))
    img.paste(a_button, (313, 540), a_button)

    # 绘制 B 按钮 (250, 560, 47x47) - 橙色
    b_button = draw_button(None, 0, 0, 47, 47, "B", (230, 126, 34))
    img.paste(b_button, (250, 560), b_button)

    # 绘制 A+B 组合按钮 (280, 485, 52x52) - 紫色
    ab_button = draw_button(None, 0, 0, 52, 52, "A+B", (155, 89, 182))
    img.paste(ab_button, (280, 485), ab_button)

    # 绘制 Select 按钮 (135, 650, 35x22) - 灰色
    sel_button = draw_button(None, 0, 0, 35, 22, "SEL", (127, 140, 141))
    img.paste(sel_button, (135, 650), sel_button)

    # 绘制 Start 按钮 (190, 650, 35x22) - 灰色
    sta_button = draw_button(None, 0, 0, 35, 22, "STA", (127, 140, 141))
    img.paste(sta_button, (190, 650), sta_button)

    # 绘制 Menu 按钮 (10, 10, 32x32) - 蓝色
    menu_button = draw_button(None, 0, 0, 32, 32, "☰", (52, 152, 219))
    img.paste(menu_button, (10, 10), menu_button)

    # 保存为 PDF
    img.save(output_file, "PDF", resolution=100.0, save_all=True)
    print(f"✓ 竖屏 PDF 生成完成 (透明背景，PIL格式)")

def generate_landscape_pdf(output_file):
    """生成横屏 PDF (812x375)"""
    print(f"正在生成横屏布局: {output_file}")

    # 创建透明背景的图像
    width, height = 812, 375
    img = Image.new('RGBA', (width, height), (0, 0, 0, 0))

    # 绘制方向键 (65, 110, 120x120)
    dpad = draw_dpad(120, 120)
    img.paste(dpad, (65, 110), dpad)

    # 绘制 A 按钮 (675, 140, 55x55) - 红色
    a_button = draw_button(None, 0, 0, 55, 55, "A", (231, 76, 60))
    img.paste(a_button, (675, 140), a_button)

    # 绘制 B 按钮 (600, 165, 55x55) - 橙色
    b_button = draw_button(None, 0, 0, 55, 55, "B", (230, 126, 34))
    img.paste(b_button, (600, 165), b_button)

    # 绘制 A+B 组合按钮 (635, 95, 58x58) - 紫色
    ab_button = draw_button(None, 0, 0, 58, 58, "A+B", (155, 89, 182))
    img.paste(ab_button, (635, 95), ab_button)

    # 绘制 Select 按钮 (330, 220, 40x25) - 灰色
    sel_button = draw_button(None, 0, 0, 40, 25, "SEL", (127, 140, 141))
    img.paste(sel_button, (330, 220), sel_button)

    # 绘制 Start 按钮 (395, 220, 40x25) - 灰色
    sta_button = draw_button(None, 0, 0, 40, 25, "STA", (127, 140, 141))
    img.paste(sta_button, (395, 220), sta_button)

    # 绘制 Menu 按钮 (10, 10, 35x35) - 蓝色
    menu_button = draw_button(None, 0, 0, 35, 35, "☰", (52, 152, 219))
    img.paste(menu_button, (10, 10), menu_button)

    # 保存为 PDF
    img.save(output_file, "PDF", resolution=100.0, save_all=True)
    print(f"✓ 横屏 PDF 生成完成 (透明背景，PIL格式)")

def main():
    """主函数"""
    print("=" * 60)
    print("Delta NES 皮肤 PDF 生成器 v2 (PIL/Pillow)")
    print("=" * 60)

    # 生成竖屏 PDF
    generate_portrait_pdf("NES-AB.deltaskin/portrait.pdf")

    # 生成横屏 PDF
    generate_landscape_pdf("NES-AB.deltaskin/landscape.pdf")

    print("\n" + "=" * 60)
    print("所有 PDF 文件已生成完成！")
    print("=" * 60)
    print("\n文件位置:")
    print("  - NES-AB.deltaskin/portrait.pdf")
    print("  - NES-AB.deltaskin/landscape.pdf")
    print("\n✨ 特性:")
    print("  - 使用 PIL/Pillow 生成，更好的兼容性")
    print("  - 透明背景 - 游戏画面不会被遮挡")
    print("  - 半透明按钮 - 既能看到按钮又不影响游戏视野")
    print("\n按钮颜色:")
    print("  - 🔴 红色 (A): A 按钮")
    print("  - 🟠 橙色 (B): B 按钮")
    print("  - 🟣 紫色 (A+B): 组合按钮 - 同时按下 A 和 B")
    print("  - ⚫ 灰色 (SEL/STA): Select 和 Start 按钮")
    print("  - 🔵 蓝色 (☰): Delta 菜单按钮")
    print("  - ⚫ 深灰色: 方向键")
    print("\n💡 提示: PDF 使用 PIL 生成，应该可以正常导入 Delta 了！")

if __name__ == "__main__":
    main()
