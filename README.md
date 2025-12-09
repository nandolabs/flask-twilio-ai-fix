# Flask Twilio AI Fix

Demo project that reproduces a small Twilio + Flask bug and shows a clean
fix. This is a portfolio-quality item for NandoLabs and follows the
NandoLabs Global Guidelines.

Features
- /voice endpoint that simulates a Twilio Voice webhook
- Buggy mode (mode=buggy) that returns malformed TwiML and skips AI
- Fixed mode that calls a mock AI handler and returns valid TwiML

Tech stack
- Python 3.12+
- Flask 3.0

Quickstart
1. Copy `.env.example` to `.env` and set `TWILIO_AUTH_TOKEN`.
2. Create a venv and install: `pip install -e .[dev]` or use `uv`.
3. Run the app:

```bash
export FLASK_ENV=development
python -m flask --app app.main run --port 5000
```

API
- POST /voice?mode=buggy => returns malformed TwiML (demo bug)
- POST /voice => returns valid TwiML using mock AI response

Testing
```bash
pytest -q
```

NandoLabs — Demonstration quality portfolio item
