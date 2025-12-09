"""
Flask application entry point.

This module provides the entry point for running the Flask development server.
It creates the Flask app using the application factory pattern and configures
basic logging.
"""

import logging
import os
from dotenv import load_dotenv

from app import create_app

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def main():
    """Create and run the Flask application."""
    app = create_app()

    # Get configuration from environment
    host = os.getenv('FLASK_HOST', '0.0.0.0')
    port = int(os.getenv('FLASK_PORT', 5000))
    debug = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'

    logger.info(f"Starting Flask app on {host}:{port} (debug={debug})")
    logger.info("Endpoints available:")
    logger.info("  GET  /voice        - Twilio webhook (buggy mode)")
    logger.info("  GET  /voice/fixed  - Twilio webhook (fixed mode)")
    logger.info("  POST /voice        - Twilio webhook (buggy mode)")
    logger.info("  POST /voice/fixed  - Twilio webhook (fixed mode)")

    app.run(host=host, port=port, debug=debug)


if __name__ == '__main__':
    main()
