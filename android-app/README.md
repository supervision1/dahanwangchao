# DreamPulse Android APK（离线版）

## 一键打包 APK

```bash
bash scripts/build_android_apk.sh
```

产物：`dist/dreampulse-preview-debug.apk`

## 离线运行说明
- 当前 APK 内置了 `assets/index.html`、`styles.css`、`app.js`。
- 安装后无需联网即可打开预览页面。

## 环境要求
- 已安装 Android SDK（默认路径：`$HOME/android-sdk`）
- 已安装 Gradle 8.x（脚本通过 `gradle -p android-app assembleDebug` 构建）
- 若使用 `mise`，脚本会自动用 `java@17` 构建

## 安装到手机
1. 把 APK 发到安卓手机（微信文件传输、ADB、网盘均可）。
2. 在手机上打开 APK 并允许“安装未知来源应用”。
3. 安装后打开 `DreamPulse` 即可。
