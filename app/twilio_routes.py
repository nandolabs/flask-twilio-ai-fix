from flask import Blueprint, request, Response, current_app, jsonify
from .ai_handler import mock_ai_response
from .utils import validate_twilio_signature, build_twiml_response


twilio_bp = Blueprint("twilio", __name__)


@twilio_bp.route("/voice", methods=["POST"])
def voice_webhook():
    """Simulate a Twilio Voice webhook.

    Query param `mode=buggy` will run the buggy handler that returns
    malformed TwiML and misses calling the AI handler. Default behavior
    runs the corrected flow.
    """
    mode = request.args.get("mode", "fixed")
    auth_token = current_app.config.get("TWILIO_AUTH_TOKEN", "changeme")

    is_valid, reason = validate_twilio_signature(request, auth_token)
    if not is_valid:
        return jsonify({"error": "invalid signature", "reason": reason}), 400

    # Buggy flow: returns malformed TwiML and does not call AI handler
    if mode == "buggy":
        # Missing XML envelope and invalid tag
        malformed = "<Response><Say>This is a broken response"  # no closing tags
        return Response(malformed, content_type="application/xml")

    # Fixed flow: call AI, build valid TwiML
    prompt = request.form.get("SpeechResult") or request.form.get("Body") or "Hello"
    ai = mock_ai_response(prompt)
    twiml = build_twiml_response(ai["text"], ai.get("tts_url"))
    return Response(twiml, content_type="application/xml")
