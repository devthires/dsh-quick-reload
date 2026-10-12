# dsh-quick-reload

把 **F5** 绑定为刷新 DeepSeek Harness（DSH）Web 客户端，让**新装的 skill 和插件无需重启应用**即可生效。

## 要解决的问题

安装 skill 后，文件已经落盘、Host 侧也立刻识别了 —— 但 `/` 斜杠菜单在**整个页面生命周期内都使用缓存的技能目录**。这份缓存只在切换 agent preset 或连接重置时才失效，所以刚装好的 skill 在菜单里看不到，必须重启整个客户端。

DSH Desktop 本身没有内置刷新快捷键：外壳没有绑定任何刷新加速键（只绑了 <kbd>F12</kbd> 开 DevTools），也没有接上浏览器式的刷新。

## 作用

按 <kbd>F5</kbd> 重载渲染层，客户端会重建并重新拉取目录 —— 新 skill 立即出现。

只接管**普通 F5**。带修饰键的（<kbd>Ctrl</kbd>+<kbd>F5</kbd>、<kbd>Shift</kbd>+<kbd>F5</kbd> 等）**故意不管**。

## 环境要求

- 支持 profile 插件的 DSH Desktop。开发与验证环境：`dsh` 0.1.5-rc.1、`@deepseek-ai` 包 0.2.0-rc.2、Windows 11。

## 安装

### DSH Desktop

打开 **设置 → 插件 → 添加插件**，填入仓库地址：

```
https://github.com/devthires/dsh-quick-reload
```

或填入你本地克隆后的目录路径。

> `dsh plugin` CLI 会拒绝 `desktop` profile（提示 `profile "desktop" is managed exclusively by the Electron application`），所以在桌面端请用设置页安装。

### 自定义 profile 或 `web` profile

```bash
dsh plugin --profile web add github:devthires/dsh-quick-reload
```

## 使用

在窗口任意位置按 <kbd>F5</kbd>。
