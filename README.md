# 🔐 MyPass: Local-First Credential Manager

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-blue?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

A professional-grade productivity tool developed for **Day 29** of the #100DaysOfCode challenge. This application refactors standard credential storage into a secure, GUI-based management system featuring real-time data retrieval and an integrated "Vault" architecture.

---

## ✨ Core Functionalities

* **🗄️ Integrated Vault Viewer**: Features a secondary window logic that parses and renders localized `data.txt` content directly within a non-editable `Text` widget for secure viewing.
* **⚡ On-Demand Generation**: A randomized entropy engine that creates complex 12-16 character passwords across multiple character sets instantly.
* **📋 Clipboard Synchronization**: Utilizes the `pyperclip` module to automatically sync generated strings to the system clipboard, streamlining the user workflow.
* **🛡️ Interactive Validation**: Built-in guard clauses and `messagebox` confirmation protocols to prevent empty fields and ensure data integrity.

---

## 🛠️ Technical Breakdown

### 1. Multi-Window State Management
Unlike basic implementations, this project manages two concurrent `Tk` instances. The `show_passwords()` function initializes a secondary window that operates independently of the main entry form, allowing users to cross-reference their "Vault" while adding new entries.
* **Independent Mainloops**: Managed separate `mainloop()` logic to ensure the secondary window captures focus without freezing the primary application state.
* **Non-Editable Buffers**: Utilized the `Text` widget with manual clearing (`1.0, END`) to ensure the display remains read-only and free from unintentional modifications during viewing.



### 2. UI Architecture & Grid Optimization
The GUI is built using a precise grid-based coordinate system to handle complex widget alignment:
* **Dynamic Column Spanning**: Leveraged `columnspan=2` on entry fields to maintain a symmetrical layout while integrating asymmetric buttons (like "Generate Password") on the same row.
* **Responsive Row Configuration**: Implemented `rowconfigure` and `columnconfigure` with specific padding (`pad=5`) to ensure a consistent aesthetic regardless of window resizing.

### 3. Persistent Data Pipeline
The backend utilizes a pipe-separated flat-file system (`Website | Username | Password`) in `data.txt`:
* **Context Manager File I/O**: Used the `with` statement for all file operations to guarantee proper stream closure and prevent memory leaks or file locking errors.
* **Append-Mode Logic**: Employed the `"a"` (append) mode for saving, ensuring that new entries are stacked without over-writing existing encrypted data.
* **Field Clearing Protocols**: Implemented post-save clearing of specific `Entry` widgets (`website_entry.delete`) to prepare the UI for the next transaction immediately.

---

## 🚀 Installation & Usage

1. **Clone the Repository**:
   ```bash
   git clone [https://github.com/CodeWithAnubhav-ICT/PasswordManager.git](https://github.com/CodeWithAnubhav-ICT/PasswordManager.git)
