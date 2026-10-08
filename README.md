# MVA 多角度提示词生成器（中英双语版）

用于 ComfyUI 的无依赖自定义节点，组合 Qwen-Image-2.1 Multiple-Angles LoRA 的 `<mva>` 角度提示词。

## 安装

在终端进入 `ComfyUI/custom_nodes/`，执行：

```bash
git clone https://github.com/jlongk2005/comfyui-mva-prompt-builder.git
```

也可以在 GitHub 仓库页面点击 **Code → Download ZIP**，解压后将文件夹重命名为 `comfyui-mva-prompt-builder`，再放入 `ComfyUI/custom_nodes/`。请确保 `__init__.py` 和 `nodes.py` 直接位于该文件夹内。

重启 ComfyUI，在节点搜索中输入 `MVA`，添加 **MVA 多角度提示词生成器**。

## 使用

- `azimuth`：12 种方位，中文和英文同时显示，如 `正面 | front view`。
- `elevation`：4 种高度角，中文和英文同时显示，如 `平视 | eye-level shot`。
- `close_up`：是否追加 `close-up`。
- 输出 `prompt`：始终只使用作者的**原始英文 caption**，不包含中文。

例如：选择 `右侧面 | right side view`、`高角度俯拍 | high-angle shot`，启用特写，得到：

```text
<mva> right side view, high-angle shot close-up
```

可以将 STRING 输出连接至 CLIP Text Encode 的 `text` 输入（如有必要，在目标节点上右键将文本控件转换为输入）。更改控件会改变下一次执行的输出，不是免执行实时计算。

## 兼容与限制

- 不加载 LoRA，也不负责生图。
- 不需要第三方 Python 包、前端 JS 或 `requirements.txt`。
- 兼容旧版节点的纯英文输入值（在执行层）；但旧工作流可能需重新选择新版下拉框项目并保存。
- 参考：https://huggingface.co/akhaliq/Qwen-Image-2.1-Multiple-Angles-LoRA
