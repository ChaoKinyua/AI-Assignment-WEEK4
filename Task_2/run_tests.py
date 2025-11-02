"""
Test runner script for login page automation
Generates HTML report with screenshots
"""
import subprocess
import sys
import os

def main():
    # Create screenshots directory if it doesn't exist
    screenshots_dir = os.path.join("Task_2", "screenshots")
    if not os.path.exists(screenshots_dir):
        os.makedirs(screenshots_dir)
        print(f"Created directory: {screenshots_dir}")
    
    # Run pytest with HTML report
    result = subprocess.run([
        sys.executable, "-m", "pytest",
        "Task_2/test_login.py",
        "-v",  # Verbose output
        "--html=Task_2/test_report.html",
        "--self-contained-html",
        "-s"   # Show print statements
    ])
    
    print("\n" + "="*60)
    print("Test execution completed!")
    print("="*60)
    print(f"Exit code: {result.returncode}")
    print("\nResults:")
    print("- Success: Login page test suite completed")
    print("- Screenshots: Saved in Task_2/screenshots/")
    print("- HTML Report: Task_2/test_report.html")
    print("\nView the full report by opening test_report.html in a browser")
    
    return result.returncode

if __name__ == "__main__":
    sys.exit(main())
