import tifffile as tiff
import os
from PIL import Image

# # Đường dẫn tới thư mục chứa các file .tif
# input_folder = r'D:\DUT\21TCLC-KHDL\sem7\Data Processing\CVC-ClinicDB\masks'
# output_folder = r'D:\DUT\21TCLC-KHDL\sem7\Data Processing\CVC-ClinicDB\mask'

# # Tạo thư mục đầu ra nếu chưa tồn tại
# if not os.path.exists(output_folder):
#     os.makedirs(output_folder)

# # Lặp qua tất cả các file trong thư mục đầu vào
# for filename in os.listdir(input_folder):
#     if filename.endswith(".tif"):  # Kiểm tra nếu file là .tif
#         # Đường dẫn đầy đủ tới file .tif
#         tif_image_path = os.path.join(input_folder, filename)

#         try:
#             # Đọc file .tif bằng tifffile
#             tif_image = tiff.imread(tif_image_path)

#             # Chuyển ảnh từ numpy array sang Pillow Image
#             img = Image.fromarray(tif_image)

#             # Chuyển tên file từ .tif sang .jpg
#             jpg_filename = filename.replace(".tif", ".jpg")
#             jpg_image_path = os.path.join(output_folder, jpg_filename)

#             # Lưu file dưới dạng .jpg
#             img.save(jpg_image_path, "JPEG")
#             print(f"Đã chuyển {filename} thành {jpg_filename}")
#         except Exception as e:
#             print(f"Không thể đọc được file {filename}: {e}")


# import os
# folder_path = r'D:\DUT\21TCLC-KHDL\sem7\Data Processing\Polyp\CVC-ClinicDB\images'

# def rename_images(folder_path):
#     # Lấy danh sách tất cả các tệp trong thư mục
#     for filename in os.listdir(folder_path):
#         if filename.endswith(".jpg"):
#             # Tạo đường dẫn tệp cũ và mới
#             old_path = os.path.join(folder_path, filename)
            
#             # Lấy chỉ số từ tên tệp cũ (có định dạng 1.jpg, 2.jpg, ...)
#             index = filename.split('.')[0]  # Lấy phần trước dấu '.' (1, 2, ...)
            
#             # Tạo tên mới theo định dạng yêu cầu
#             new_filename = f"fine_3_{index}_fram.jpg"
#             new_path = os.path.join(folder_path, new_filename)
            
#             # Đổi tên tệp
#             os.rename(old_path, new_path)
#             print(f'Renamed: {old_path} -> {new_path}')

# # Đường dẫn đến thư mục chứa các tệp hình ảnh
# rename_images(folder_path)




import os
folder_path = r'CVC-ClinicDB/mask'

def rename_images(folder_path):
    # Lấy danh sách tất cả các tệp trong thư mục
    for filename in os.listdir(folder_path):
        if filename.endswith(".jpg"):
            # Tạo đường dẫn tệp cũ và mới
            old_path = os.path.join(folder_path, filename)
            
            # Lấy chỉ số từ tên tệp cũ (có định dạng 1.jpg, 2.jpg, ...)
            index = filename.split('.')[0]  # Lấy phần trước dấu '.' (1, 2, ...)
            
            # Tạo tên mới theo định dạng yêu cầu
            new_filename = f"fine_3_{index}_mask.jpg"
            new_path = os.path.join(folder_path, new_filename)
            
            # Đổi tên tệp
            os.rename(old_path, new_path)
            print(f'Renamed: {old_path} -> {new_path}')

# Đường dẫn đến thư mục chứa các tệp hình ảnh
rename_images(folder_path)
