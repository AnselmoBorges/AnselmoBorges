"""Atualiza somente o bloco de vídeos do perfil a partir do feed público da Rescue Point."""

from datetime import datetime
from html import escape
from pathlib import Path
import re
from urllib.request import Request, urlopen
from xml.etree import ElementTree

CHANNEL_ID = "UC18rVtiPZXg-PBAazAkJDew"
FEED_URL = f"https://www.youtube.com/feeds/videos.xml?channel_id={CHANNEL_ID}"
ATOM = "{http://www.w3.org/2005/Atom}"
YT = "{http://www.youtube.com/xml/schemas/2015}"
START = "<!-- YOUTUBE:START -->"
END = "<!-- YOUTUBE:END -->"
README = Path(__file__).resolve().parents[1] / "README.md"


def videos_from_feed(payload: bytes) -> list[str]:
    root = ElementTree.fromstring(payload)
    if root.findtext(f"{YT}channelId") != CHANNEL_ID:
        raise ValueError("O feed não corresponde ao canal Rescue Point")

    entries = []
    for entry in root.findall(f"{ATOM}entry"):
        video_id = entry.findtext(f"{YT}videoId", "")
        title = entry.findtext(f"{ATOM}title", "")
        published = entry.findtext(f"{ATOM}published", "")
        if not re.fullmatch(r"[A-Za-z0-9_-]{11}", video_id) or not title or not published:
            continue
        date = datetime.fromisoformat(published.replace("Z", "+00:00"))
        # O título vem de uma fonte externa: neutralizar HTML e Markdown antes de publicar.
        safe_title = escape(" ".join(title.split()), quote=False)
        safe_title = re.sub(r"([\\`*_[\]()!|])", r"\\\1", safe_title)
        entries.append((date, f"- [{safe_title}](https://www.youtube.com/watch?v={video_id}) · {date:%d/%m/%Y}"))

    if not entries:
        raise ValueError("O feed não contém vídeos válidos; README preservado")
    entries.sort(reverse=True)
    return [line for _, line in entries[:3]]


def replace_video_block(readme: str, lines: list[str]) -> str:
    if readme.count(START) != 1 or readme.count(END) != 1:
        raise ValueError("Marcadores de vídeos ausentes ou duplicados")
    left, rest = readme.split(START, 1)
    _, right = rest.split(END, 1)
    return left + START + "\n" + "\n".join(lines) + "\n" + END + right


def main() -> None:
    request = Request(FEED_URL, headers={"User-Agent": "RescuePoint-GitHub-Profile/1.0"})
    with urlopen(request, timeout=20) as response:
        payload = response.read(2_000_001)
    if len(payload) > 2_000_000:
        raise ValueError("Feed maior que o limite esperado")
    original = README.read_text(encoding="utf-8")
    updated = replace_video_block(original, videos_from_feed(payload))
    if updated != original:
        README.write_text(updated, encoding="utf-8")
        print("Lista de vídeos atualizada")
    else:
        print("Lista de vídeos já está atualizada")


if __name__ == "__main__":
    main()
