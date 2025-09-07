#!/usr/bin/env python3
"""
Setup script for Mathematics for Machine Learning course
This script helps set up the Python environment and verify dependencies.
"""

import subprocess
import sys
import os
from pathlib import Path


def check_python_version():
    """Check if Python version is 3.8 or higher"""
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 or higher is required")
        print(f"Current version: {sys.version}")
        return False
    else:
        print(f"✅ Python version: {sys.version}")
        return True


def install_requirements():
    """Install required packages from requirements.txt"""
    print("\n📦 Installing required packages...")
    try:
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", "-r", "requirements.txt"]
        )
        print("✅ All packages installed successfully!")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to install packages")
        return False


def verify_imports():
    """Verify that key packages can be imported"""
    print("\n🔍 Verifying package imports...")
    packages = ["numpy", "scipy", "matplotlib", "jupyter", "pandas", "sklearn", "sympy"]

    failed_imports = []
    for package in packages:
        try:
            __import__(package)
            print(f"✅ {package}")
        except ImportError:
            print(f"❌ {package}")
            failed_imports.append(package)

    return len(failed_imports) == 0


def create_jupyter_config():
    """Create basic Jupyter configuration"""
    print("\n⚙️  Setting up Jupyter configuration...")
    try:
        # Enable widgets extension
        subprocess.run(
            [
                sys.executable,
                "-m",
                "jupyter",
                "nbextension",
                "enable",
                "--py",
                "widgetsnbextension",
            ],
            capture_output=True,
        )
        print("✅ Jupyter widgets enabled")
        return True
    except:
        print("⚠️  Could not configure Jupyter widgets (non-critical)")
        return True


def setup_git_hooks():
    """Set up git hooks for the repository (optional)"""
    if os.path.exists(".git"):
        print("\n🔧 Setting up git hooks...")
        # You could add pre-commit hooks here
        print("✅ Git repository detected")
    else:
        print("\n⚠️  Not a git repository - skipping git setup")


def main():
    """Main setup function"""
    print("🚀 Mathematics for Machine Learning - Setup Script")
    print("=" * 50)

    # Check Python version
    if not check_python_version():
        sys.exit(1)

    # Install requirements
    if not install_requirements():
        print("\n❌ Setup failed during package installation")
        sys.exit(1)

    # Verify imports
    if not verify_imports():
        print("\n❌ Some packages failed to import")
        print("Try running: pip install -r requirements.txt")
        sys.exit(1)

    # Configure Jupyter
    create_jupyter_config()

    # Setup git (optional)
    setup_git_hooks()

    print("\n" + "=" * 50)
    print("🎉 Setup completed successfully!")
    print("\nNext steps:")
    print("1. Start Jupyter Lab: jupyter lab")
    print("2. Open modules/01-foundations/README.md")
    print("3. Begin your learning journey!")
    print("\nFor help, visit: https://github.com/your-repo/discussions")


if __name__ == "__main__":
    main()
