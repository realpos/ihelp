import argparse
from pathlib import Path
import textwrap

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError as e:
    raise SystemExit('Pillow is required. Install with "pip install pillow"') from e


FIELDS = [
    ("child_name", "아이 이름"),
    ("birth_date", "생년월일"),
    ("blood_type", "혈액형"),
    ("diseases", "지병"),
    ("allergies", "알러지"),
    ("special_notes", "특이사항"),
    ("parent_contact", "부모 연락처"),
    ("emergency_contact", "긴급 연락처"),
]

def parse_args():
    p = argparse.ArgumentParser(description="아이구해줘 카드 생성기")
    p.add_argument("input_file", type=Path, help="YAML 또는 JSON 입력 파일")
    p.add_argument("--output", "-o", type=Path, default=Path("card.png"), help="출력 이미지 경로")
    return p.parse_args()


def load_data(path: Path):
    if path.suffix.lower() in {".yaml", ".yml"}:
        import yaml
        with path.open("r", encoding="utf-8") as f:
            return yaml.safe_load(f)
    else:
        import json
        with path.open("r", encoding="utf-8") as f:
            return json.load(f)


def create_card(data: dict, output: Path):
    width, height = 600, 400
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()
    line_height = 20

    margin = 20
    y = margin
    for key, label in FIELDS:
        if key not in data:
            continue
        value = data[key]
        if isinstance(value, list):
            value = ", ".join(str(v) for v in value)
        text = f"{label}: {value}"
        wrapped = textwrap.fill(text, width=40)
        draw.text((margin, y), wrapped, fill="black", font=font)
        y += line_height * (wrapped.count("\n") + 1)
        y += 5
    image.save(output)


def main():
    args = parse_args()
    data = load_data(args.input_file)
    create_card(data, args.output)
    print(f"Saved card to {args.output}")


if __name__ == "__main__":
    main()
