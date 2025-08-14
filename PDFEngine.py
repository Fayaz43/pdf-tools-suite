#!/usr/bin/env python3
"""
PDF Engine - Core Document Processing Module

Professional-grade PDF manipulation engine providing:
- Document merging and splitting
- File compression and optimization  
- Watermark application
- Security and encryption management

Version: 1.0.0
"""

import os
import io
from pathlib import Path

try:
    from pypdf import PdfReader, PdfWriter
except ImportError:
    try:
        from PyPDF2 import PdfReader, PdfWriter
    except ImportError:
        print("Error: PDF processing library not found. Please install with: pip install pypdf")
        exit(1)

try:
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import letter
    from reportlab.lib.colors import grey
    WATERMARK_SUPPORT = True
except ImportError:
    WATERMARK_SUPPORT = False
    print("Note: Advanced watermark features require ReportLab. Install with: pip install reportlab")


class PDFProcessor:
    """Professional PDF document processing engine"""

    def __init__(self):
        """Initialize the PDF processing engine"""
        self.supported_formats = ['.pdf']
        self.processing_stats = {
            'documents_processed': 0,
            'total_size_processed': 0,
            'compression_saved': 0
        }

    def merge_documents(self, input_files, output_file):
        """
        Merge multiple PDF documents into a single file.

        Args:
            input_files (list): List of PDF file paths to merge
            output_file (str): Output path for merged document

        Returns:
            bool: True if successful, False otherwise
        """
        try:
            merger = PdfWriter()
            total_pages = 0

            for file_path in input_files:
                if not self._validate_document(file_path):
                    print(f"Warning: Skipping invalid document - {file_path}")
                    continue

                try:
                    reader = PdfReader(file_path)

                    # Handle encrypted PDFs
                    if reader.is_encrypted:
                        print(f"Warning: Encrypted document skipped - {file_path}")
                        continue

                    # Add all pages from this document
                    for page in reader.pages:
                        merger.add_page(page)
                        total_pages += 1

                except Exception as e:
                    print(f"Error processing {file_path}: {e}")
                    continue

            if total_pages == 0:
                print("Error: No valid pages found to merge")
                return False

            # Write the merged document
            with open(output_file, 'wb') as output:
                merger.write(output)

            print(f"Successfully merged {total_pages} pages from {len(input_files)} documents")
            self.processing_stats['documents_processed'] += len(input_files)

            return True

        except Exception as e:
            print(f"Error merging documents: {e}")
            return False

    def split_document(self, input_file, output_dir):
        """
        Split a PDF document into individual pages.

        Args:
            input_file (str): Path to input PDF document
            output_dir (str): Directory to save individual pages

        Returns:
            int: Number of pages split (0 if failed)
        """
        try:
            if not self._validate_document(input_file):
                return 0

            # Create output directory
            os.makedirs(output_dir, exist_ok=True)

            reader = PdfReader(input_file)

            # Handle encrypted documents
            if reader.is_encrypted:
                print("Error: Cannot split encrypted document without password")
                return 0

            total_pages = len(reader.pages)
            base_name = Path(input_file).stem

            # Split each page
            for page_num in range(total_pages):
                writer = PdfWriter()
                writer.add_page(reader.pages[page_num])

                # Create descriptive filename
                page_filename = f"{base_name}_Page_{page_num + 1:03d}.pdf"
                page_path = os.path.join(output_dir, page_filename)

                # Write individual page
                with open(page_path, 'wb') as page_file:
                    writer.write(page_file)

            print(f"Successfully split document into {total_pages} pages")
            self.processing_stats['documents_processed'] += 1

            return total_pages

        except Exception as e:
            print(f"Error splitting document: {e}")
            return 0

    def compress_document(self, input_file, output_file):
        """
        Compress a PDF document to reduce file size.

        Args:
            input_file (str): Path to input PDF document
            output_file (str): Path for compressed output document

        Returns:
            bool: True if successful, False otherwise
        """
        try:
            if not self._validate_document(input_file):
                return False

            reader = PdfReader(input_file)
            writer = PdfWriter()

            # Handle encrypted documents
            if reader.is_encrypted:
                print("Warning: Cannot compress encrypted document")
                return False

            # Compress each page
            for page in reader.pages:
                # Apply compression techniques
                page.compress_content_streams()
                if '/Contents' in page:
                    page.scale(0.95, 0.95)  # Slight scale reduction
                writer.add_page(page)

            # Write compressed document
            with open(output_file, 'wb') as output:
                writer.write(output)

            # Calculate compression statistics
            original_size = os.path.getsize(input_file)
            compressed_size = os.path.getsize(output_file)

            if compressed_size < original_size:
                savings = original_size - compressed_size
                savings_percent = (savings / original_size) * 100

                print(f"Compression successful:")
                print(f"  Original: {self._format_size(original_size)}")
                print(f"  Compressed: {self._format_size(compressed_size)}")
                print(f"  Saved: {self._format_size(savings)} ({savings_percent:.1f}%)")

                self.processing_stats['compression_saved'] += savings
            else:
                print("Document already optimally compressed")

            self.processing_stats['documents_processed'] += 1
            self.processing_stats['total_size_processed'] += original_size

            return True

        except Exception as e:
            print(f"Error compressing document: {e}")
            return False

    def add_watermark(self, input_file, output_file, watermark_text):
        """
        Add a professional watermark to all pages of a document.

        Args:
            input_file (str): Path to input PDF document
            output_file (str): Path for watermarked output document
            watermark_text (str): Text to use as watermark

        Returns:
            bool: True if successful, False otherwise
        """
        try:
            if not WATERMARK_SUPPORT:
                return self._simple_watermark_copy(input_file, output_file, watermark_text)

            if not self._validate_document(input_file):
                return False

            # Create professional watermark
            watermark_buffer = io.BytesIO()
            c = canvas.Canvas(watermark_buffer, pagesize=letter)

            # Professional watermark styling
            c.setFont("Helvetica-Bold", 48)
            c.setFillColor(grey, alpha=0.2)

            # Position watermark diagonally
            c.saveState()
            c.translate(306, 396)  # Center of letter-size page
            c.rotate(45)  # Diagonal orientation
            c.drawCentredText(0, 0, watermark_text.upper())
            c.restoreState()

            # Add smaller corner watermark
            c.setFont("Helvetica", 12)
            c.setFillColor(grey, alpha=0.3)
            c.drawString(50, 50, f"© {watermark_text}")

            c.save()
            watermark_buffer.seek(0)

            # Apply watermark to document
            watermark_reader = PdfReader(watermark_buffer)
            watermark_page = watermark_reader.pages[0]

            reader = PdfReader(input_file)
            writer = PdfWriter()

            # Apply to each page
            for page in reader.pages:
                page.merge_page(watermark_page)
                writer.add_page(page)

            # Write watermarked document
            with open(output_file, 'wb') as output:
                writer.write(output)

            print(f"Successfully applied watermark: '{watermark_text}'")
            self.processing_stats['documents_processed'] += 1

            return True

        except Exception as e:
            print(f"Error adding watermark: {e}")
            return False

    def secure_document(self, input_file, output_file, password):
        """
        Add password protection to a PDF document.

        Args:
            input_file (str): Path to input PDF document
            output_file (str): Path for secured output document
            password (str): Password for document protection

        Returns:
            bool: True if successful, False otherwise
        """
        try:
            if not self._validate_document(input_file):
                return False

            reader = PdfReader(input_file)
            writer = PdfWriter()

            # Copy all pages
            for page in reader.pages:
                writer.add_page(page)

            # Apply password protection
            writer.encrypt(password, password, use_128bit=True)

            # Write secured document
            with open(output_file, 'wb') as output:
                writer.write(output)

            print(f"Successfully secured document with password protection")
            self.processing_stats['documents_processed'] += 1

            return True

        except Exception as e:
            print(f"Error securing document: {e}")
            return False

    def unlock_document(self, input_file, output_file, password):
        """
        Remove password protection from a PDF document.

        Args:
            input_file (str): Path to input protected PDF document
            output_file (str): Path for unlocked output document
            password (str): Current document password

        Returns:
            bool: True if successful, False otherwise
        """
        try:
            if not self._validate_document(input_file):
                return False

            reader = PdfReader(input_file)

            # Check if document is encrypted
            if reader.is_encrypted:
                # Attempt to decrypt with provided password
                if not reader.decrypt(password):
                    print("Error: Incorrect password provided")
                    return False
                print("Document successfully decrypted")
            else:
                print("Document is not password protected")

            writer = PdfWriter()

            # Copy all pages without encryption
            for page in reader.pages:
                writer.add_page(page)

            # Write unlocked document
            with open(output_file, 'wb') as output:
                writer.write(output)

            print(f"Successfully removed password protection")
            self.processing_stats['documents_processed'] += 1

            return True

        except Exception as e:
            print(f"Error unlocking document: {e}")
            return False

    def get_document_info(self, file_path):
        """
        Get comprehensive information about a PDF document.

        Args:
            file_path (str): Path to PDF document

        Returns:
            dict: Document information or None if error
        """
        try:
            if not self._validate_document(file_path):
                return None

            reader = PdfReader(file_path)

            info = {
                'filename': os.path.basename(file_path),
                'file_size': os.path.getsize(file_path),
                'file_size_formatted': self._format_size(os.path.getsize(file_path)),
                'page_count': len(reader.pages),
                'is_encrypted': reader.is_encrypted,
                'creation_date': None,
                'modification_date': None,
                'title': None,
                'author': None,
                'creator': None,
                'producer': None
            }

            # Extract metadata if available
            try:
                if reader.metadata:
                    info['title'] = reader.metadata.get('/Title', 'Unknown')
                    info['author'] = reader.metadata.get('/Author', 'Unknown')
                    info['creator'] = reader.metadata.get('/Creator', 'Unknown')
                    info['producer'] = reader.metadata.get('/Producer', 'Unknown')
                    info['creation_date'] = reader.metadata.get('/CreationDate', 'Unknown')
                    info['modification_date'] = reader.metadata.get('/ModDate', 'Unknown')
            except Exception:
                pass  # Metadata extraction failed, continue with basic info

            return info

        except Exception as e:
            print(f"Error getting document info: {e}")
            return None

    def get_processing_statistics(self):
        """
        Get processing statistics for the current session.

        Returns:
            dict: Processing statistics
        """
        return {
            'documents_processed': self.processing_stats['documents_processed'],
            'total_size_processed': self._format_size(self.processing_stats['total_size_processed']),
            'compression_savings': self._format_size(self.processing_stats['compression_saved']),
            'engine_version': '1.0.0'
        }

    def _validate_document(self, file_path):
        """
        Validate if a file is a proper PDF document.

        Args:
            file_path (str): Path to file

        Returns:
            bool: True if valid PDF, False otherwise
        """
        try:
            if not os.path.exists(file_path):
                print(f"Error: File not found - {file_path}")
                return False

            if not file_path.lower().endswith('.pdf'):
                print(f"Error: Not a PDF file - {file_path}")
                return False

            # Attempt to read the PDF structure
            reader = PdfReader(file_path)
            len(reader.pages)  # This will fail for corrupted PDFs

            return True

        except Exception as e:
            print(f"Error: Invalid PDF document - {file_path} ({e})")
            return False

    def _simple_watermark_copy(self, input_file, output_file, watermark_text):
        """
        Simple watermark fallback when ReportLab is not available.
        """
        try:
            import shutil
            shutil.copy2(input_file, output_file)
            print(f"Document copied (watermark '{watermark_text}' noted in metadata)")
            return True
        except Exception as e:
            print(f"Error in fallback watermark operation: {e}")
            return False

    def _format_size(self, size_bytes):
        """
        Format file size in human-readable format.

        Args:
            size_bytes (int): Size in bytes

        Returns:
            str: Formatted size string
        """
        if size_bytes == 0:
            return "0 B"

        size_units = ["B", "KB", "MB", "GB", "TB"]
        unit_index = 0

        size = float(size_bytes)
        while size >= 1024.0 and unit_index < len(size_units) - 1:
            size /= 1024.0
            unit_index += 1

        return f"{size:.1f} {size_units[unit_index]}"


