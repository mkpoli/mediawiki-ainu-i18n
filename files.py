import os
import yaml

from pathlib import Path
from dotenv import load_dotenv
from convert import DIST_DIR  # Assuming this is the correct import for DIST_DIR

load_dotenv()

FTP_SERVER_MEDIAWIKI_DIR = os.getenv("FTP_SERVER_MEDIAWIKI_DIR")
LOCAL_DIR = os.getenv("LOCAL_DIR")
TARGET_LANGUAGES = (os.getenv("TARGET_LANGUAGES") or "").split(",")

if not FTP_SERVER_MEDIAWIKI_DIR or not LOCAL_DIR or not TARGET_LANGUAGES:
    raise ValueError("Missing environment variables")


def find_nested_files_by_metadata(
    local_dir: Path, remote_dir: Path
) -> dict[Path, Path]:
    upload_map: dict[Path, Path] = {}

    if local_dir.is_dir() and "metadata.yml" in [
        file.name for file in local_dir.glob("*")
    ]:
        with open(local_dir / "metadata.yml", "r") as f:
            metadata = yaml.safe_load(f)  # safer alternative with safe_load

        for source_dir, target_dir in metadata.get("directories", {}).items():
            source_path = local_dir / source_dir
            target_path = remote_dir / target_dir

            for lang in TARGET_LANGUAGES:
                source_file = (source_path / f"{lang}.json").resolve()
                if source_file.is_file():
                    upload_map[source_file] = target_path / source_file.name

        for source_file, target_file in metadata.get("files", {}).items():
            source_path = (local_dir / source_file).resolve()
            target_path = remote_dir / target_file

            upload_map[source_path] = target_path

    return upload_map


def generate_upload_map(local_dir: str, remote_dir: str) -> dict[Path, Path]:
    upload_map: dict[Path, Path] = {}

    remote_i18n_dir = Path(remote_dir, "languages", "i18n")

    # Translations
    for lang in TARGET_LANGUAGES:
        local_path = Path(local_dir, f"{lang}.json").resolve()
        if not os.path.isfile(local_path):
            raise FileNotFoundError(f"File not found: {local_path}")
        remote_path = remote_i18n_dir / f"{lang}.json"
        upload_map[local_path] = remote_path

    remote_messages_dir = Path(remote_dir, "languages", "messages")

    # Upload Messages
    for lang in TARGET_LANGUAGES:
        messages_dir = Path(local_dir, "messages")

        for file in messages_dir.glob(f"Messages{lang.title()}*.php"):
            remote_path = remote_messages_dir / file.name
            upload_map[file.resolve()] = remote_path

    # Conversion results
    for file in DIST_DIR.glob("*.json"):
        file_path = file.resolve()
        upload_map[file_path] = remote_i18n_dir / file.name

    # Extension translations
    local_extensions_dir = Path(local_dir, "extensions")
    remote_extensions_dir = Path(remote_dir, "extensions")

    for extension_dir in local_extensions_dir.glob("*"):
        upload_map |= find_nested_files_by_metadata(
            extension_dir, remote_extensions_dir / extension_dir.name
        )

    # Skin translations
    local_skins_dir = Path(local_dir, "skins")
    remote_skins_dir = Path(remote_dir, "skins")

    for skin_dir in local_skins_dir.glob("*"):
        upload_map |= find_nested_files_by_metadata(
            skin_dir, remote_skins_dir / skin_dir.name
        )

    # Upload Names.php
    local_names_php = Path(local_dir, "Names.php").resolve()
    remote_names_php = Path(remote_dir, "includes", "languages", "data", "Names.php")
    upload_map[local_names_php] = remote_names_php

    # Upload converter
    local_converter_dir = Path(local_dir, "converter")
    remote_converter_dir = Path(remote_dir)

    upload_map |= find_nested_files_by_metadata(
        local_converter_dir, remote_converter_dir
    )

    return upload_map


def get_relative_local_path(path: Path) -> Path:
    if not LOCAL_DIR:
        raise ValueError("LOCAL_DIR not set")
    return path.relative_to(Path(LOCAL_DIR).resolve())


def get_relative_remote_path(path: Path) -> Path:
    if not FTP_SERVER_MEDIAWIKI_DIR:
        raise ValueError("FTP_SERVER_MEDIAWIKI_DIR not set")
    return path.relative_to(Path(FTP_SERVER_MEDIAWIKI_DIR))


def main():
    resolved_local_dir = Path(LOCAL_DIR).resolve()

    print("LOCAL_BASE_DIR:", Path(LOCAL_DIR).absolute())
    print("REMOTE_BASE_DIR:", FTP_SERVER_MEDIAWIKI_DIR)
    print()

    file_map = generate_upload_map(LOCAL_DIR, FTP_SERVER_MEDIAWIKI_DIR)
    for local, remote in file_map.items():
        relative_local_path = local.relative_to(resolved_local_dir)
        relative_remote_path = remote.relative_to(FTP_SERVER_MEDIAWIKI_DIR)

        print(f"{relative_local_path}\n  -> {relative_remote_path}")


if __name__ == "__main__":
    main()
