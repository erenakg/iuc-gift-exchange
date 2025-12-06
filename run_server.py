#!/usr/bin/env python
"""
Simple script to help setup and run the New Year's Gift Exchange application
"""

import os
import sys
import subprocess

def print_banner():
    print("""
    ╔═══════════════════════════════════════════════════════════╗
    ║                                                           ║
    ║        🎄 New Year's Gift Exchange Setup Script 🎄        ║
    ║                                                           ║
    ╚═══════════════════════════════════════════════════════════╝
    """)

def check_python_version():
    print("✓ Checking Python version...")
    version = sys.version_info
    if version.major >= 3 and version.minor >= 8:
        print(f"  Python {version.major}.{version.minor} detected - OK!")
        return True
    else:
        print(f"  ✗ Python {version.major}.{version.minor} detected")
        print("  Please install Python 3.8 or higher")
        return False

def run_migrations():
    print("\n✓ Running database migrations...")
    try:
        subprocess.run([sys.executable, "manage.py", "migrate"], check=True)
        print("  Database setup complete!")
        return True
    except subprocess.CalledProcessError:
        print("  ✗ Migration failed")
        return False

def start_server():
    print("\n✓ Starting development server...")
    print("\n" + "="*60)
    print("🎉 Your New Year's Gift Exchange app is starting!")
    print("="*60)
    print("\n📱 Open your browser and visit:")
    print("   http://127.0.0.1:8000/")
    print("\n🛑 Press Ctrl+C to stop the server")
    print("="*60 + "\n")
    
    try:
        subprocess.run([sys.executable, "manage.py", "runserver"])
    except KeyboardInterrupt:
        print("\n\n✓ Server stopped. Happy coding! 🎄")

def main():
    print_banner()
    
    if not check_python_version():
        sys.exit(1)
    
    print("\nIMPORTANT: Make sure you have:")
    print("  1. Created and activated your virtual environment")
    print("  2. Installed requirements: pip install -r requirements.txt")
    
    response = input("\nHave you completed these steps? (yes/no): ").lower()
    
    if response not in ['yes', 'y']:
        print("\nPlease complete the setup steps first:")
        print("  1. python -m venv venv")
        print("  2. .\\venv\\Scripts\\Activate.ps1  (Windows)")
        print("  3. pip install -r requirements.txt")
        print("\nThen run this script again!")
        sys.exit(0)
    
    if not run_migrations():
        print("\n✗ Setup failed. Please check the errors above.")
        sys.exit(1)
    
    start_server()

if __name__ == "__main__":
    main()
