import ftplib
import os

from dotenv import load_dotenv
from loguru import logger
from pathlib import Path
from convert import main as convert_main
from files import generate_upload_map

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


def upload_file(ftp: ftplib.FTP, local_file: Path, remote_file: Path) -> None:
    """
    Uploads a single file to the FTP server.

    :param ftp: An active FTP connection object.
    :param local_file: Path to the local file to upload.
    :param remote_file: The target path on the FTP server.
    """
    remote_dir = Path(remote_file).parent
    ftp.cwd("/")
    ftp.cwd(remote_dir.as_posix())

    already_exists = remote_file.name in ftp.nlst()

    with open(local_file, "rb") as file:
        logger.info(f"Uploading '{local_file}' to '{remote_file}'...")
        ftp.storbinary(f"STOR {Path(remote_file).name}", file)
    logger.info(f"{'Overwritten' if already_exists else 'Created' } '{remote_file}'")


def main():
    # git pull
    os.system("git pull")

    # convert
    convert_main()

    # get files
    files = generate_upload_map(LOCAL_DIR, FTP_SERVER_MEDIAWIKI_DIR)

    with ftplib.FTP(FTP_SERVER_HOST) as ftp:
        ftp.login(FTP_SERVER_USER, FTP_SERVER_PASS)

        for local_file, remote_file in files.items():
            upload_file(ftp, local_file, remote_file)


if __name__ == "__main__":
    main()
