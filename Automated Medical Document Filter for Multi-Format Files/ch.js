const fs = require('fs');
const path = require('path');
const pdfParse = require('pdf-parse');
const MEDICAL_KEYWORDS = new Set(["diagnosis", "prescription", "patient", "disease", "treatment", "doctor", "surgery", "medicine"]);
const ACCEPTED_FOLDER = "accepted_files";
if (!fs.existsSync(ACCEPTED_FOLDER)) {
    fs.mkdirSync(ACCEPTED_FOLDER);
}
async function extractTextFromPDF(filePath) {
    const data = await pdfParse(fs.readFileSync(filePath));
    return data.text.toLowerCase().trim();
}
function moveFile(filePath) {
    const newPath = path.join(ACCEPTED_FOLDER, path.basename(filePath));
    fs.renameSync(filePath, newPath);
    return newPath;
}
async function isMedicalDocument(filePath) {
    const ext = path.extname(filePath).toLowerCase();
    if ([".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"].includes(ext)) {
        return `Accepted (Image File) -> ${moveFile(filePath)}`;
    }
    if (ext !== ".pdf") {
        return `Rejected (Unsupported File Type) -> ${filePath}`;
    }
    const text = await extractTextFromPDF(filePath);
    if (!text) {
        return `Accepted (Empty PDF) -> ${moveFile(filePath)}`;
    }
    const keywordCount = Array.from(MEDICAL_KEYWORDS).filter(word => text.includes(word)).length;
    if (keywordCount >= 3) {
        return `Accepted (Medical PDF) -> ${moveFile(filePath)}`;
    } else {
        return `Rejected (Non-Medical PDF)`;
    }
}

async function processFolder(folderPath) {
    if (!fs.existsSync(folderPath) || !fs.lstatSync(folderPath).isDirectory()) {
        return "Invalid folder path";
    }
    const files = fs.readdirSync(folderPath);
    const results = [];
    for (const file of files) {
        const filePath = path.join(folderPath, file);
        const result = await isMedicalDocument(filePath);
        results.push(result);
    }
    return results;
}
(async () => {
    const folderPath = "D:\\mynive\\wholefold"; 
    const results = await processFolder(folderPath);
    results.forEach(res => console.log(res));
})();