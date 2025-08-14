# 🛠️ PDF Tools Suite - Installation Guide

**Professional Setup Instructions for All Platforms**

## 📋 System Requirements

### Minimum Requirements
- **Operating System**: Windows 10, macOS 10.14, or Linux (Ubuntu 18.04+)
- **Python**: Version 3.7 or higher
- **Memory**: 512 MB RAM available
- **Storage**: 100 MB free disk space
- **Display**: 1024x768 screen resolution

### Recommended Requirements  
- **Operating System**: Windows 11, macOS 12+, or Linux (Ubuntu 20.04+)
- **Python**: Version 3.9 or higher
- **Memory**: 2 GB RAM available
- **Storage**: 1 GB free disk space
- **Display**: 1920x1080 screen resolution

## 🚀 Quick Installation

### Option 1: One-Click Setup (Recommended)

**Windows Users:**
1. Download all project files
2. Double-click `StartApp.bat`
3. Follow automatic setup prompts

**Mac/Linux Users:**
1. Download all project files
2. Open terminal in project directory
3. Run: `chmod +x StartApp.sh && ./StartApp.sh`

### Option 2: Manual Installation

**Step 1: Install Python**
- Visit [python.org](https://python.org/downloads)
- Download Python 3.7+ for your operating system
- **Important**: Check "Add Python to PATH" during installation

**Step 2: Install Dependencies**
```bash
pip install pypdf reportlab pillow
```

**Step 3: Launch Application**
```bash
python PDFToolsApp.py
```

## 🔧 Platform-Specific Instructions

### Windows Installation

**Method 1: Using Python Installer**
1. Download Python from [python.org](https://python.org)
2. Run installer with "Add to PATH" checked
3. Open Command Prompt
4. Navigate to project folder
5. Run: `pip install -r Dependencies.txt`
6. Run: `python PDFToolsApp.py`

**Method 2: Using Microsoft Store**
1. Install Python from Microsoft Store
2. Open PowerShell in project directory
3. Run: `pip install pypdf reportlab pillow`
4. Run: `python PDFToolsApp.py`

**Troubleshooting Windows:**
- If Python not recognized: Reinstall with PATH option
- If pip fails: Run as Administrator
- If tkinter missing: Reinstall Python with full features

### macOS Installation

**Method 1: Using Homebrew (Recommended)**
```bash
# Install Homebrew if not present
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python
brew install python

# Install dependencies
pip3 install pypdf reportlab pillow

# Run application
python3 PDFToolsApp.py
```

**Method 2: Using Official Python**
1. Download Python from [python.org](https://python.org)
2. Install using the downloaded package
3. Open Terminal
4. Run: `pip3 install pypdf reportlab pillow`
5. Run: `python3 PDFToolsApp.py`

**Troubleshooting macOS:**
- If permission denied: Use `sudo pip3 install`
- If tkinter issues: Install Python from python.org
- If Homebrew conflicts: Use virtual environment

### Linux Installation

**Ubuntu/Debian:**
```bash
# Update package list
sudo apt update

# Install Python and pip
sudo apt install python3 python3-pip python3-tk

# Install dependencies
pip3 install pypdf reportlab pillow

# Run application
python3 PDFToolsApp.py
```

**CentOS/RHEL/Fedora:**
```bash
# Install Python and pip
sudo dnf install python3 python3-pip python3-tkinter

# Install dependencies  
pip3 install pypdf reportlab pillow

# Run application
python3 PDFToolsApp.py
```

**Arch Linux:**
```bash
# Install dependencies
sudo pacman -S python python-pip tk

# Install Python packages
pip install pypdf reportlab pillow

# Run application
python PDFToolsApp.py
```

## 🔍 Verification & Testing

### Installation Verification
1. **Check Python Version**:
   ```bash
   python --version
   # Should show 3.7.0 or higher
   ```

2. **Verify Dependencies**:
   ```bash
   python -c "import pypdf, reportlab, PIL; print('All dependencies installed')"
   ```

3. **Test Application Launch**:
   ```bash
   python PDFToolsApp.py
   # Application window should appear
   ```

### Test Application Function
1. **Run Test Suite**:
   ```bash
   python TestApplication.py
   ```

2. **Verify Core Features**:
   - Document selection works
   - All operation buttons respond
   - Activity log displays messages
   - File dialogs open correctly

## 🌐 Advanced Setup Options

### Virtual Environment (Recommended for Developers)
```bash
# Create virtual environment
python -m venv pdf_tools_env

# Activate environment
# Windows:
pdf_tools_env\Scripts\activate
# Mac/Linux:
source pdf_tools_env/bin/activate

# Install dependencies
pip install pypdf reportlab pillow

# Run application
python PDFToolsApp.py
```

### Portable Installation
1. Create folder: `PDFToolsPortable`
2. Copy all project files
3. Install portable Python
4. Create custom launcher script
5. Distribute as single package

### System-Wide Installation
```bash
# Install as system package (Linux/Mac)
sudo pip install pypdf reportlab pillow

# Create desktop shortcut
cp PDFToolsApp.py /usr/local/bin/pdf-tools
chmod +x /usr/local/bin/pdf-tools
```

## 🔧 Common Installation Issues

### Python Not Found
**Problem**: `python` command not recognized
**Solutions**:
- Windows: Reinstall Python with "Add to PATH" checked
- Mac: Use `python3` instead of `python`
- Linux: Install `python-is-python3` package

### Permission Errors
**Problem**: Cannot install packages
**Solutions**:
- Windows: Run Command Prompt as Administrator
- Mac/Linux: Use `sudo pip install` or `pip install --user`
- All: Use virtual environment

### Missing tkinter
**Problem**: GUI framework not available
**Solutions**:
- Windows: Reinstall Python with full installation
- Mac: Install Python from python.org (not Homebrew)
- Linux: Install `python3-tk` package

### Network Issues
**Problem**: Cannot download packages
**Solutions**:
- Check internet connection
- Use different pip index: `pip install -i https://pypi.org/simple/`
- Download wheels manually

## 📦 Package Management

### Updating Dependencies
```bash
# Update all packages
pip install --upgrade pypdf reportlab pillow

# Check versions
pip list | grep -E "(pypdf|reportlab|pillow)"
```

### Uninstalling
```bash
# Remove Python packages
pip uninstall pypdf reportlab pillow

# Delete project files
# Windows: Delete project folder
# Mac/Linux: rm -rf pdf-tools-folder
```

## 🆘 Getting Help

### Self-Diagnosis
1. Run `python TestApplication.py`
2. Check error messages in Activity Log
3. Verify all files are present
4. Test with sample PDF documents

### Community Support
- Check project documentation
- Review common issues section
- Submit bug reports with error details
- Share installation environment details

---

**Installation Complete!** 🎉

Your PDF Tools Suite is ready for professional document processing.

**Next Steps**:
1. Review the UserGuide.md for usage instructions
2. Test with sample documents
3. Explore all available features
4. Customize settings as needed

*For ongoing support, keep this guide handy and check for application updates regularly.*
