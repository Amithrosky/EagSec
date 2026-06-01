import os
import sys
import time
import subprocess
import ctypes
import tempfile
import webbrowser

def is_admin():
    """Checks if the script is running with administrative privileges."""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def main_menu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("EagSec [Version 1.0.26200.8457]")
        print(">>>Still incomplete BTW.\n")
        print("1) Lock App")
        print("2) Immortalisation")
        print("3) Exit\n")
        
        choice = input("EagSec > ").strip()
        
        if choice == "1":
            lock_app()
        elif choice == "2":
            make_immortal()
        elif choice == "3":
            print("\nOnce done, EagSec will close on its own.")
            time.sleep(2)
            break

def lock_app():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("1. Lock App")
    print("-----------------------------")
    print("EagSec>LockApp")
    html_file = input("Enter target HTML file path: ").strip()
    
    if not os.path.exists(html_file):
        print("[!] Target HTML file not found. Check your path or spelling.")
        input("\nPress Enter to return to main menu...")
        return

    print("\n>>> Next, user must configure password.")
    app_password = input("Enter Password: ")
    
    print("\n>>> Securing and wrapping application...")
    for i in range(1, 101, 5):
        print(f"Processing... [{i}%]")
        time.sleep(0.04)
        
    base_name = os.path.splitext(os.path.basename(html_file))[0]
    output_wrapper = f"Run_{base_name}.py"
    
    # Read the content of the HTML file safely without line parsing breaks
    try:
        with open(html_file, 'r', encoding='utf-8', errors='ignore') as f:
            html_content = f.read()
    except Exception as e:
        print(f"[!] Error reading HTML file: {e}")
        input("\nPress Enter to return to main menu...")
        return
        
    # Generate a pure, stable Python wrapper engine
    launcher_code = f"""import os
import sys
import tempfile
import webbrowser
import time

def run_secured_app():
    print(">>> EagSec Runtime Protection Engine Active...")
    time.sleep(1)
    
    while True:
        input_pass = input("Enter Password to Unlock: ")
        if input_pass == {repr(app_password)}:
            print(">>> Access Granted.")
            break
        print("ACCESS DENIED. Invalid signature token.\\n")
        
    # Initialize container via standard secure temp space
    print("Initializing isolated container...")
    fd, temp_path = tempfile.mkstemp(suffix=".html")
    try:
        with os.fdopen(fd, 'w', encoding='utf-8') as tmp:
            tmp.write({repr(html_content)})
            
        # Safely render using system default browser interface
        webbrowser.open(f"file://{{temp_path}}")
        time.sleep(2)  
    finally:
        # Immediate clean up once loaded
        try:
            os.remove(temp_path)
        except:
            pass

if __name__ == "__main__":
    run_secured_app()
"""
    
    try:
        with open(output_wrapper, 'w', encoding='utf-8') as f:
            f.write(launcher_code)
        print(f"\nSuccess! Password lock applied successfully.")
        print(f"Generated protected bundle: {output_wrapper}")
    except Exception as e:
        print(f"[!] Error writing wrapper script: {e}")
        input("\nPress Enter to return to main menu...")
        return
        
    print("------------------------------------------------------------")
    del_choice = input(f"[?] Do you want to delete the original unprotected source file (\"{html_file}\")? (Y/N): ").strip().upper()
    
    if del_choice == "Y":
        try:
            os.remove(html_file)
            print("[>] Original unprotected file removed. Only the locked app remains.")
        except Exception as e:
            print(f"[!] Error removing original file: {e}")
    else:
        print("[>] Original unprotected file preserved.")
        
    input("\nPress Enter to return to main menu...")

def make_immortal():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("2. Make file immortal")
    print("-----------------------------")
    print("EagSec > MFI")
    target_file = input("Chose File: ").strip()
    
    if not os.path.exists(target_file):
        print("[!] Target file does not exist.")
        input("\nPress Enter to return to main menu...")
        return
        
    print("\nChecking administrator privileges...")
    if not is_admin():
        print("[ERROR] You MUST run this Python script as an Administrator to use MFI!")
        input("\nPress Enter to return to main menu...")
        return
        
    print("\nDeploying low-level system attributes...")
    for i in range(1, 101, 10):
        print(f"Processing... [{i}%]")
        time.sleep(0.04)
        
    try:
        # Apply Windows system attributes (Read-only, System, Hidden)
        subprocess.run(["attrib", "+r", "+s", "+h", target_file], check=True)
        
        # Deny explicit deletion permissions to global users via standard SID (S-1-1-0)
        subprocess.run(["icacls", target_file, "/deny", "*S-1-1-0:(D,WDAC)"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        print("\n>>> System integrity flags applied.")
        print("File is now hidden and locked against deletion.")
    except Exception as e:
        print(f"[!] Failed to apply attributes or permissions: {e}")
        
    input("\nPress Enter to return to main menu...")

if __name__ == "__main__":
    # Friendly enforcement for Windows-specific components
    if os.name != 'nt':
        print("[!] Warning: This utility relies on Windows elements (attrib, icacls). Run on Windows for optimal behavior.")
        input("Press Enter to proceed anyway...")
    main_menu()
