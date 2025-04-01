"""Module to start the backend."""
import subprocess
import sys
import os

PYTHON_EXECUTABLE = sys.executable
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

print(" Starting Backend...")
subprocess.Popen(
    [PYTHON_EXECUTABLE, "-m", "backend.backend_app"],
    cwd=ROOT_DIR
)
print(" Backend started...")
