# ihelp

아이구해줘 서비스
-----------------

이 저장소는 어린이의 의료 및 긴급 상황 정보를 카드 형태로 정리해 주는 간단한 도구를 제공합니다. 원하는 항목을 입력한 후 이미지를 생성하여 출력하거나 별도의 카드 제작에 활용할 수 있습니다.

## 요구 사항

- Python 3.8 이상
- [Pillow](https://python-pillow.org) 및 [PyYAML](https://pyyaml.org) 패키지

```bash
pip install pillow pyyaml
```

## 사용 방법

1. `examples/sample_card.yml` 파일을 참고하여 자녀의 정보를 입력합니다.
2. 다음 명령으로 카드를 생성합니다.

```bash
python3 src/card_generator.py examples/sample_card.yml -o my_card.png
```

실행 후 `my_card.png` 파일이 생성됩니다. 필요에 따라 이미지 파일을 출력하거나 카드 제작에 활용할 수 있습니다.
