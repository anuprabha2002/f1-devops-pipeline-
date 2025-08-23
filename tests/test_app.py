
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import app


def test_app_output():
    # Capture the output of app.py
    # Expected output is: "Hello DevOps"
    assert app.main() == "Hello DevOps"

