import os
import ftplib

from dotenv import load_dotenv
from loguru import logger
from pathlib import Path

load_dotenv()

FTP_SERVER_HOST = os.getenv("FTP_SERVER_HOST")
FTP_SERVER_USER = os.getenv("FTP_SERVER_USER")
FTP_SERVER_PASS = os.getenv("FTP_SERVER_PASS")
FTP_SERVER_TARGET_DIR = os.getenv("FTP_SERVER_TARGET_DIR")
LOCAL_DIR = os.getenv("LOCAL_DIR")
TARGET_LANGUAGES = (os.getenv("TARGET_LANGUAGES") or "").split(",")

if (
    not FTP_SERVER_HOST
    or not FTP_SERVER_USER
    or not FTP_SERVER_PASS
    or not FTP_SERVER_TARGET_DIR
    or not LOCAL_DIR
    or not TARGET_LANGUAGES
):
    raise ValueError("Missing environment variables")


# Put all LOCAL_DIR/TARGET_LANGUAGES[*].json files to FTP_SERVER_TARGET_DIR
def upload():
    ftp = ftplib.FTP(FTP_SERVER_HOST)
    ftp.login(FTP_SERVER_USER, FTP_SERVER_PASS)
    ftp.cwd(FTP_SERVER_TARGET_DIR)

    for lang in TARGET_LANGUAGES:
        path = Path(LOCAL_DIR, f"{lang}.json")
        target = Path(FTP_SERVER_TARGET_DIR, f"{lang}.json")
        with open(path, "rb") as f:
            logger.info(f"Uploading {path} to {target.as_posix()}...")
            ftp.storbinary(f"STOR {lang}.json", fp=f)
        logger.info(f"Uploaded {path} to {target.as_posix()}")

    ftp.quit()


def main():
    upload()


if __name__ == "__main__":
    main()
