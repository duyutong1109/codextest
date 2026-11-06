# codextest

一个最小的 Python 示例，运行时输出 `Hello Codex`，并使用 pytest 验证输出。

## 安装

建议在虚拟环境中安装依赖：

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
python -m pip install -r requirements.txt
```

## 运行

```bash
python hello.py
```

预期输出：

```text
Hello Codex
```

## 测试

```bash
pytest
```
