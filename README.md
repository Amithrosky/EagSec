# 🦅 EagSec (v3.2)

**EagSec** is a streamlined Python utility built exclusively for Windows environments. It is designed to securely compile standard HTML files into standalone `.exe` binaries equipped with cryptographic access controls, dual-payload plausible deniability, and native file-locking mechanisms.

---

## ⚙️ Core Capabilities

* **Executable Generation:** Transforms `.html` assets into highly portable, single-file Windows executables.
* **Dual-State Plausible Deniability:** Supports two distinct unlock passwords per executable: one to decrypt the genuine HTML asset, and a secondary password to deploy an auto-generated "Secure Sandbox" decoy.
* **System-Level File Locking:** Grants users the ability to render designated files "immortal" by manipulating Windows access control lists (ACLs) to block modification or deletion.
* **Auto-Elevation:** Automatically detects execution context and prompts for User Account Control (UAC) administrative privileges if lacking.

---

## 🛠️ Technical Architecture

EagSec utilizes a zero-hardcoded-secrets approach. Passwords are never stored in plain text, and payloads are dynamically decrypted directly into memory before being briefly written to a temporary browser cache.

| Component | Implementation Details |
| :--- | :--- |
| **Compilation Engine** | PyInstaller (Auto-installs via `pip` if missing) |
| **Authentication** | SHA-256 Hashing |
| **Payload Encryption** | XOR Cipher mapped to user-defined keys |
| **Binary Storage** | Base64 Encoded Strings |
| **Immortality Locks** | Windows Native Commands (`attrib` & `icacls`) |
| **System Interaction** | `ctypes`, `subprocess`, `tempfile` |

---

## 🚀 Installation & Setup

### Prerequisites
* **OS:** Windows 10 / 11
* **Environment:** Python 3.x installed and added to System PATH.
* **Additional** Pyinstaller installed

### Deployment Steps
1.  **Clone the repository to your local machine:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/EagSec.git](https://github.com/YOUR_USERNAME/EagSec.git)
    cd EagSec
    ```
2.  **Launch the application:**
    ```bash
    python EagSec.py
    ```
    *Note: The script will automatically request Admin privileges upon launch. Allow the UAC prompt to ensure all features function correctly.*

---

## 📖 Usage Guide

Upon launching the EagSec terminal interface, you will be presented with a centralized menu:

### 1. Lock HTML App to EXE
Provide the absolute or relative path to your `.html` file. The terminal will prompt you to establish a **Real Password** and a **Fake Password**. Once compiled, the new `.exe` will be saved to an automatically generated `dist/` directory. 

### 2. Make File Immortal
Provide the exact path to any local file you wish to lock. EagSec will apply strict Read-Only attributes and deny `WDAC` (Write DAC) permissions to prevent deletion.

### 3. Remove Immortality
Provide the path of a previously locked file. EagSec will strip the applied attributes and restore default file interaction permissions.

---

## ⚖️ Legal & Ethical Disclaimer

**EagSec is provided for educational, authorized administrative, and conceptual security testing purposes only.** The developers and contributors assume no liability and are not responsible for any misuse or damage caused by this program. Users must operate this tool in strict compliance with all applicable local, state, and federal laws.
