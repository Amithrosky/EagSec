import os
import sys
import time
import subprocess
import ctypes
import tempfile
import webbrowser
import re
import ast
import random
import base64
import hashlib

# ==========================================
#                  LOGO
# ==========================================
EAGSEC_LOGO = r"""
███████╗ █████╗  ██████╗ ███████╗███████╗██████╗ 
██╔════╝██╔══██╗██╔════╝ ██╔════╝██╔════╝██╔═══╝
█████╗  ███████║██║  ███╗███████╗█████╗  ██║  
██╔══╝  ██╔══██║██║   ██║╚════██║██╔══╝  ██║  
███████╗██║  ██║╚██████╔╝███████║███████╗██████╗
╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚══════╝╚═════╝ 
=================================================
             Version - 3.2 Auto-Open
=================================================
"""

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_loading_animation(message):
    clear_screen()
    print(EAGSEC_LOGO)
    print(f"  {message}")
    print("  " + "─" * 45)
    x = random.randint(1, 20)
    for progress in range(0, 101, x):
        sys.stdout.write(f"\r  Initializing... [{progress}%]")
        sys.stdout.flush()
        time.sleep(0.05)
    sys.stdout.write("\r  Initializing... [100%]\n\n")
    sys.stdout.flush()
    time.sleep(0.5)

