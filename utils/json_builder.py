import json

def build_json(text_data, image_data, output_file="output.json"):
    content = []

    for i, text in enumerate(text_data):
        page_content = {
            "page": i + 1,
            "text": text.strip(),
            "images": image_data[i]["images"] if i < len(image_data) else []
        }
        content.append(page_content)

    try:
        with open(output_file, "w") as f:
            json.dump(content, f, indent=4)
        print(f"[SUCCESS] JSON saved as '{output_file}'")
    except Exception as e:
        print(f"[ERROR] Failed to save JSON: {e}")
