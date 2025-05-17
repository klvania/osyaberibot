import subprocess
import sys

# インストールしたいパッケージ一覧
required_packages = [
    "discord.py",
    "aiohttp",  # 念のため明示
]

# pipでインストール
for package in required_packages:
    try:
        print(f"📦 Installing: {package}")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    except Exception as e:
        print(f"❌ Error installing {package}: {e}")
