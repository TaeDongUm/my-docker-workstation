from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "counter.txt"


def ensure_data_file():
    """counter.txt 파일이 없으면 생성하고 0으로 초기화한다."""
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    if not DATA_FILE.exists():
        DATA_FILE.write_text("0", encoding="utf-8")


def read_count():
    """현재 방문 횟수를 읽는다."""
    ensure_data_file()
    try:
        content = DATA_FILE.read_text(encoding="utf-8").strip()
        return int(content) if content else 0
    except ValueError:
        return 0


def increment_count():
    """방문 횟수를 1 증가시키고 저장한다."""
    count = read_count() + 1
    DATA_FILE.write_text(str(count), encoding="utf-8")
    return count