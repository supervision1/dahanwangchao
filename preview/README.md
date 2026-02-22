# 预览界面

## 本地运行

```bash
python -m http.server 4173 -d preview
```

打开 `http://localhost:4173` 即可查看。

## 打包（给手机测试）

```bash
bash scripts/build_preview_package.sh
```

会生成：`dist/dreampulse-preview-mobile-test.zip`。

## 手机上测试（推荐）
1. 把 `preview/` 或 zip 解压后的文件部署到任意静态托管（如 GitHub Pages / Vercel / Netlify）。
2. 手机浏览器打开页面。
3. 在浏览器菜单中选择「添加到主屏幕」，即可按 App 方式打开（PWA）。

## 快速验证（可选）

```bash
curl -I http://localhost:4173
```

返回 `HTTP/1.0 200 OK` 代表静态预览已成功启动。
