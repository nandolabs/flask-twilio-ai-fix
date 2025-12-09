from flask import Flask


def create_app(test_config: dict | None = None) -> Flask:
    app = Flask(__name__, instance_relative_config=False)

    if test_config:
        app.config.update(test_config)

    from .twilio_routes import twilio_bp
    app.register_blueprint(twilio_bp)

    return app
