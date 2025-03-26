"""The common Module to start Backend and Frontend"""
import subprocess
import sys

PYTHON_EXECUTABLE = sys.executable

print("Starting Backend...")
backend_proc = subprocess.Popen([PYTHON_EXECUTABLE, "-m", "backend.backend_app"])
print("Backend started...")

print("Starting Frontend...")
frontend_proc = subprocess.Popen([PYTHON_EXECUTABLE, "-m", "frontend.frontend_app"])
print("Frontend started...")

try:
    backend_proc.wait()
    frontend_proc.wait()
except KeyboardInterrupt:
    print("🛑 Shutting down...")
    backend_proc.terminate()
    frontend_proc.terminate()
