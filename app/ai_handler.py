"""Mock AI handler for Twilio demo.

Provides a simple function `mock_ai_response` which simulates generating text and TTS URLs.
This keeps the demo offline and deterministic for tests.
"""

from typing import Dict


def mock_ai_response(prompt: str) -> Dict[str, str]:
    """Return a deterministic AI response for a given prompt.

    Returns a dict with keys:
    - text: The textual response
    - tts_url: A fake URL to a TTS audio file (for demo only)
    """
    text = f"Echo: {prompt[:120]}"
    tts_url = "https://example.com/fake-tts/audio.mp3"
    return {"text": text, "tts_url": tts_url}
