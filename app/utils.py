from typing import Tuple
import hmac
import hashlib


def validate_twilio_signature(request, auth_token: str) -> Tuple[bool, str]:
    """Validate Twilio signature for incoming webhook.

    Returns (is_valid, reason).
    This is a simplified implementation suitable for demo/testing. It
    does NOT support all Twilio features but is good enough for this demo.
    """
    signature = request.headers.get("X-Twilio-Signature", "")
    # Allow a simple test-mode: when the repo/example auth token is still
    # the placeholder value and no signature is supplied, treat as valid.
    if not signature and auth_token == "changeme":
        return True, "test-mode: signature skipped"

    url = request.url
    params = request.form or request.get_json(silent=True) or {}

    # Twilio builds the string as URL plus parameters sorted by key
    payload = url
    if isinstance(params, dict):
        for k in sorted(params.keys()):
            payload += k + (params[k] or "")

    expected = hmac.new(auth_token.encode(), payload.encode(), hashlib.sha1)
    expected_sig = expected.hexdigest()

    if hmac.compare_digest(expected_sig, signature):
        return True, "OK"
    return False, "Signature mismatch"


def build_twiml_response(text: str, tts_url: str | None = None) -> str:
    """Construct a minimal valid TwiML response.

    If tts_url is provided, insert <Play> tag. Otherwise return simple
    <Response><Say> text </Say></Response> structure.
    """
    if tts_url:
        return (
            '<?xml version="1.0" encoding="UTF-8"?>'
            '<Response>'
            f'<Play>{tts_url}</Play>'
            '</Response>'
        )
    return (
        '<?xml version="1.0" encoding="UTF-8"?>'
        '<Response>'
        f'<Say>{text}</Say>'
        '</Response>'
    )
