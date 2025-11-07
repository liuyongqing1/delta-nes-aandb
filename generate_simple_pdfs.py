#!/usr/bin/env python3
"""
Delta NES Skin - 生成简单透明PDF
Delta会根据info.json处理按钮，PDF只需提供透明背景
"""

from PIL import Image

def generate_simple_portrait_pdf(output_file):
    """生成简单的竖屏 PDF - 完全透明"""
    print(f"正在生成简单竖屏布局: {output_file}")

    # 创建完全透明的图像
    width, height = 375, 812
    img = Image.new('RGBA', (width, height), (0, 0, 0, 0))

    # 保存为 PDF
    img.save(output_file, "PDF", resolution=100.0)
    print(f"✓ 竖屏 PDF 生成完成 (完全透明)")

def generate_simple_landscape_pdf(output_file):
    """生成简单的横屏 PDF - 完全透明"""
    print(f"正在生成简单横屏布局: {output_file}")

    # 创建完全透明的图像
    width, height = 812, 375
    img = Image.new('RGBA', (width, height), (0, 0, 0, 0))

    # 保存为 PDF
    img.save(output_file, "PDF", resolution=100.0)
    print(f"✓ 横屏 PDF 生成完成 (完全透明)")

def main():
    print("=" * 60)
    print("Delta NES 皮肤 - 简单透明PDF生成器")
    print("=" * 60)

    generate_simple_portrait_pdf("NES-AB.deltaskin/portrait.pdf")
    generate_simple_landscape_pdf("NES-AB.deltaskin/landscape.pdf")

    print("\n" + "=" * 60)
    print("PDF 文件生成完成！")
    print("=" * 60)
    print("\n说明:")
    print("  - 生成的是完全透明的PDF背景")
    print("  - Delta 会根据 info.json 自动处理按钮显示")
    print("  - 游戏画面可以完整显示")

if __name__ == "__main__":
    main()
