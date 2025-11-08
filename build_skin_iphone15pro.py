#!/usr/bin/env python3
"""
Delta NES 皮肤一键生成和打包工具
生成PNG文件并打包成可直接导入的.deltaskin文件

适配 iPhone 15 Pro (393x852)
"""

import os
import zipfile
from PIL import Image

def create_transparent_png(width, height, output_file):
    """创建完全透明的PNG文件"""
    img = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    img.save(output_file, "PNG")
    print(f"  ✓ 生成: {output_file} ({width}x{height})")

def generate_skin_assets():
    """生成皮肤资源文件"""
    print("\n" + "=" * 60)
    print("第1步: 生成皮肤资源文件")
    print("=" * 60)

    skin_dir = "NES-AB.deltaskin"

    # 确保目录存在
    if not os.path.exists(skin_dir):
        os.makedirs(skin_dir)
        print(f"  创建目录: {skin_dir}")

    # 生成PNG文件 - 标准分辨率
    create_transparent_png(393, 852, f"{skin_dir}/portrait.png")
    create_transparent_png(852, 393, f"{skin_dir}/landscape.png")

    # 生成PNG文件 - 高分辨率 (@2x)
    create_transparent_png(786, 1704, f"{skin_dir}/portrait@2x.png")
    create_transparent_png(1704, 786, f"{skin_dir}/landscape@2x.png")

    print("\n  ✓ 所有资源文件生成完成")
    print(f"  - 竖屏: portrait.png (393x852), portrait@2x.png (786x1704)")
    print(f"  - 横屏: landscape.png (852x393), landscape@2x.png (1704x786)")
    print(f"  - 配置: info.json (已存在)")

def package_skin():
    """打包皮肤文件为.deltaskin"""
    print("\n" + "=" * 60)
    print("第2步: 打包皮肤文件")
    print("=" * 60)

    skin_dir = "NES-AB.deltaskin"
    output_zip = "NES-AB-iPhone15Pro.zip"
    output_deltaskin = "NES-AB-iPhone15Pro.deltaskin"

    # 检查必需文件
    required_files = [
        f"{skin_dir}/info.json",
        f"{skin_dir}/portrait.png",
        f"{skin_dir}/landscape.png",
        f"{skin_dir}/portrait@2x.png",
        f"{skin_dir}/landscape@2x.png"
    ]

    missing_files = [f for f in required_files if not os.path.exists(f)]
    if missing_files:
        print(f"\n  ❌ 错误: 缺少必需文件:")
        for f in missing_files:
            print(f"     - {f}")
        return False

    # 创建ZIP文件
    print(f"\n  正在打包...")
    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(skin_dir):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, skin_dir)
                zipf.write(file_path, arcname)
                print(f"    + {arcname}")

    # 重命名为.deltaskin
    if os.path.exists(output_deltaskin):
        os.remove(output_deltaskin)
    os.rename(output_zip, output_deltaskin)

    # 获取文件大小
    file_size = os.path.getsize(output_deltaskin)
    size_kb = file_size / 1024

    print(f"\n  ✓ 打包完成: {output_deltaskin} ({size_kb:.1f} KB)")

    return True

def print_installation_guide():
    """打印安装说明"""
    print("\n" + "=" * 60)
    print("安装说明")
    print("=" * 60)
    print("""
📱 如何安装到 iPhone 15 Pro:

1. 将 NES-AB-iPhone15Pro.deltaskin 发送到你的 iPhone
   - 使用 AirDrop (推荐)
   - 或通过 iCloud Drive / 文件 App

2. 在 iPhone 上点击该文件

3. 选择 "用 Delta 打开"

4. 在 Delta 中:
   - 进入设置 (Settings)
   - 选择控制器皮肤 (Controller Skin)
   - 选择 "NES with A+B Button"

✨ 功能特点:
  - 专为 iPhone 15 Pro 优化 (393x852 分辨率)
  - A+B 组合按钮 - 紫色按钮同时按下A和B
  - 透明背景 - 游戏画面完整显示
  - 支持竖屏和横屏

🎮 适合游戏:
  - 魂斗罗 (Contra) - 同时跳跃和射击
  - 双截龙 (Double Dragon) - 特殊攻击
  - 忍者龙剑传 (Ninja Gaiden) - 忍术技能
    """)

def main():
    """主函数"""
    print("\n" + "=" * 60)
    print("Delta NES 皮肤生成器 - iPhone 15 Pro 专版")
    print("=" * 60)
    print("\n适配设备: iPhone 15 Pro (393x852)")
    print("功能: 包含 A+B 组合按钮\n")

    # 生成资源文件
    generate_skin_assets()

    # 打包皮肤
    if package_skin():
        # 显示安装说明
        print_installation_guide()

        print("=" * 60)
        print("✅ 完成! 皮肤文件已准备就绪")
        print("=" * 60)
        print(f"\n📦 文件位置: NES-AB-iPhone15Pro.deltaskin")
        print("📲 现在可以将此文件发送到你的 iPhone 15 Pro 了!\n")
    else:
        print("\n❌ 打包失败，请检查错误信息")

if __name__ == "__main__":
    main()
