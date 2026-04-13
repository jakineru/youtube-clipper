# 🎬 YouTube Clipper

A Python-based tool to download YouTube clips (`/clip/`) directly as `.mp4` files, quickly, easily, and without downloading the entire video.

---

## 🚀 Features

- ⚡ Downloads only the clip
- 🎯 Precise cutting
- 📁 Exports directly to `.mp4`
- 🧠 Automatic naming if none is specified
---

## ▶️ Usage

```bash
python script.py
```
Or download the `.exe` at: https://github.com/jakineru/youtube-clipper/releases/tag/YouTubeClipper


## 📦 Requirements

You need to have the following installed:

- Python 3.8 or higher
- yt-dlp
- FFmpeg

---

## 🧰 Installation

### 1. Install Python

Download from:

https://www.python.org/downloads/

IMPORTANT: During installation, check "Add Python to PATH"

---

### 2. Install yt-dlp

Open the terminal (CMD or PowerShell) and run:

```bash
python3 -m pip install -U yt-dlp
```

---

### 3. Install FFmpeg

```bash
winget install -e --id Gyan.FFmpeg.Essentials
```

---

### 4. Add FFmpeg to the PATH

1. Search: "Environment Variables"
2. Edit the Path variable
3. Add: "C:\ffmpeg\bin"
4. Save changes

---

### 5. Verify installation

```bash
ffmpeg -version
```

If information appears → Ready

---


## 🏷️ Automatic naming

Format:

Video title [mm-ss-mm-ss].mp4

Example:

The best video in da world!!1 [01-05-01-09].mp4

---

## 🔒 Legal

Personal use. Respect copyright.

---

## ⭐ Credits

- yt-dlp
- FFmpeg
