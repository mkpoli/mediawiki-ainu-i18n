import ftplib
import json
import os

from dotenv import load_dotenv
from loguru import logger
from pathlib import Path

load_dotenv()

FTP_SERVER_HOST = os.getenv("FTP_SERVER_HOST")
FTP_SERVER_USER = os.getenv("FTP_SERVER_USER")
FTP_SERVER_PASS = os.getenv("FTP_SERVER_PASS")
FTP_SERVER_MEDIAWIKI_DIR = os.getenv("FTP_SERVER_MEDIAWIKI_DIR")
LOCAL_DIR = os.getenv("LOCAL_DIR")
TARGET_LANGUAGES = (os.getenv("TARGET_LANGUAGES") or "").split(",")

if (
    not FTP_SERVER_HOST
    or not FTP_SERVER_USER
    or not FTP_SERVER_PASS
    or not FTP_SERVER_MEDIAWIKI_DIR
    or not LOCAL_DIR
    or not TARGET_LANGUAGES
):
    raise ValueError("Missing environment variables")


REMOTE_I18N_DIR = Path(FTP_SERVER_MEDIAWIKI_DIR, "languages", "i18n")

LOCAL_EXTENSIONS_DIR = Path(LOCAL_DIR, "extensions")
REMOTE_EXTENSIONS_DIR = Path(FTP_SERVER_MEDIAWIKI_DIR, "extensions")


def main():
    ftp = ftplib.FTP(FTP_SERVER_HOST)
    ftp.login(FTP_SERVER_USER, FTP_SERVER_PASS)

    ftp.cwd(REMOTE_I18N_DIR.as_posix())

    # Upload translations
    for lang in TARGET_LANGUAGES:
        path = Path(LOCAL_DIR, f"{lang}.json")
        target = Path(REMOTE_I18N_DIR, f"{lang}.json")
        with open(path, "rb") as f:
            logger.info(f"Uploading '{path}' to '{target.as_posix()}'...")
            ftp.storbinary(f"STOR {lang}.json", fp=f)
        logger.info(f"Uploaded as '{target.as_posix()}'")

    # Upload extension translations
    for extension_dir in LOCAL_EXTENSIONS_DIR.glob("*"):
        if extension_dir.is_dir() and "metadata.json" in [
            file.name for file in extension_dir.glob("*")
        ]:
            logger.info(f"Found extension {extension_dir.name}")
            with open(extension_dir / "metadata.json", "r") as f:
                metadata = json.load(f)
                for source, target in metadata["files"].items():
                    source_path = extension_dir / source
                    target_path = REMOTE_EXTENSIONS_DIR / extension_dir.name / target
                    logger.info(
                        f"Uploading '{source_path}' to '{target_path.as_posix()}'..."
                    )

                    ftp.cwd("/")
                    ftp.cwd(target_path.parent.as_posix())

                    with open(source_path, "rb") as f:
                        ftp.storbinary(f"STOR {target_path.name}", fp=f)
                    logger.info(f"Uploaded as '{target_path.as_posix()}' ")

    ftp.quit()


if __name__ == "__main__":
    main()
