import pytest
from app import create_app


@pytest.fixture
def client():
    app = create_app({"TESTING": True, "TWILIO_AUTH_TOKEN": "changeme"})
    with app.test_client() as c:
        yield c


def test_voice_webhook_buggy_mode_returns_malformed_twiml(client):
    resp = client.post("/voice?mode=buggy", data={"SpeechResult": "hi"}, headers={"X-Twilio-Signature": ""})
    assert resp.status_code == 200
    text = resp.get_data(as_text=True)
    # The buggy response is intentionally malformed (missing closing tags)
    assert text.startswith("<Response><Say")


def test_voice_webhook_fixed_mode_returns_valid_twiml(client):
    # Use a fake signature that matches our simplistic validator (empty ok for demo)
    resp = client.post("/voice", data={"SpeechResult": "hello"}, headers={"X-Twilio-Signature": ""})
    assert resp.status_code == 200
    text = resp.get_data(as_text=True)
    assert text.startswith("<?xml")
    assert "<Response>" in text and ("<Say>" in text or "<Play>" in text)
