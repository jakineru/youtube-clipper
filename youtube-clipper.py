import yt_dlp
import subprocess
import shutil
import os
import webbrowser
import re
import sys

GITHUB_URL = "https://github.com/jakineru/youtube-clipper"
CLR = {
    "red": "\033[91m",
    "green": "\033[92m",
    "yellow": "\033[93m",
    "blue": "\033[94m",
    "cyan": "\033[96m",
    "reset": "\033[0m",
    "bold": "\033[1m"
}

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def title():
    print(f"{CLR['cyan']}=================================================={CLR['reset']}")
    print(f"      {CLR['bold']}🎬 YOUTUBE CLIPPER{CLR['reset']} {CLR['blue']}@jakineru{CLR['reset']}")
    print(f"{CLR['cyan']}=================================================={CLR['reset']}\n")

def check_dependencies():
    if not shutil.which("ffmpeg"):
        print(f"{CLR['red']}❌ Necesitas instalar ffmpeg...{CLR['reset']}")
        webbrowser.open(GITHUB_URL)
        input("[ENTER] para continuar...")
        return False

    try:
        import yt_dlp
    except ImportError:
        print(f"{CLR['red']}❌ Necesitas instalar yt-dlp...{CLR['reset']}")
        webbrowser.open(GITHUB_URL)
        input("[ENTER] para continuar...")
        return False

    return True

def clean_filename(name):
    return re.sub(r'[\\/*?:"<>|]', "", name).strip()

def format_time(seconds):
    m = int(seconds // 60)
    s = int(seconds % 60)
    return f"{m:02d}-{s:02d}"

def download_clip(url, filename_input):
    try:
        ydl_opts = {
            "quiet": True,
            "no_warnings": True,
            "format": "best[height<=720][ext=mp4]/best[height<=720]"
        }

        print(f"{CLR['blue']}   🔍 Analizando el clip...{CLR['reset']}")

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)

        stream = info.get("url")
        start = info.get("section_start", 0)
        end = info.get("section_end", info.get("duration", 0))
        title_video = info.get("title", "clip")

        if not filename_input:
            start_txt = format_time(start)
            end_txt = format_time(end)
            filename = f"{title_video} [{start_txt}-{end_txt}]"
        else:
            filename = filename_input

        filename = clean_filename(filename)
        output_file = filename + ".mp4"

        print(f"\n{CLR['green']}✅ Clip detectado:{CLR['reset']}")
        print(f"   ⏱  Tiempo: {round(start, 2)}s ➔ {round(end, 2)}s")
        print(f"   📁 Archivo: {output_file}")
        
        print(f"\n{CLR['yellow']}⚡ Descargando y procesando...{CLR['reset']}")
        print(f"{CLR['cyan']}   (Por favor, espera. FFmpeg está trabajando en segundo plano){CLR['reset']}")

        cmd = [
            "ffmpeg",
            "-loglevel", "error",
            "-ss", str(start),
            "-to", str(end),
            "-i", stream,
            "-c:v", "copy",
            "-c:a", "copy",
            "-y", 
            output_file
        ]

        subprocess.run(cmd)

        print(f"\n{CLR['green']}✨ ¡LISTO! El clip se ha guardado con éxito.{CLR['reset']}")

    except Exception as e:
        print(f"\n{CLR['red']}❌ Error: {e}{CLR['reset']}")

def main():
    while True:
        clear()
        title()

        if not check_dependencies():
            break

        print(f"{CLR['bold']}Datos:{CLR['reset']}")
        url = input(f" 🔗 {CLR['cyan']}URL del clip:{CLR['reset']} ").strip()
        
        if not url:
            print(f"\n{CLR['red']}❌ URL inválida{CLR['reset']}")
            input("[ENTER] para volver...")
            continue

        name = input(f" 📁 {CLR['cyan']}Nombre archivo (Enter para auto):{CLR['reset']} ").strip()

        download_clip(url, name)

        print(f"\n{CLR['cyan']}=================================================={CLR['reset']}")
        choice = input("¿Quieres descargar otro clip? (s/N): ").lower()
        if choice != 's':
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