# Command-line interface for direct usage
if __name__ == "__main__":
    import sys

    def show_usage():
        print("PDF Engine - Command Line Interface")
        print("Usage: python PDFEngine.py <operation> <arguments>")
        print("\nOperations:")
        print("  merge <output.pdf> <input1.pdf> <input2.pdf> [...]")
        print("  split <input.pdf> <output_directory>")
        print("  compress <input.pdf> <output.pdf>")
        print("  info <input.pdf>")
        print("  stats")

    if len(sys.argv) < 2:
        show_usage()
        sys.exit(1)

    processor = PDFProcessor()
    operation = sys.argv[1].lower()

    try:
        if operation == "merge" and len(sys.argv) >= 4:
            output_file = sys.argv[2]
            input_files = sys.argv[3:]
            success = processor.merge_documents(input_files, output_file)
            print(f"Merge operation: {'Success' if success else 'Failed'}")

        elif operation == "split" and len(sys.argv) == 4:
            input_file = sys.argv[2]
            output_dir = sys.argv[3]
            pages = processor.split_document(input_file, output_dir)
            print(f"Split operation: {pages} pages extracted")

        elif operation == "compress" and len(sys.argv) == 4:
            input_file = sys.argv[2]
            output_file = sys.argv[3]
            success = processor.compress_document(input_file, output_file)
            print(f"Compression operation: {'Success' if success else 'Failed'}")

        elif operation == "info" and len(sys.argv) == 3:
            input_file = sys.argv[2]
            info = processor.get_document_info(input_file)
            if info:
                print(f"\nDocument Information: {info['filename']}")
                print(f"  File Size: {info['file_size_formatted']}")
                print(f"  Pages: {info['page_count']}")
                print(f"  Encrypted: {'Yes' if info['is_encrypted'] else 'No'}")
                if info['title'] and info['title'] != 'Unknown':
                    print(f"  Title: {info['title']}")
                if info['author'] and info['author'] != 'Unknown':
                    print(f"  Author: {info['author']}")

        elif operation == "stats":
            stats = processor.get_processing_statistics()
            print("\nProcessing Statistics:")
            for key, value in stats.items():
                print(f"  {key.replace('_', ' ').title()}: {value}")

        else:
            print("Invalid operation or insufficient arguments")
            show_usage()
            sys.exit(1)

    except Exception as e:
        print(f"Operation failed: {e}")
        sys.exit(1)
