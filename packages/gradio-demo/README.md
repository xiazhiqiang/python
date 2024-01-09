# gradio-demo

## 本地开发

- 初始化直接 poetry add gradio 报错，发现是 orjson 包问题，逐个版本尝试发现，orjson<=3.8.12 可以，定死这个版本
- 出现问题：https://github.com/python-pillow/Pillow/issues/6862

```sh
python3 -m pip install --force-reinstall Pillow==9.3.0
```

```text
# 原始环境安装的pillow@10.2.0
Found existing installation: pillow 10.2.0
    Uninstalling pillow-10.2.0:
      Successfully uninstalled pillow-10.2.0
```

- 启动 demo

```sh
poetry run python3 src/gradio_demo/demo.py
```

- 访问：http://127.0.0.1:7860/
