from utils.text_extractor import extract_text
from utils.image_extractor import extract_images
from utils.json_builder import build_json

pdf_file = r"D:\Testline\1706.03762v7 (1).pdf"

def main():
    print("📘 Starting PDF content analysis...")

   
    text_data = extract_text(pdf_file)

 
    image_data = extract_images(pdf_file, output_folder="images")

   
    build_json(text_data, image_data, output_file="output.json")

    print("All tasks completed. Check 'images/' and 'output.json'.")

if __name__ == "__main__":
    main()