def ensure_dependencies():
    """Checks if PyInstaller is installed; if not, attempts to install it."""
    try:
        # Test if PyInstaller can be called as a module execution
        subprocess.run([sys.executable, "-m", "PyInstaller", "--version"], 
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("  [*] PyInstaller dependency not found. Installing via pip...")
        try:
            subprocess.run([sys.executable, "-m", "pip", "install", "pyinstaller"], check=True)
            print("  [+] PyInstaller installed successfully!\n")
            time.sleep(1.5)
        except Exception as e:
            print(f"  [!] Failed to auto-install PyInstaller: {e}")
            print("  [!] Please install it manually using: pip install pyinstaller")
            input("\n  Press Enter to continue anyway...")

# --- Encryption Helpers ---
def get_hash(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()

def xor_cipher(text, key):
    return ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(text))

def encrypt_payload(html_content, password):
    encrypted_text = xor_cipher(html_content, password)
    return base64.b64encode(encrypted_text.encode('utf-8')).decode('utf-8')

# ==========================================
#            AUTO-GENERATED DECOY
# ==========================================
def generate_fake_html():
    return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Storage Container Dashboard</title>
    <style>
        body { font-family: sans-serif; background-color: #f8f9fa; color: #202124; display: flex; justify-content: center; align-items: center; height: 100vh; margin:0; }
        .container { background: #ffffff; padding: 32px; border-radius: 24px; box-shadow: 0 4px 16px rgba(0,0,0,0.04); text-align: center; border: 1px solid #e0e0e0; max-width: 400px; }
        h1 { font-size: 22px; font-weight: 500; margin-bottom: 12px; }
        p { font-size: 14px; color: #5f6368; line-height: 1.6; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Secure Environment Sandbox</h1>
        <p>Initialization complete. This local runtime container is empty. Please mount a valid source directory to load assets.</p>
    </div>
</body>
</html>"""

# ==========================================
#               CORE FEATURES
# ==========================================
def lock_app():
    clear_screen()
    print("  [ MODE: SECURE HTML TO EXE ]")
    print("  " + "─" * 45)
    
    real_html_file = input("  Enter HTML file path: ").strip(' "')
    if not real_html_file.lower().endswith('.html') or not os.path.exists(real_html_file):
        print("\n  [!] ERROR: Valid .html file not found!")
        input("\n  Press Enter to go back...")
        return
        
    real_password = input("  Set password for REAL app: ")

    print("\n  -- Plausible Deniability Setup --")
    fake_password = input("  Set password for FAKE app: ")
    
    show_loading_animation("Encrypting payloads and generating wrapper...")
        
    base_name = os.path.splitext(os.path.basename(real_html_file))[0]
    output_py = f"Run_{base_name}.py"
    
    with open(real_html_file, 'r', encoding='utf-8', errors='ignore') as f:
        real_html = f.read()
        
    fake_html = generate_fake_html()
        
    real_hash = get_hash(real_password)
    fake_hash = get_hash(fake_password)
    real_payload = encrypt_payload(real_html, real_password)
    fake_payload = encrypt_payload(fake_html, fake_password)
    
    launcher_code = f"""import os
import sys
import tempfile
import webbrowser
import time
import base64
import hashlib

REAL_HASH = "{real_hash}"
FAKE_HASH = "{fake_hash}"
REAL_PAYLOAD = "{real_payload}"
FAKE_PAYLOAD = "{fake_payload}"

def get_hash(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()

def xor_decipher(text, key):
    return ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(text))

def run_secured_app():
    print("====================================================")
    print("  EAGSEC PROTECTED APP ACTIVE                       ")
    print("====================================================")
    
    html_to_load = None
    
    while True:
        input_pass = input("  Enter Password to Unlock: ")
        input_hash = get_hash(input_pass)
        
        if input_hash == REAL_HASH:
            print("  Access Granted.")
            decoded_b64 = base64.b64decode(REAL_PAYLOAD).decode('utf-8')
            html_to_load = xor_decipher(decoded_b64, input_pass)
            break
        elif input_hash == FAKE_HASH:
            print("  Access Granted.")
            decoded_b64 = base64.b64decode(FAKE_PAYLOAD).decode('utf-8')
            html_to_load = xor_decipher(decoded_b64, input_pass)
            break
        else:
            print("  ACCESS DENIED. Incorrect password.\\n")
        
    fd, temp_path = tempfile.mkstemp(suffix=".html")
    try:
        with os.fdopen(fd, 'w', encoding='utf-8') as tmp:
            tmp.write(html_to_load)
            
        webbrowser.open(f"file://{{temp_path}}")
        time.sleep(2)  
    finally:
        try:
            os.remove(temp_path)
        except:
            pass

if __name__ == "__main__":
    run_secured_app()
"""
    
    with open(output_py, 'w', encoding='utf-8') as f:
        f.write(launcher_code)
        
    print(f"  [+] Python wrapper generated: {output_py}")
    print("  [+] Compiling into a single standalone .exe file...")
    
    # Auto-Compile to EXE using PyInstaller
    try:
        subprocess.run([sys.executable, "-m", "PyInstaller", "--onefile", output_py], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        current_dir = os.getcwd()
        exe_dir = os.path.join(current_dir, "dist")
        exe_path = os.path.join(exe_dir, f"Run_{base_name}.exe")
        
        print(f"\n  [+] SUCCESS! Your executable is ready.")
        print(f"  [+] Exact Folder Location: {exe_dir}")
        print(f"  [+] Exact File Location: {exe_path}")
        
        if os.name == 'nt' and os.path.exists(exe_dir):
            print("  [+] Opening the destination folder for you right now...")
            os.startfile(exe_dir)
            
    except Exception as e:
        print(f"  [!] PyInstaller failed. Error: {e}")
            
    input("\n  Press Enter to go back to the menu...")

def make_immortal():
    clear_screen()
    print("  [ MODE: MAKE FILE IMMORTAL ]")
    print("  " + "─" * 45)
    if not is_admin():
        print("  [!] ERROR: You MUST run this script as Administrator to use this feature!")
        input("\n  Press Enter to go back to the menu...")
        return
    target_file = input("  Choose file to protect from deletion: ").strip(' "')
    if not os.path.exists(target_file):
        print("  [!] ERROR: File not found.")
        input("\n  Press Enter to go back...")
        return
    show_loading_animation("Applying system protection locks...")
    try:
        subprocess.run(["attrib", "+r", target_file], check=True)
        subprocess.run(["icacls", target_file, "/deny", "*S-1-1-0:(D,WDAC)"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print("  [+] Success! The file is now locked against deletion.")
    except Exception as e:
        print(f"  [!] Failed to lock file: {e}")
    input("\n  Press Enter to go back to the menu...")

def remove_immortal():
    clear_screen()
    print("  [ MODE: REMOVE IMMORTALITY ]")
    print("  " + "─" * 45)
    target_file = input("  Choose protected file to free: ").strip(' "')
    if not os.path.exists(target_file):
        print("  [!] ERROR: File not found.")
        input("\n  Press Enter to go back...")
        return
    if not is_admin():
        print("  [!] ERROR: You MUST run this script as Administrator to use this feature!")
        input("\n  Press Enter to go back...")
        return
    show_loading_animation("Removing file protection locks...")
    try:
        subprocess.run(["attrib", "-r", "-s", "-h", target_file], check=True)
        subprocess.run(["icacls", target_file, "/remove:d", "*S-1-1-0"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print("  [+] Success! The file is back to normal.")
    except Exception as e:
        print(f"  [!] Failed to unlock file: {e}")
    input("\n  Press Enter to go back to the menu...")

def main_menu():
    while True:
        clear_screen()
        admin_status = "ADMIN ACTIVE" if is_admin() else "NORMAL USER (No Admin)"
        print(f"  Status: {admin_status}")
        print("  " + "═" * 45)
        print("\n -------------- Choose your preference -------------- \n")
        print("  1) Lock HTML App to EXE (Auto-Decoy)")
        print("  2) Make File Immortal")
        print("  3) Remove Immortality")
        print("  4) Exit")
        print("  " + "═" * 45 + "\n")
        choice = input("  EagSec > ").strip()
        if choice == "1":
            lock_app()
        elif choice == "2":
            make_immortal()
        elif choice == "3":
            remove_immortal()
        elif choice == "4":
            print("\n  Closing EagSec. Have a nice day!")
            time.sleep(1)
            break

if __name__ == "__main__":
    # Check Windows OS requirement
    if os.name != 'nt':
        print("[!] Warning: This script relies on Windows features.")
        input("    Press Enter to continue anyway...")
    
    # 1. Automatic Administrator Elevation Check
    if not is_admin():
        print("[*] Script requires administrative privileges. Attempting elevation...")
        try:
            # Re-launch script with administrative permissions ('runas')
            # Passes the current interpreter executable and the current script file path
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, f'"{__file__}"', None, 1)
            sys.exit(0)
        except Exception as e:
            print(f"[!] Elevation failed: {e}")
            input("Press Enter to continue with current privileges...")

    # 2. Run dependency checker and initializations
    ensure_dependencies()
    show_loading_animation("Created by Amithrosky.")
    main_menu()
