# 安装指南

## 快速安装步骤

### 在 iOS 设备上安装

1. **下载皮肤文件**
   - 从 GitHub 下载 `NES-AB.deltaskin.zip` 文件

2. **重命名文件**
   - 将文件从 `NES-AB.deltaskin.zip` 重命名为 `NES-AB.deltaskin`
   - 注意：直接改扩展名即可，不需要解压

3. **传输到设备**
   - 使用 AirDrop 发送到 iPhone/iPad
   - 或者通过 iCloud Drive、文件 App 等方式传输

4. **安装皮肤**
   - 在 iOS 设备上找到 `NES-AB.deltaskin` 文件
   - 点击文件，选择"用 Delta 打开"
   - Delta 会自动安装皮肤

5. **启用皮肤**
   - 打开 Delta 应用
   - 进入 **设置 (Settings)**
   - 选择 **控制器皮肤 (Controller Skin)**
   - 选择 **NES with A+B Button**

## 使用说明

### 按钮布局

#### 竖屏模式
```
                 [☰ Menu]


    [D-Pad]                      [A+B]
      ←↑→
      ↓                        [A]  [B]



            [Select] [Start]
```

#### 横屏模式
```
   [☰]
                                              [A+B]
                                           [A]  [B]
   [D-Pad]        [Select] [Start]
    ←↑→
     ↓
```

### 按钮功能

- **D-Pad**: 方向控制（上下左右）
- **A**: 主要动作按钮（红色）
- **B**: 次要动作按钮（橙色）
- **A+B**: 组合按钮（紫色）- **同时按下 A 和 B**
- **Select**: 选择按钮
- **Start**: 开始按钮
- **☰ Menu**: Delta 菜单按钮

### 适合使用 A+B 组合的游戏

1. **魂斗罗 (Contra)**
   - A+B 可以同时跳跃和射击
   - 在空中更灵活地消灭敌人

2. **双截龙 (Double Dragon)**
   - A+B 触发特殊攻击
   - 更强大的连击技能

3. **忍者龙剑传 (Ninja Gaiden)**
   - A+B 使用忍术技能
   - 关键时刻的特殊技能

4. **热血系列游戏**
   - 各种组合技能
   - 超必杀技

## 故障排除

### 问题：皮肤无法安装

**解决方法**：
- 确保文件扩展名是 `.deltaskin` 而不是 `.zip`
- 确保您使用的是最新版本的 Delta
- 尝试重新下载文件

### 问题：按钮位置不准确

**解决方法**：
- 在 Delta 设置中调整控制器的不透明度
- 尝试重新校准触摸位置
- 如果需要，可以在 `info.json` 中启用 `"debug": true` 查看按钮边界

### 问题：A+B 按钮不工作

**解决方法**：
- 确保游戏支持同时按下 A 和 B
- 尝试在 Delta 设置中调整按钮灵敏度
- 某些游戏可能需要特定的按键组合顺序

## 自定义

如果您想自定义皮肤：

1. **克隆仓库**
   ```bash
   git clone https://github.com/yourusername/delta-nes-aandb.git
   cd delta-nes-aandb
   ```

2. **修改配置**
   - 编辑 `NES-AB.deltaskin/info.json` 调整按钮位置
   - 修改 `generate_skin_pdfs.py` 更改按钮外观

3. **重新生成 PDF**
   ```bash
   python3 generate_skin_pdfs.py
   ```

4. **打包皮肤**
   ```bash
   cd NES-AB.deltaskin
   zip -r ../NES-AB.deltaskin.zip .
   cd ..
   ```

5. **重命名并安装**
   - 将 `.zip` 改为 `.deltaskin`
   - 按照上述安装步骤安装

## 需要帮助？

如果遇到问题，请：
- 查看 [README.md](README.md) 获取更多信息
- 在 GitHub 上提交 Issue
- 参考 [Delta 官方文档](https://noah978.gitbook.io/delta-docs/)

## 祝您游戏愉快！

享受带有 A+B 组合按钮的 Delta NES 体验！
