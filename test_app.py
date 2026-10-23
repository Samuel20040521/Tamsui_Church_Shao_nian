#!/usr/bin/env python3
"""
Quick test script to verify the UI skeleton works
Run with: python test_app.py
"""

import sys
import subprocess
import time


def main():
    print("=" * 60)
    print("Testing Tamsui Church Shao-nian System UI Skeleton")
    print("=" * 60)

    print("\n1. Checking if FastAPI is installed...")
    try:
        import fastapi

        print("   ✓ FastAPI is installed")
    except ImportError:
        print("   ✗ FastAPI not found. Installing...")
        subprocess.run(
            [
                sys.executable,
                "-m",
                "pip",
                "install",
                "fastapi",
                "uvicorn[standard]",
                "jinja2",
            ]
        )

    print("\n2. Starting development server...")
    print("   Server will start at: http://localhost:8000")
    print("   Press Ctrl+C to stop\n")
    print("=" * 60)
    print("Test the following URLs:")
    print("  • Home:     http://localhost:8000/")
    print("  • Record:   http://localhost:8000/record")
    print("  • Devotion: http://localhost:8000/devotion")
    print("  • Profile:  http://localhost:8000/profile")
    print("=" * 60)

    time.sleep(2)

    # Start the server
    subprocess.run(
        [
            sys.executable,
            "-m",
            "uvicorn",
            "app.main:app",
            "--reload",
            "--host",
            "0.0.0.0",
            "--port",
            "8000",
        ]
    )


if __name__ == "__main__":
    main()
