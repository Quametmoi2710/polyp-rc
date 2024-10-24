import tifffile as tiff
import os
from PIL import Image

# Đường dẫn tới thư mục chứa các file .tif
input_folder = r'D:\DUT\21TCLC-KHDL\sem7\Data Processing\CVC-ClinicDB\masks'
output_folder = r'D:\DUT\21TCLC-KHDL\sem7\Data Processing\CVC-ClinicDB\mask'

# Tạo thư mục đầu ra nếu chưa tồn tại
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Lặp qua tất cả các file trong thư mục đầu vào
for filename in os.listdir(input_folder):
    if filename.endswith(".tif"):  # Kiểm tra nếu file là .tif
        # Đường dẫn đầy đủ tới file .tif
        tif_image_path = os.path.join(input_folder, filename)

        try:
            # Đọc file .tif bằng tifffile
            tif_image = tiff.imread(tif_image_path)

            # Chuyển ảnh từ numpy array sang Pillow Image
            img = Image.fromarray(tif_image)

            # Chuyển tên file từ .tif sang .jpg
            jpg_filename = filename.replace(".tif", ".jpg")
            jpg_image_path = os.path.join(output_folder, jpg_filename)

            # Lưu file dưới dạng .jpg
            img.save(jpg_image_path, "JPEG")
            print(f"Đã chuyển {filename} thành {jpg_filename}")
        except Exception as e:
            print(f"Không thể đọc được file {filename}: {e}")
