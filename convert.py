import ainconv
import json
import regex as re

from tqdm import tqdm
from loguru import logger
from pathlib import Path

BASE_DIR = Path(__file__).parent

DIST_DIR = BASE_DIR / "dist"


def convert_word(text: str):
    for word in re.findall(r"[\p{scx=Latn}=]+", text):
        if all(char.isupper() for char in word):
            # SITENAME, etc. reserved words
            continue
        text = text.replace(word, ainconv.latn2kana(word.lower()))
    return text


def convert_sentence(text: str) -> str:
    # preprocess
    text = text.replace("or ta", "otta")
    text = text.replace("orta", "otta")

    return " ".join([convert_word(word) for word in text.split(" ")])


def convert_item(key: str, value: str) -> str:
    return convert_sentence(value) if key != "@metadata" else value


def main():
    logger.info("Converting ain.json to dist/ain.json")

    with open("ain.json", "r") as f:
        ain = json.load(f)

    converted = {key: convert_item(key, value) for key, value in tqdm(ain.items())}

    with open("dist/ain-kana.json", "w") as f:
        json.dump(converted, f, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    main()
