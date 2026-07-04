# VK虚拟键值转换器

一个用于Windows虚拟键值(VK)双向转换的GUI工具。

## 功能

### 单键转换
- **VK名称 → 十六进制/十进制**: 输入如 `VK_RETURN` 或 `RETURN`
- **十六进制 → VK名称**: 输入如 `0x0D`
- **十进制 → VK名称**: 输入如 `13`
- **模糊搜索**: 支持按名称、描述搜索
- **浏览列表**: 显示所有VK键值，支持实时过滤

### 按键序列解析
支持解析特殊格式的按键序列，例如：
```
[Pasted ~4 linecmd[ENTER]
[CTRL_L]pyinstaller [ENTER]
[↑]-h[ENTER]
```

支持的别名包括：
| 别名 | VK名称 | 说明 |
|------|--------|------|
| `ENTER` / `RETURN` | VK_RETURN | 回车键 |
| `TAB` | VK_TAB | Tab键 |
| `ESC` / `ESCAPE` | VK_ESCAPE | Esc键 |
| `SPACE` | VK_SPACE | 空格键 |
| `BACKSPACE` / `BKSP` | VK_BACK | 退格键 |
| `DELETE` / `DEL` | VK_DELETE | 删除键 |
| `CTRL` / `CTRL_L` / `CTRL_R` | VK_CONTROL | Ctrl键 |
| `SHIFT` / `SHIFT_L` / `SHIFT_R` | VK_SHIFT | Shift键 |
| `ALT` / `ALT_L` / `ALT_R` | VK_MENU | Alt键 |
| `WIN` / `WIN_L` / `WIN_R` | VK_LWIN | Windows键 |
| `↑` `↓` `←` `→` | VK_UP/DOWN/LEFT/RIGHT | 方向键 |
| `F1` ~ `F12` | VK_F1 ~ VK_F12 | 功能键 |
| `CAPSLOCK` / `CAPS` | VK_CAPITAL | 大写锁定 |
| `NUMLOCK` | VK_NUMLOCK | 数字锁定 |
| `PRINTSCREEN` / `PRTSC` | VK_SNAPSHOT | 截屏键 |
| `PAUSE` / `BREAK` | VK_PAUSE | 暂停键 |

## 使用方法

```bash
python VK转换器.py
```

## 界面说明

### 单键转换标签页
1. **输入框**: 输入VK名称、十六进制值或十进制值，按回车转换
2. **结果区域**: 显示转换结果（VK名称、十六进制、十进制、描述）
3. **搜索框**: 过滤下方列表
4. **列表**: 点击选择条目自动填入输入框

### 按键序列解析标签页
1. **输入区**: 粘贴按键序列数据
2. **解析按钮**: 执行解析
3. **结果表格**: 显示每个按键的详细信息

## 示例

### 单键转换
| 输入 | 结果 |
|------|------|
| `VK_RETURN` | 0x0D (13) - 输入键 |
| `0x1B` | VK_ESCAPE - Esc键 |
| `27` | VK_ESCAPE (0x1B) - Esc键 |

### 按键序列
输入：
```
[CTRL_L]pyinstaller [ENTER]
```
解析结果：
| # | 类型 | 输入 | VK名称 | 十六进制 | 描述 |
|---|------|------|--------|----------|------|
| 1 | 按键 | CTRL_L | VK_LCONTROL | 0xA2 | 左Ctrl键 |
| 2 | 文本 | pyinstaller | - | - | - |
| 3 | 按键 | ENTER | VK_RETURN | 0x0D | 输入键 |

## 依赖

- Python 3.x
- tkinter (Python内置)