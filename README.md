# 🔧 PDF Tools - All-in-One PDF Manipulation

A simple, powerful desktop application for PDF manipulation with an intuitive GUI.

![Python](https://img.shields.io/badge/python-v3.7+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![GUI](https://img.shields.io/badge/GUI-tkinter-orange.svg)

## ✨ Features

🔗 **Merge PDFs** - Combine multiple PDF files into one document  
✂️ **Split PDFs** - Break a PDF into individual pages  
📦 **Compress PDFs** - Reduce file size while maintaining quality  
🏷️ **Add Watermarks** - Protect your documents with custom text  
🔒 **Password Protection** - Secure PDFs with password encryption  
🔓 **Remove Passwords** - Unlock protected PDFs  

## 🚀 Quick Start

### Installation

1. **Clone or download this repository**
```bash
git clone https://github.com/yourusername/pdf-tools.git
cd pdf-tools
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the application**
```bash
python pdf_tools.py
```

### System Requirements

- Python 3.7 or higher
- Windows, macOS, or Linux
- tkinter (usually included with Python)

## 📱 How to Use

1. **Launch the application**
   ```bash
   python pdf_tools.py
   ```

2. **Select PDF files**
   - Click "🔍 Select PDF Files" to choose your files
   - Selected files will appear in the list

3. **Choose an operation**
   - **Merge**: Combine multiple PDFs into one
   - **Split**: Break a PDF into separate pages
   - **Compress**: Reduce file size
   - **Watermark**: Add protective text overlay
   - **Protect**: Add password protection
   - **Unlock**: Remove password protection

4. **Follow the prompts**
   - Choose output location
   - Enter required information (passwords, watermark text)
   - Watch the progress in the log window

## 💡 Use Cases

### Personal Use
- **Organize documents**: Merge related PDFs into single files
- **Reduce storage**: Compress large PDFs for email or storage
- **Privacy protection**: Add watermarks or passwords to sensitive documents
- **Document preparation**: Split large PDFs for easier sharing

### Professional Use  
- **Legal documents**: Merge contracts and supporting documents
- **Reports**: Combine charts, data, and text into comprehensive reports
- **Presentations**: Split presentation PDFs for individual distribution
- **Client work**: Add watermarks to protect intellectual property

### Student Use
- **Research papers**: Merge research sources and notes
- **Assignments**: Combine multiple assignment parts
- **Study materials**: Organize and compress textbooks/materials

## 🛠 Technical Details

### Architecture
- **GUI**: tkinter for cross-platform desktop interface
- **PDF Engine**: pypdf/PyPDF2 for core PDF operations
- **Watermarking**: ReportLab for advanced text overlays
- **Threading**: Background processing for responsive UI

### File Structure
```
pdf-tools/
├── pdf_tools.py          # Main GUI application
├── pdf_operations.py     # Core PDF manipulation functions  
├── requirements.txt      # Python dependencies
├── README.md            # This file
└── .gitignore          # Git ignore patterns
```

### Core Functions
- `merge_pdfs()` - Combine multiple PDFs
- `split_pdf()` - Extract individual pages
- `compress_pdf()` - Optimize file size
- `add_watermark()` - Apply text overlays
- `password_protect()` - Add encryption
- `remove_password()` - Remove encryption

## 🔧 Command Line Usage

You can also use the core functions from command line:

```bash
# Merge PDFs
python pdf_operations.py merge output.pdf file1.pdf file2.pdf file3.pdf

# Split PDF
python pdf_operations.py split input.pdf output_directory/

# Compress PDF
python pdf_operations.py compress input.pdf compressed_output.pdf

# Get PDF info
python pdf_operations.py info document.pdf
```

## 🐛 Troubleshooting

### Common Issues

**"Module not found" error**
```bash
pip install pypdf reportlab pillow
```

**GUI doesn't appear on Linux**
```bash
sudo apt-get install python3-tk
```

**Permission errors**
- Ensure you have write permissions to output directories
- Close PDFs in other applications before processing

**Password protection not working**
- Ensure you're using pypdf>=3.0.0
- Some very old PDFs may not support modern encryption

### Performance Tips
- **Large files**: Split very large PDFs into smaller chunks first
- **Batch processing**: Process files in smaller batches for better performance
- **Memory usage**: Close the application between processing large batches

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Report bugs** - Create an issue with details and steps to reproduce
2. **Suggest features** - Open an issue with your feature request
3. **Submit code** - Fork, create a branch, and submit a pull request

### Development Setup
```bash
git clone https://github.com/yourusername/pdf-tools.git
cd pdf-tools
pip install -r requirements.txt
python pdf_tools.py
```

## 📋 Changelog

### Version 1.0.0
- Initial release
- GUI application with tkinter
- Core PDF operations (merge, split, compress)
- Watermarking and password protection
- Cross-platform compatibility

## 🔮 Future Features

- [ ] Drag & drop file interface
- [ ] Batch processing automation
- [ ] PDF form editing
- [ ] OCR text recognition
- [ ] Cloud storage integration
- [ ] Dark mode theme
- [ ] Multi-language support

## 📄 License

MIT License - see LICENSE file for details

## 🙏 Acknowledgments

- **pypdf** - Excellent Python PDF library
- **ReportLab** - Professional PDF generation
- **tkinter** - Built-in Python GUI framework

---

**Made with ❤️ for PDF productivity**

*Star this repo if it helped you! ⭐*

## Support

If you find this tool useful, consider:
- ⭐ Starring the repository
- 🐛 Reporting bugs
- 💡 Suggesting new features
- 🤝 Contributing code

**Happy PDF processing!** 🎉
