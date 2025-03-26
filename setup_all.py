"""Module to install requirements of both Backend server and Frontend client APP. """

import subprocess
import os

def install_requirements(path):
    """Function to Install requirements"""
    req_file = os.path.join(path, "requirements.txt")
    if os.path.exists(req_file):
        print(f"📦 Installing dependencies for {path}...")
        subprocess.check_call(["pip", "install", "-r", req_file])
    else:
        print(f"⚠️ No requirements.txt found in {path}")


# Install backend and frontend requirements
install_requirements("backend")
install_requirements("frontend")
