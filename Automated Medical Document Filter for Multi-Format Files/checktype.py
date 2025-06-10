import os
import shutil
import fitz  
import docx
MEDICAL_KEYWORDS = {"diagnosis", "prescription", "patient", "disease", "treatment", "doctor", "surgery", "medicine"}
ACCEPTED_FOLDER = "accepted_files"
os.makedirs(ACCEPTED_FOLDER, exist_ok=True)
def extract_text_from_pdf(file_path):
    text = ""
    with fitz.open(file_path) as doc:
        for page in doc:
            text += page.get_text()
    return text.strip().lower()
def extract_text_from_docx(file_path):
    doc = docx.Document(file_path)
    text = " ".join([para.text for para in doc.paragraphs]).strip()
    return text.lower()
def extract_text_from_txt(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read().strip().lower()
def move_file(file_path):
    new_path = os.path.join(ACCEPTED_FOLDER, os.path.basename(file_path))
    shutil.move(file_path, new_path)
    return new_path
def is_medical_document(file_path):
    extension = os.path.splitext(file_path)[1].lower()
    if extension not in {".pdf", ".docx", ".txt"}:
        new_path = move_file(file_path)
        return f"Accepted without checking -> {new_path}"
    if extension == ".pdf":
        text = extract_text_from_pdf(file_path)
    elif extension == ".docx":
        text = extract_text_from_docx(file_path)
    elif extension == ".txt":
        text = extract_text_from_txt(file_path)
    if not text:
        new_path = move_file(file_path)
        return f"Accepted (Empty Document) -> {new_path}"
    keyword_count = sum(word in text for word in MEDICAL_KEYWORDS)
    if keyword_count >= 3:
        new_path = move_file(file_path)
        return f"Accepted (Medical Document) -> {new_path}"
    else:
        return "Rejected (Non-Medical Document)"
def process_folder(folder_path):
    if not os.path.isdir(folder_path):
        return "Invalid folder path"
    results = []
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            result = is_medical_document(file_path)
            results.append(result)
    return results
input_path = "D:\\mynive\\wholefold" 
if os.path.isdir(input_path):
    results = process_folder(input_path)
    for res in results:
        print(res)
elif os.path.isfile(input_path):
    result = is_medical_document(input_path)
    print(result)
else:
    print("Invalid path")