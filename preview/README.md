# 预览界面

## 本地运行

```bash
python -m http.server 4173 -d preview
```

打开 `http://localhost:4173` 即可查看。

## 快速验证（可选）

```bash
curl -I http://localhost:4173
```

返回 `HTTP/1.0 200 OK` 代表静态预览已成功启动。
