# dsh-quick-reload

Bind **F5** to reload the DeepSeek Harness (DSH) Web client, so newly installed
skills and plugins show up **without restarting the app**.

## The problem

When you install a skill, the files land on disk and the Host side picks them up
immediately — but the `/` slash menu keeps serving a **cached** skill catalog for
the lifetime of the page. That cache is only dropped when the agent preset
changes or the connection resets, so a freshly installed skill stays invisible in
the menu until the whole desktop app is restarted.

There is no reload shortcut built into DSH Desktop: the shell binds no reload
accelerator (only <kbd>F12</kbd> for DevTools), and a browser-style refresh is
not wired up.

## What it does

Pressing <kbd>F5</kbd> reloads the renderer, which rebuilds the client and
refetches the catalog — new skills appear right away.

Plain F5 only. Modified variants (<kbd>Ctrl</kbd>+<kbd>F5</kbd>,
<kbd>Shift</kbd>+<kbd>F5</kbd>, …) are deliberately left alone.

## Requirements

- DSH Desktop with profile plugin support. Developed and tested against
  `dsh` 0.1.5-rc.1 with `@deepseek-ai` packages `0.2.0-rc.2` on Windows 11.

## Install

### DSH Desktop

Open **Settings → Plugins → Add plugin** and give the repository address:

```
https://github.com/devthires/dsh-quick-reload
```

or a local directory path when you have cloned it.

> The `dsh plugin` CLI refuses the `desktop` profile
> (`profile "desktop" is managed exclusively by the Electron application`), so
> use the settings page there.

### Custom or `web` profile

```bash
dsh plugin --profile web add github:devthires/dsh-quick-reload
```

## Usage

Press <kbd>F5</kbd> anywhere in the window.
