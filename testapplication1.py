# Create the StartApp.sh file (Linux/Mac launcher)
startapp_sh_content = '''#!/bin/bash

# PDF Tools Suite - Professional Edition Launcher
# For Linux and macOS systems

# Colors for output
RED='\\033[0;31m'
GREEN='\\033[0;32m'
YELLOW='\\033[1;33m'
BLUE='\\033[0;34m'
NC='\\033[0m' # No Color

echo ""
echo "================================================"
echo "         PDF Tools Suite - Starting..."
echo "================================================"
echo ""

# Function to print colored output
print_info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

# Check if Python is installed
print_info "Checking Python installation..."

# Try python3 first (recommended)
if command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
    PYTHON_VERSION=$(python3 --version 2>&1)
    print_info "Found $PYTHON_VERSION"
elif command -v python &> /dev/null; then
    PYTHON_CMD="python"
    PYTHON_VERSION=$(python --version 2>&1)
    
    # Check if it's Python 3
    if [[ $PYTHON_VERSION == *"Python 3"* ]]; then
        print_info "Found $PYTHON_VERSION"
    else
        print_error "Found $PYTHON_VERSION, but Python 3.7+ is required"
        echo ""
        echo "Please install Python 3.7+ from:"
        echo "  • Ubuntu/Debian: sudo apt install python3 python3-pip python3-tk"
        echo "  • macOS: brew install python3 or download from python.org"
        echo "  • CentOS/RHEL: sudo dnf install python3 python3-pip python3-tkinter"
        echo ""
        exit 1
    fi
else
    print_error "Python not found!"
    echo ""
    echo "Please install Python 3.7+ from:"
    echo "  • Ubuntu/Debian: sudo apt install python3 python3-pip python3-tk"
    echo "  • macOS: brew install python3 or download from python.org"
    echo "  • CentOS/RHEL: sudo dnf install python3 python3-pip python3-tkinter"
    echo ""
    exit 1
fi

# Set pip command
if command -v pip3 &> /dev/null; then
    PIP_CMD="pip3"
elif command -v pip &> /dev/null; then
    PIP_CMD="pip"
else
    print_error "pip not found! Please install pip3"
    exit 1
fi

# Check if main application exists
if [ ! -f "PDFToolsApp.py" ]; then
    print_error "PDFToolsApp.py not found!"
    echo ""
    echo "Please make sure all application files are in the same directory:"
    echo "  • PDFToolsApp.py (main application)"
    echo "  • PDFEngine.py (processing engine)"
    echo "  • Dependencies.txt (requirements)"
    echo ""
    exit 1
fi

# Check if dependencies are installed
print_info "Checking dependencies..."

$PYTHON_CMD -c "import pypdf, reportlab, PIL" 2>/dev/null
if [ $? -ne 0 ]; then
    echo ""
    print_info "Installing required dependencies..."
    echo "This may take a few moments..."
    echo ""
    
    # Install dependencies
    $PIP_CMD install pypdf>=3.0.0 reportlab>=4.0.0 Pillow>=10.0.0
    
    # Check if installation was successful
    $PYTHON_CMD -c "import pypdf, reportlab, PIL" 2>/dev/null
    if [ $? -ne 0 ]; then
        echo ""
        print_error "Failed to install dependencies!"
        echo ""
        echo "Please try manually:"
        echo "  $PIP_CMD install pypdf reportlab pillow"
        echo ""
        echo "If you get permission errors, try:"
        echo "  $PIP_CMD install --user pypdf reportlab pillow"
        echo ""
        exit 1
    fi
    
    print_success "Dependencies installed successfully!"
fi

print_success "All dependencies are ready!"

# Check for tkinter (GUI framework)
print_info "Checking GUI framework..."
$PYTHON_CMD -c "import tkinter" 2>/dev/null
if [ $? -ne 0 ]; then
    print_warning "tkinter not found!"
    echo ""
    echo "Please install tkinter:"
    echo "  • Ubuntu/Debian: sudo apt install python3-tk"
    echo "  • macOS: Usually included with Python from python.org"
    echo "  • CentOS/RHEL: sudo dnf install python3-tkinter"
    echo ""
    exit 1
fi

print_success "GUI framework ready!"

echo ""
echo "================================================"
echo "          Starting PDF Tools Suite..."
echo "================================================"
echo ""

# Start the application
$PYTHON_CMD PDFToolsApp.py

# Check exit code
if [ $? -ne 0 ]; then
    echo ""
    echo "================================================"
    print_error "Application encountered an error."
    echo "================================================"
    echo ""
    echo "Troubleshooting tips:"
    echo "1. Make sure all files are in the same directory"
    echo "2. Check if all dependencies are installed"
    echo "3. Try running: $PYTHON_CMD -c \\"import tkinter\\""
    echo "4. See InstallationGuide.md for detailed help"
    echo ""
    echo "Press Enter to continue..."
    read
else
    echo ""
    print_success "PDF Tools Suite closed normally."
fi
'''

with open('StartApp.sh', 'w') as f:
    f.write(startapp_sh_content)

# Make the script executable
import os
import stat

# Add execute permission
st = os.stat('StartApp.sh')
os.chmod('StartApp.sh', st.st_mode | stat.S_IEXEC)

print("✅ Created StartApp.sh (Linux/Mac launcher)")
print(f"   Size: {len(startapp_sh_content)} characters")
print("   ✅ Made executable (chmod +x)")