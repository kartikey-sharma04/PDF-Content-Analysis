# 📘 AI Internship Assignment – PDF Content Extraction & Analysis

This project was completed as part of an AI/Python Internship assignment. The task was to build a Python-based tool that extracts structured content (text and images) from a PDF and saves the data in a structured JSON format.

> 🔍 **PDF used**: [Attention Is All You Need (Vaswani et al., 2017)](https://arxiv.org/abs/1706.03762)

---

## ✅ Features

- Extracts **all text content** from a PDF file (page by page).
- Extracts **all embedded images** and saves them separately.
- Generates a **structured JSON** file combining text and corresponding image paths.

---

## 📁 Project Structure

├── main.py # Main controller script
├── utils/
│ ├── text_extractor.py # Extracts text from each page
│ ├── image_extractor.py # Extracts and saves images
│ └── json_builder.py # Combines text & images into JSON
├── images/ # Folder to store extracted images
├── output.json # Final structured data
└── requirements.txt # List of required Python packages


---

## ⚙️ Setup Instructions

1. **Clone or download the repo**
2. Place your target PDF (e.g., `Attention_is_all_you_need.pdf`) in the project root.
3. Make sure Python 3.7+ is installed.

### 🔧 Install dependencies:

```bash
pip install -r requirements.txt

to run
python main.py

