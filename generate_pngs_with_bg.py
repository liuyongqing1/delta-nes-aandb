#!/usr/bin/env python3
"""
Delta NES 皮肤PNG生成器 - 带控制器背景条
上方透明显示游戏画面，下方半透明背景显示控制器按钮
"""

from PIL import Image, ImageDraw

def create_portrait_png_with_controller_bg(width, height, output_file):
    """生成竖屏PNG - 上方透明，下方半透明控制器背景"""
    print(f"  正在生成: {output_file} ({width}x{height})")

    img = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # 计算控制器区域 - 下方约35%
    controller_top = int(height * 0.65)

    # 绘制半透明控制器背景（深灰色，60%透明度）
    draw.rectangle(
        [(0, controller_top), (width, height)],
        fill=(40, 40, 40, 150)  # RGBA: 深灰色，alpha=150/255≈60%
    )

    img.save(output_file, "PNG")
    print(f"  ✓ 完成: 上方{controller_top}px透明，下方{height-controller_top}px半透明背景")

def create_landscape_png_with_controller_bg(width, height, output_file):
    """生成横屏PNG - 中间透明，两侧半透明控制器背景"""
    print(f"  正在生成: {output_file} ({width}x{height})")

    img = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # 左侧控制器区域（方向键）- 约30%
    left_width = int(width * 0.30)
    draw.rectangle(
        [(0, 0), (left_width, height)],
        fill=(40, 40, 40, 150)
    )

    # 右侧控制器区域（按钮）- 约30%
    right_start = int(width * 0.70)
    draw.rectangle(
        [(right_start, 0), (width, height)],
        fill=(40, 40, 40, 150)
    )

    img.save(output_file, "PNG")
    print(f"  ✓ 完成: 左侧{left_width}px和右侧{width-right_start}px半透明背景")

def main():
    """主函数"""
    print("\n" + "=" * 60)
    print("Delta NES 皮肤PNG生成器 - 带控制器背景")
    print("=" * 60)
    print("\n设计说明:")
    print("  - 竖屏: 上方65%透明(游戏区)，下方35%半透明(控制器)")
    print("  - 横屏: 中间40%透明(游戏区)，两侧各30%半透明(控制器)")
    print("  - 背景色: 深灰色(#282828)，透明度60%\n")

    skin_dir = "NES-AB.deltaskin"

    print("=" * 60)
    print("生成 iPhone 15 Pro 皮肤文件")
    print("=" * 60)

    # 标准分辨率
    create_portrait_png_with_controller_bg(393, 852, f"{skin_dir}/portrait.png")
    create_landscape_png_with_controller_bg(852, 393, f"{skin_dir}/landscape.png")

    # 高分辨率 @2x
    create_portrait_png_with_controller_bg(786, 1704, f"{skin_dir}/portrait@2x.png")
    create_landscape_png_with_controller_bg(1704, 786, f"{skin_dir}/landscape@2x.png")

    print("\n" + "=" * 60)
    print("✓ 所有PNG文件生成完成")
    print("=" * 60)
    print("\n效果预览:")
    print("  竖屏: ┌────────────┐")
    print("        │ 游戏画面   │ ← 透明，游戏可见")
    print("        │            │")
    print("        ├────────────┤")
    print("        │ [控制器]   │ ← 半透明背景")
    print("        └────────────┘")
    print("\n  横屏: ┌────┬────────┬────┐")
    print("        │[D] │ 游戏   │[AB]│")
    print("        └────┴────────┴────┘")
    print("         ↑     透明     ↑")
    print("       半透明          半透明")

if __name__ == "__main__":
    main()
