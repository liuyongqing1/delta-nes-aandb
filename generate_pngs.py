#!/usr/bin/env python3
"""
Delta NES Skin - 生成PNG格式皮肤文件
使用PNG代替PDF，可能更兼容Delta
"""

from PIL import Image, ImageDraw, ImageFont

def create_button_overlay(width, height):
    """创建带有半透明按钮的覆盖层"""
    img = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    return img

def generate_portrait_png(output_file):
    """生成竖屏 PNG (375x812)"""
    print(f"正在生成竖屏布局: {output_file}")

    width, height = 375, 812
    # 创建完全透明的PNG - Delta会处理按钮显示
    img = Image.new('RGBA', (width, height), (0, 0, 0, 0))

    # 保存为 PNG
    img.save(output_file, "PNG")
    print(f"✓ 竖屏 PNG 生成完成 (透明背景)")

def generate_landscape_png(output_file):
    """生成横屏 PNG (812x375)"""
    print(f"正在生成横屏布局: {output_file}")

    width, height = 812, 375
    # 创建完全透明的PNG - Delta会处理按钮显示
    img = Image.new('RGBA', (width, height), (0, 0, 0, 0))

    # 保存为 PNG
    img.save(output_file, "PNG")
    print(f"✓ 横屏 PNG 生成完成 (透明背景)")

def generate_portrait_png_2x(output_file):
    """生成高分辨率竖屏 PNG (750x1624)"""
    print(f"正在生成高分辨率竖屏布局: {output_file}")

    width, height = 750, 1624  # 2x resolution
    img = Image.new('RGBA', (width, height), (0, 0, 0, 0))

    # 保存为 PNG
    img.save(output_file, "PNG")
    print(f"✓ 高分辨率竖屏 PNG 生成完成")

def generate_landscape_png_2x(output_file):
    """生成高分辨率横屏 PNG (1624x750)"""
    print(f"正在生成高分辨率横屏布局: {output_file}")

    width, height = 1624, 750  # 2x resolution
    img = Image.new('RGBA', (width, height), (0, 0, 0, 0))

    # 保存为 PNG
    img.save(output_file, "PNG")
    print(f"✓ 高分辨率横屏 PNG 生成完成")

def main():
    print("=" * 60)
    print("Delta NES 皮肤 - PNG 文件生成器")
    print("=" * 60)

    # 生成标准分辨率PNG
    generate_portrait_png("NES-AB.deltaskin/portrait.png")
    generate_landscape_png("NES-AB.deltaskin/landscape.png")

    # 生成高分辨率PNG (可选)
    generate_portrait_png_2x("NES-AB.deltaskin/portrait@2x.png")
    generate_landscape_png_2x("NES-AB.deltaskin/landscape@2x.png")

    print("\n" + "=" * 60)
    print("PNG 文件生成完成！")
    print("=" * 60)
    print("\n文件位置:")
    print("  - NES-AB.deltaskin/portrait.png")
    print("  - NES-AB.deltaskin/landscape.png")
    print("  - NES-AB.deltaskin/portrait@2x.png")
    print("  - NES-AB.deltaskin/landscape@2x.png")
    print("\n说明:")
    print("  - 生成的是完全透明的PNG背景")
    print("  - Delta 会根据 info.json 自动处理按钮显示")
    print("  - 需要修改 info.json 将 PDF 引用改为 PNG")

if __name__ == "__main__":
    main()
