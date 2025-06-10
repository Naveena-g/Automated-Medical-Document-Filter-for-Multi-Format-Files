# 📁 Medical Document Classifier – Python & Node.js

### 🔍 Detect, Filter, and Sort Medical Records from Mixed File Inputs

## 📝 Overview

This project provides two implementations — one in **Python** and another in **Node.js** — to **analyze and classify files** (PDF, DOCX, TXT, and common image formats) as **medical or non-medical documents** based on keyword detection.

The classifier works by:
**Extracting text** from supported file types
**Searching for medical keywords**
**Accepting or rejecting files** based on a match threshold
**Automatically moving accepted files** to a dedicated folder


## 📦 Features

✅ Supports multiple formats: `.pdf`, `.docx`, `.txt`, and common image formats
✅ Medical keyword detection
✅ Accepts empty or image-only files
✅ Automatic file moving for accepted documents
✅ Recursive folder processing (Python)
✅ Asynchronous processing (Node.js)

## 🛠️ Technologies Used

### Python:

* `PyMuPDF` (fitz) for PDF parsing
* `python-docx` for DOCX parsing
* Standard libraries: `os`, `shutil`

### Node.js:

* `pdf-parse` for PDF content extraction
* `fs` and `path` for file handling



## 📂 Folder Structure

```
📁 accepted_files/       <- Stores accepted documents
📁 your_input_folder/    <- Place your files here to be processed
📄 check_medical.py      <- Python script
📄 checkMedical.js       <- Node.js script
```


## 🚀 Getting Started

### Python

```bash
pip install python-docx pymupdf
python check_medical.py
```

### Node.js

```bash
npm install pdf-parse
node checkMedical.js
```

Make sure to update the folder path in both scripts before running.

## 📌 Medical Keywords Used

```
diagnosis, prescription, patient, disease, treatment,
doctor, surgery, medicine
```


## 🧪 Sample Output

```
Accepted (Medical Document) -> accepted_files/prescription.pdf
Rejected (Non-Medical Document)
Accepted without checking -> accepted_files/image.png
```
