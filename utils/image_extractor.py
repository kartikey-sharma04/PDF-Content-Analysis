import fitz
import os

def extract_images(pdf_path, output_folder="images"):
    os.makedirs(output_folder, exist_ok=True)
    image_data = []

    try:
        doc = fitz.open(pdf_path)

        for page_num in range(len(doc)):
            page = doc[page_num]
            img_list = page.get_images(full=True)
            page_images = []

            for idx, img in enumerate(img_list):
                xref = img[0]
                base_image = doc.extract_image(xref)
                img_bytes = base_image["image"]
                ext = base_image["ext"]

                img_filename = f"page{page_num+1}_image{idx+1}.{ext}"
                img_path = os.path.join(output_folder, img_filename)

                with open(img_path, "wb") as f:
                    f.write(img_bytes)

                page_images.append(img_path)

            image_data.append({"page": page_num + 1, "images": page_images})
            print(f"[INFO] Extracted {len(page_images)} images from page {page_num+1}")

        doc.close()

    except Exception as e:
        print(f"[ERROR] Failed to extract images: {e}")

    return image_data



       
