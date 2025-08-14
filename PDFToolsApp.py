#!/usr/bin/env python3
"""
PDF Tools Application - Professional Desktop Suite

A comprehensive desktop application for PDF document manipulation.
Features: Merge, Split, Compress, Watermark, and Password Protection.

Version: 1.0.0
License: MIT
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import os
import threading
from PDFEngine import PDFProcessor

class PDFToolsApplication:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Tools Suite - Professional Edition")
        self.root.geometry("850x650")
        self.root.configure(bg='#f8f9fa')

        # Initialize PDF processor
        self.pdf_processor = PDFProcessor()

        # Selected files list
        self.selected_files = []

        # Create modern GUI
        self.create_interface()

        # Status tracking
        self.status_var = tk.StringVar()
        self.status_var.set("Ready to process PDFs")

    def create_interface(self):
        """Create the modern professional interface"""

        # Header Section
        header_frame = tk.Frame(self.root, bg='#1e3d59', height=90)
        header_frame.pack(fill='x', padx=12, pady=(12, 0))
        header_frame.pack_propagate(False)

        # Main title
        title_label = tk.Label(
            header_frame,
            text="📄 PDF Tools Suite",
            font=('Segoe UI', 26, 'bold'),
            fg='white',
            bg='#1e3d59'
        )
        title_label.pack(expand=True, pady=(10, 0))

        # Subtitle
        subtitle_label = tk.Label(
            header_frame,
            text="Professional PDF Document Processing",
            font=('Segoe UI', 13),
            fg='#b8d4f0',
            bg='#1e3d59'
        )
        subtitle_label.pack(pady=(0, 10))

        # Main workspace
        workspace = tk.Frame(self.root, bg='#f8f9fa')
        workspace.pack(fill='both', expand=True, padx=12, pady=12)

        # Left panel - Document Management
        left_panel = tk.LabelFrame(
            workspace,
            text="📂 Document Management",
            font=('Segoe UI', 13, 'bold'),
            bg='#ffffff',
            fg='#1e3d59',
            relief='raised',
            bd=2
        )
        left_panel.pack(side='left', fill='both', expand=True, padx=(0, 8))

        # File management controls
        control_frame = tk.Frame(left_panel, bg='#ffffff')
        control_frame.pack(fill='x', padx=15, pady=15)

        select_button = tk.Button(
            control_frame,
            text="📁 Select Documents",
            command=self.select_documents,
            bg='#007bff',
            fg='white',
            font=('Segoe UI', 12, 'bold'),
            relief='flat',
            padx=25,
            pady=12,
            cursor='hand2'
        )
        select_button.pack(side='left', padx=(0, 12))

        clear_button = tk.Button(
            control_frame,
            text="🗑️ Clear All",
            command=self.clear_documents,
            bg='#dc3545',
            fg='white',
            font=('Segoe UI', 12, 'bold'),
            relief='flat',
            padx=25,
            pady=12,
            cursor='hand2'
        )
        clear_button.pack(side='left')

        # Document list display
        list_container = tk.Frame(left_panel, bg='#ffffff')
        list_container.pack(fill='both', expand=True, padx=15, pady=(0, 15))

        # Enhanced listbox with scrollbar
        list_frame = tk.Frame(list_container, bg='#ffffff')
        list_frame.pack(fill='both', expand=True)

        scrollbar = tk.Scrollbar(list_frame, bg='#e9ecef')
        scrollbar.pack(side='right', fill='y')

        self.document_list = tk.Listbox(
            list_frame,
            yscrollcommand=scrollbar.set,
            font=('Segoe UI', 11),
            bg='#f8f9fa',
            fg='#495057',
            selectmode='extended',
            relief='flat',
            bd=1,
            highlightthickness=1,
            highlightcolor='#007bff'
        )
        self.document_list.pack(side='left', fill='both', expand=True)
        scrollbar.config(command=self.document_list.yview)

        # Right panel - Operations Center
        right_panel = tk.LabelFrame(
            workspace,
            text="⚡ Operations Center",
            font=('Segoe UI', 13, 'bold'),
            bg='#ffffff',
            fg='#1e3d59',
            relief='raised',
            bd=2
        )
        right_panel.pack(side='right', fill='both', expand=True, padx=(8, 0))

        # Operation buttons with modern styling
        self.create_operation_panel(right_panel)

        # Activity log section
        log_section = tk.LabelFrame(
            right_panel,
            text="📊 Activity Log",
            font=('Segoe UI', 11, 'bold'),
            bg='#ffffff',
            fg='#6c757d'
        )
        log_section.pack(fill='both', expand=True, padx=15, pady=15)

        self.activity_log = scrolledtext.ScrolledText(
            log_section,
            height=9,
            font=('Consolas', 10),
            bg='#1a1a1a',
            fg='#00ff41',
            wrap='word',
            relief='flat',
            bd=0,
            padx=10,
            pady=8
        )
        self.activity_log.pack(fill='both', expand=True, padx=8, pady=8)

        # Status bar
        status_bar = tk.Frame(self.root, bg='#343a40', height=35)
        status_bar.pack(fill='x', side='bottom')
        status_bar.pack_propagate(False)

        self.status_display = tk.Label(
            status_bar,
            textvariable=self.status_var,
            bg='#343a40',
            fg='#ffffff',
            font=('Segoe UI', 11),
            anchor='w'
        )
        self.status_display.pack(side='left', padx=15, pady=8)

    def create_operation_panel(self, parent):
        """Create the operations panel with modern buttons"""

        operations = [
            ("🔗 Merge Documents", self.merge_documents, "#28a745"),
            ("✂️ Split Document", self.split_document, "#ffc107"),
            ("📦 Compress Files", self.compress_documents, "#6f42c1"),
            ("🏷️ Add Watermark", self.add_watermark, "#fd7e14"),
            ("🔒 Secure Documents", self.secure_documents, "#dc3545"),
            ("🔓 Unlock Documents", self.unlock_documents, "#20c997")
        ]

        # Create button grid
        button_frame = tk.Frame(parent, bg='#ffffff')
        button_frame.pack(fill='x', padx=15, pady=15)

        for i, (text, command, color) in enumerate(operations):
            row = i // 2
            col = i % 2

            button = tk.Button(
                button_frame,
                text=text,
                command=command,
                bg=color,
                fg='white',
                font=('Segoe UI', 12, 'bold'),
                relief='flat',
                padx=20,
                pady=15,
                cursor='hand2',
                width=18
            )
            button.grid(row=row, column=col, padx=8, pady=8, sticky='ew')

        # Configure grid weights
        button_frame.grid_columnconfigure(0, weight=1)
        button_frame.grid_columnconfigure(1, weight=1)

    def select_documents(self):
        """Select PDF documents for processing"""
        files = filedialog.askopenfilenames(
            title="Select PDF Documents",
            filetypes=[("PDF Documents", "*.pdf"), ("All Files", "*.*")]
        )

        for file in files:
            if file not in self.selected_files:
                self.selected_files.append(file)
                filename = os.path.basename(file)
                self.document_list.insert('end', f"📄 {filename}")

        self.log_activity(f"Added {len(files)} document(s) to processing queue")
        self.update_status(f"{len(self.selected_files)} documents ready for processing")

    def clear_documents(self):
        """Clear all selected documents"""
        self.selected_files.clear()
        self.document_list.delete(0, 'end')
        self.log_activity("Document queue cleared")
        self.update_status("Ready to process PDFs")

    def log_activity(self, message):
        """Log activity with timestamp"""
        from datetime import datetime
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.activity_log.insert('end', f"[{timestamp}] {message}\n")
        self.activity_log.see('end')
        self.root.update()

    def update_status(self, message):
        """Update status bar"""
        self.status_var.set(message)
        self.root.update()

    def execute_operation(self, operation_func, *args):
        """Execute operation in background thread"""
        def worker():
            try:
                operation_func(*args)
            except Exception as e:
                self.log_activity(f"❌ Operation failed: {str(e)}")
                messagebox.showerror("Process Error", f"Operation failed: {str(e)}")
            finally:
                self.update_status("Ready to process PDFs")

        thread = threading.Thread(target=worker, daemon=True)
        thread.start()

    def merge_documents(self):
        """Merge selected PDF documents"""
        if len(self.selected_files) < 2:
            messagebox.showwarning("Insufficient Documents", "Please select at least 2 PDF documents to merge")
            return

        output_file = filedialog.asksaveasfilename(
            title="Save Merged Document As",
            defaultextension=".pdf",
            filetypes=[("PDF Documents", "*.pdf")]
        )

        if output_file:
            self.update_status("Merging documents...")
            self.log_activity(f"🔗 Merging {len(self.selected_files)} documents...")
            self.execute_operation(self._merge_worker, output_file)

    def _merge_worker(self, output_file):
        """Background worker for merging"""
        success = self.pdf_processor.merge_documents(self.selected_files, output_file)
        if success:
            self.log_activity(f"✅ Documents merged successfully: {os.path.basename(output_file)}")
            messagebox.showinfo("Success", f"Documents merged successfully!\nSaved as: {os.path.basename(output_file)}")
        else:
            raise Exception("Document merge operation failed")

    def split_document(self):
        """Split selected PDF document"""
        if len(self.selected_files) != 1:
            messagebox.showwarning("Document Selection", "Please select exactly 1 PDF document to split")
            return

        output_dir = filedialog.askdirectory(title="Select Output Directory for Split Documents")
        if output_dir:
            self.update_status("Splitting document...")
            self.log_activity(f"✂️ Splitting document: {os.path.basename(self.selected_files[0])}")
            self.execute_operation(self._split_worker, self.selected_files[0], output_dir)

    def _split_worker(self, input_file, output_dir):
        """Background worker for splitting"""
        pages_count = self.pdf_processor.split_document(input_file, output_dir)
        if pages_count > 0:
            self.log_activity(f"✅ Document split into {pages_count} pages")
            messagebox.showinfo("Success", f"Document split into {pages_count} pages!\nFiles saved in: {output_dir}")
        else:
            raise Exception("Document split operation failed")

    def compress_documents(self):
        """Compress selected PDF documents"""
        if not self.selected_files:
            messagebox.showwarning("No Documents", "Please select PDF documents to compress")
            return

        output_dir = filedialog.askdirectory(title="Select Output Directory for Compressed Documents")
        if output_dir:
            self.update_status("Compressing documents...")
            self.log_activity(f"📦 Compressing {len(self.selected_files)} document(s)...")
            self.execute_operation(self._compress_worker, output_dir)

    def _compress_worker(self, output_dir):
        """Background worker for compression"""
        compressed_count = 0
        for file_path in self.selected_files:
            filename = os.path.basename(file_path)
            output_file = os.path.join(output_dir, f"compressed_{filename}")

            if self.pdf_processor.compress_document(file_path, output_file):
                compressed_count += 1
                self.log_activity(f"✅ Compressed: {filename}")
            else:
                self.log_activity(f"❌ Failed to compress: {filename}")

        messagebox.showinfo("Compression Complete", f"Compressed {compressed_count}/{len(self.selected_files)} documents!\nSaved in: {output_dir}")

    def add_watermark(self):
        """Add watermark to PDF documents"""
        if not self.selected_files:
            messagebox.showwarning("No Documents", "Please select PDF documents")
            return

        watermark_text = tk.simpledialog.askstring(
            "Watermark Text",
            "Enter watermark text:",
            initialvalue="CONFIDENTIAL"
        )

        if watermark_text:
            output_dir = filedialog.askdirectory(title="Select Output Directory")
            if output_dir:
                self.update_status("Adding watermarks...")
                self.log_activity(f"🏷️ Adding watermark: '{watermark_text}'")
                self.execute_operation(self._watermark_worker, watermark_text, output_dir)

    def _watermark_worker(self, watermark_text, output_dir):
        """Background worker for watermarking"""
        watermarked_count = 0
        for file_path in self.selected_files:
            filename = os.path.basename(file_path)
            output_file = os.path.join(output_dir, f"watermarked_{filename}")

            if self.pdf_processor.add_watermark(file_path, output_file, watermark_text):
                watermarked_count += 1
                self.log_activity(f"✅ Watermarked: {filename}")
            else:
                self.log_activity(f"❌ Failed to watermark: {filename}")

        messagebox.showinfo("Watermarking Complete", f"Watermarked {watermarked_count}/{len(self.selected_files)} documents!")

    def secure_documents(self):
        """Add password protection to PDF documents"""
        if not self.selected_files:
            messagebox.showwarning("No Documents", "Please select PDF documents")
            return

        password = tk.simpledialog.askstring(
            "Document Security",
            "Enter password for protection:",
            show='*'
        )

        if password:
            output_dir = filedialog.askdirectory(title="Select Output Directory")
            if output_dir:
                self.update_status("Securing documents...")
                self.log_activity("🔒 Adding password protection...")
                self.execute_operation(self._secure_worker, password, output_dir)

    def _secure_worker(self, password, output_dir):
        """Background worker for password protection"""
        secured_count = 0
        for file_path in self.selected_files:
            filename = os.path.basename(file_path)
            output_file = os.path.join(output_dir, f"secured_{filename}")

            if self.pdf_processor.secure_document(file_path, output_file, password):
                secured_count += 1
                self.log_activity(f"✅ Secured: {filename}")
            else:
                self.log_activity(f"❌ Failed to secure: {filename}")

        messagebox.showinfo("Security Complete", f"Secured {secured_count}/{len(self.selected_files)} documents!")

    def unlock_documents(self):
        """Remove password protection from PDF documents"""
        if not self.selected_files:
            messagebox.showwarning("No Documents", "Please select PDF documents")
            return

        password = tk.simpledialog.askstring(
            "Document Unlock",
            "Enter current password:",
            show='*'
        )

        if password:
            output_dir = filedialog.askdirectory(title="Select Output Directory")
            if output_dir:
                self.update_status("Unlocking documents...")
                self.log_activity("🔓 Removing password protection...")
                self.execute_operation(self._unlock_worker, password, output_dir)

    def _unlock_worker(self, password, output_dir):
        """Background worker for password removal"""
        unlocked_count = 0
        for file_path in self.selected_files:
            filename = os.path.basename(file_path)
            output_file = os.path.join(output_dir, f"unlocked_{filename}")

            if self.pdf_processor.unlock_document(file_path, output_file, password):
                unlocked_count += 1
                self.log_activity(f"✅ Unlocked: {filename}")
            else:
                self.log_activity(f"❌ Failed to unlock: {filename}")

        messagebox.showinfo("Unlock Complete", f"Unlocked {unlocked_count}/{len(self.selected_files)} documents!")


def launch_application():
    """Launch the PDF Tools Application"""
    try:
        import tkinter.simpledialog

        root = tk.Tk()

        # Set application icon (if available)
        try:
            root.iconbitmap('app_icon.ico')
        except:
            pass

        # Center window on screen
        root.update_idletasks()
        x = (root.winfo_screenwidth() // 2) - (850 // 2)
        y = (root.winfo_screenheight() // 2) - (650 // 2)
        root.geometry(f"850x650+{x}+{y}")

        app = PDFToolsApplication(root)

        # Start the application
        root.mainloop()

    except ImportError as e:
        print(f"Error: Missing required module - {e}")
        print("Please install required dependencies:")
        print("pip install pypdf reportlab pillow")
    except Exception as e:
        print(f"Error starting application: {e}")


if __name__ == "__main__":
    launch_application()
