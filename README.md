# Delta NES 皮肤 - 带A+B组合按钮

这是一个为 Delta 模拟器定制的 NES 皮肤，增加了 **A+B 组合按钮**，可以同时按下 A 和 B 键。

## 功能特点

- **标准 NES 按钮**：包含所有经典 NES 控制器按钮（十字方向键、A、B、Select、Start）
- **A+B 组合按钮**：一个专门的按钮可以同时按下 A 和 B，非常适合以下游戏：
  - 魂斗罗（Contra）- 同时射击和跳跃
  - 双截龙（Double Dragon）- 特殊攻击
  - 忍者龙剑传（Ninja Gaiden）- 特殊技能
  - 其他需要同时按 A+B 的游戏
- **竖屏和横屏支持**：包含 portrait（竖屏）和 landscape（横屏）两种布局
- **全面屏设备优化**：包含 edgeToEdge 配置，适配刘海屏和全面屏设备

## 按钮布局

### 竖屏模式（Portrait）
- **左侧**：十字方向键（D-Pad）
- **右侧上方**：A+B 组合按钮
- **右侧中间**：A 按钮
- **右侧下方**：B 按钮
- **底部中央**：Select 和 Start 按钮
- **左上角**：菜单按钮

### 横屏模式（Landscape）
- 类似的布局，针对横屏显示优化
- A+B 组合按钮位于 A 和 B 按钮上方

## 安装方法

### 方法一：使用配置文件

1. 克隆或下载此仓库
2. 在 Delta 模拟器中，进入设置 > 控制器皮肤
3. 导入 `NES-AB.deltaskin` 文件夹

### 方法二：创建 .deltaskin 文件

1. 将 `NES-AB.deltaskin` 文件夹压缩为 ZIP 文件
2. 将扩展名从 `.zip` 改为 `.deltaskin`
3. 在 iOS 设备上使用 AirDrop 或文件管理器将文件传输到设备
4. 使用 Delta 打开 `.deltaskin` 文件

**注意**：此皮肤配置需要您自己创建对应的 PDF 布局文件（`portrait.pdf` 和 `landscape.pdf`），或者使用 Delta 的标准 NES 皮肤作为基础。

## 文件结构

```
NES-AB.deltaskin/
├── info.json              # 皮肤配置文件（包含所有按钮定义和布局）
├── portrait.pdf           # 竖屏布局图像（需要自行创建）
└── landscape.pdf          # 横屏布局图像（需要自行创建）
```

## info.json 配置说明

### A+B 组合按钮配置

组合按钮的关键配置在 `inputs` 数组中：

```json
{
  "inputs": ["a", "b"],
  "frame": {
    "x": 280,
    "y": 485,
    "width": 52,
    "height": 52
  },
  "extendedEdges": {
    "top": 8,
    "bottom": 8,
    "left": 8,
    "right": 8
  }
}
```

- **inputs**: `["a", "b"]` - 定义同时按下 A 和 B 键
- **frame**: 按钮的位置和大小
- **extendedEdges**: 扩展点击区域，提高触控体验

### 支持的设备配置

- **standard**: 标准屏幕设备（iPhone 8, iPhone SE 等）
- **edgeToEdge**: 全面屏设备（iPhone X 及更新机型）

每种配置都包含竖屏和横屏两种方向。

## 自定义

您可以根据需要调整按钮位置：

1. 在 `info.json` 中修改 `frame` 属性来调整按钮位置
2. 设置 `"debug": true` 可以在 Delta 中显示按钮边界，方便调试
3. 使用图形设计软件（如 Sketch、Figma）创建自定义的 PDF 布局文件

### 调试模式

在 `info.json` 顶部设置：
```json
{
  "debug": true,
  ...
}
```

这将在 Delta 中用红色方框显示所有按钮的位置，便于调整布局。

## 技术细节

- **坐标系统**：使用点（points）而非像素，确保跨设备兼容性
- **原点位置**：左上角为 (0, 0)
- **mappingSize**：定义布局的基准尺寸
  - Portrait: 375 x 812（iPhone X 尺寸）
  - Landscape: 812 x 375

## 兼容游戏推荐

以下 NES 游戏特别适合使用 A+B 组合按钮：

- 魂斗罗（Contra）
- 双截龙（Double Dragon）
- 忍者龙剑传（Ninja Gaiden）
- 热血系列游戏
- 超级马里奥兄弟 3（某些特殊技巧）

## 参考资源

- [Delta 官方文档](https://noah978.gitbook.io/delta-docs/)
- [Delta 皮肤制作指南](https://noah978.gitbook.io/delta-docs/skins)
- [Delta Skins 社区](https://github.com/delta-skins/delta-skins.github.io)
- [DeltaCore Wiki](https://github.com/rileytestut/DeltaCore/wiki/Skins)

## 许可证

本项目使用 MIT 许可证。

## 贡献

欢迎提交 Issue 和 Pull Request 来改进这个皮肤！

## 更新日志

- **v1.0.0** (2025-11-07)
  - 初始版本
  - 添加 A+B 组合按钮
  - 支持竖屏和横屏
  - 支持标准和全面屏设备