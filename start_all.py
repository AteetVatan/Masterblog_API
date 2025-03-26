import subprocess
import os
import sys

# Use the same Python interpreter that's running this script
PYTHON_EXECUTABLE = sys.executable

# File paths
BACKEND_PATH = os.path.join("backend", "backend_app.py")
FRONTEND_PATH = os.path.join("frontend", "frontend_app.py")

print("🚀 Starting Backend...")
backend_proc = subprocess.Popen([PYTHON_EXECUTABLE, BACKEND_PATH])
print(f"✅ Backend started with PID {backend_proc.pid}")

print("🚀 Starting Frontend...")
frontend_proc = subprocess.Popen([PYTHON_EXECUTABLE, FRONTEND_PATH])
print(f"✅ Frontend started with PID {frontend_proc.pid}")

# Keep the main process alive
try:
    backend_proc.wait()
    frontend_proc.wait()
except KeyboardInterrupt:
    print("🛑 Shutting down...")
    backend_proc.terminate()
    frontend_proc.terminate()
