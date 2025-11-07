#!/usr/bin/env python3
"""
Delta NES Skin PDF Generator
为 Delta NES 皮肤生成带有按钮视觉效果的 PDF 文件
"""

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

def draw_button(c, x, y, width, height, label, color, text_color=colors.white):
    """绘制一个按钮"""
    # 绘制按钮背景
    c.setFillColor(color)
    c.roundRect(x, y, width, height, 5, fill=1, stroke=0)

    # 绘制按钮边框
    c.setStrokeColor(colors.HexColor('#333333'))
    c.setLineWidth(2)
    c.roundRect(x, y, width, height, 5, fill=0, stroke=1)

    # 添加按钮文字
    c.setFillColor(text_color)
    c.setFont("Helvetica-Bold", min(width, height) * 0.4)
    text_width = c.stringWidth(label, "Helvetica-Bold", min(width, height) * 0.4)
    text_x = x + (width - text_width) / 2
    text_y = y + height / 2 - min(width, height) * 0.15
    c.drawString(text_x, text_y, label)

def draw_dpad(c, x, y, size):
    """绘制方向键（D-Pad）"""
    # D-Pad 中心
    center_x = x + size / 2
    center_y = y + size / 2
    arm_width = size * 0.35
    arm_length = size * 0.45

    # 绘制 D-Pad 背景
    c.setFillColor(colors.HexColor('#444444'))

    # 上
    c.rect(center_x - arm_width / 2, center_y, arm_width, arm_length, fill=1, stroke=0)
    # 下
    c.rect(center_x - arm_width / 2, center_y - arm_length, arm_width, arm_length, fill=1, stroke=0)
    # 左
    c.rect(center_x - arm_length, center_y - arm_width / 2, arm_length, arm_width, fill=1, stroke=0)
    # 右
    c.rect(center_x, center_y - arm_width / 2, arm_length, arm_width, fill=1, stroke=0)

    # 中心圆
    c.circle(center_x, center_y, arm_width / 2, fill=1, stroke=0)

    # 绘制边框
    c.setStrokeColor(colors.HexColor('#333333'))
    c.setLineWidth(2)
    c.rect(center_x - arm_width / 2, center_y, arm_width, arm_length, fill=0, stroke=1)
    c.rect(center_x - arm_width / 2, center_y - arm_length, arm_width, arm_length, fill=0, stroke=1)
    c.rect(center_x - arm_length, center_y - arm_width / 2, arm_length, arm_width, fill=0, stroke=1)
    c.rect(center_x, center_y - arm_width / 2, arm_length, arm_width, fill=0, stroke=1)

    # 添加方向标签
    c.setFillColor(colors.white)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(center_x - 5, center_y + arm_length * 0.6, "↑")
    c.drawString(center_x - 5, center_y - arm_length * 0.8, "↓")
    c.drawString(center_x - arm_length * 0.7, center_y - 5, "←")
    c.drawString(center_x + arm_length * 0.4, center_y - 5, "→")

