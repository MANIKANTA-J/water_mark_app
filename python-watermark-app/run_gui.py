#!/usr/bin/env python3
"""
Watermark Application Launcher
Run this script to start the GUI watermark application.
"""

import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

try:
    from gui_app import main
    main()
except ImportError as e:
    print(f"Error importing required modules: {e}")
    print("Please make sure you have installed the required dependencies:")
    print("pip install -r requirements.txt")
    sys.exit(1)
except Exception as e:
    print(f"An error occurred: {e}")
    sys.exit(1)