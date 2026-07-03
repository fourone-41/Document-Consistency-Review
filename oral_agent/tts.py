import asyncio
import tempfile

import edge_tts

VOICE = "en-US-JennyNeural"


def speak(text: str) -> str:
    """Synthesize English text to speech. Returns path to MP3 file."""
    async def _run() -> str:
        path = tempfile.mktemp(suffix=".mp3")
        await edge_tts.Communicate(text, VOICE).save(path)
        return path

    return asyncio.run(_run())