def generate_portrait_pdf(output_file):
    """生成竖屏 PDF"""
    print(f"正在生成竖屏布局: {output_file}")

    # 创建 PDF (375x812 points)
    c = canvas.Canvas(output_file, pagesize=(375, 812))

    # 设置背景色
    c.setFillColor(colors.HexColor('#2C2C2C'))
    c.rect(0, 0, 375, 812, fill=1, stroke=0)

    # 标题
    c.setFillColor(colors.white)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(375/2 - 80, 812 - 40, "Delta NES - Portrait")

    # 绘制方向键 (45, 520, 100x100) - 需要翻转Y坐标
    draw_dpad(c, 45, 812 - 520 - 100, 100)

    # 绘制 A 按钮 (313, 540, 47x47)
    draw_button(c, 313, 812 - 540 - 47, 47, 47, "A", colors.HexColor('#E74C3C'))

    # 绘制 B 按钮 (250, 560, 47x47)
    draw_button(c, 250, 812 - 560 - 47, 47, 47, "B", colors.HexColor('#E67E22'))

    # 绘制 A+B 组合按钮 (280, 485, 52x52) - 特殊颜色
    draw_button(c, 280, 812 - 485 - 52, 52, 52, "A+B", colors.HexColor('#9B59B6'))

    # 绘制 Select 按钮 (135, 650, 35x22)
    draw_button(c, 135, 812 - 650 - 22, 35, 22, "SEL", colors.HexColor('#7F8C8D'))

    # 绘制 Start 按钮 (190, 650, 35x22)
    draw_button(c, 190, 812 - 650 - 22, 35, 22, "STA", colors.HexColor('#7F8C8D'))

    # 绘制 Menu 按钮 (10, 10, 32x32)
    draw_button(c, 10, 812 - 10 - 32, 32, 32, "☰", colors.HexColor('#3498DB'))

    # 添加说明文字
    c.setFont("Helvetica", 10)
    c.setFillColor(colors.HexColor('#95A5A6'))
    c.drawString(20, 50, "NES Controller Skin with A+B Combo Button")
    c.drawString(20, 35, "紫色按钮为 A+B 组合键")

    c.save()
    print(f"✓ 竖屏 PDF 生成完成")

def generate_landscape_pdf(output_file):
    """生成横屏 PDF"""
    print(f"正在生成横屏布局: {output_file}")

    # 创建 PDF (812x375 points)
    c = canvas.Canvas(output_file, pagesize=(812, 375))

    # 设置背景色
    c.setFillColor(colors.HexColor('#2C2C2C'))
    c.rect(0, 0, 812, 375, fill=1, stroke=0)

    # 标题
    c.setFillColor(colors.white)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(812/2 - 85, 375 - 40, "Delta NES - Landscape")

    # 绘制方向键 (65, 110, 120x120)
    draw_dpad(c, 65, 375 - 110 - 120, 120)

    # 绘制 A 按钮 (675, 140, 55x55)
    draw_button(c, 675, 375 - 140 - 55, 55, 55, "A", colors.HexColor('#E74C3C'))

    # 绘制 B 按钮 (600, 165, 55x55)
    draw_button(c, 600, 375 - 165 - 55, 55, 55, "B", colors.HexColor('#E67E22'))

    # 绘制 A+B 组合按钮 (635, 95, 58x58) - 特殊颜色
    draw_button(c, 635, 375 - 95 - 58, 58, 58, "A+B", colors.HexColor('#9B59B6'))

    # 绘制 Select 按钮 (330, 220, 40x25)
    draw_button(c, 330, 375 - 220 - 25, 40, 25, "SEL", colors.HexColor('#7F8C8D'))

    # 绘制 Start 按钮 (395, 220, 40x25)
    draw_button(c, 395, 375 - 220 - 25, 40, 25, "STA", colors.HexColor('#7F8C8D'))

    # 绘制 Menu 按钮 (10, 10, 35x35)
    draw_button(c, 10, 375 - 10 - 35, 35, 35, "☰", colors.HexColor('#3498DB'))

    # 添加说明文字
    c.setFont("Helvetica", 10)
    c.setFillColor(colors.HexColor('#95A5A6'))
    c.drawString(20, 35, "NES Controller Skin with A+B Combo Button | 紫色按钮为 A+B 组合键")

    c.save()
    print(f"✓ 横屏 PDF 生成完成")

def main():
    """主函数"""
    print("=" * 60)
    print("Delta NES 皮肤 PDF 生成器")
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
    print("\n按钮说明:")
    print("  - 红色 (A): A 按钮")
    print("  - 橙色 (B): B 按钮")
    print("  - 紫色 (A+B): 组合按钮 - 同时按下 A 和 B")
    print("  - 灰色 (SEL/STA): Select 和 Start 按钮")
    print("  - 蓝色 (☰): Delta 菜单按钮")
    print("  - 深灰色: 方向键")

if __name__ == "__main__":
    main()
