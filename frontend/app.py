"""Module to start the frontend."""
import subprocess
import sys
import os

PYTHON_EXECUTABLE = sys.executable
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

print(" Starting Frontend...")
subprocess.Popen(
    [PYTHON_EXECUTABLE, "-m", "frontend.frontend_app"],
    cwd=ROOT_DIR
)
print(" Frontend started...")
