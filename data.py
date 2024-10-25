import os
import numpy as np
import cv2
import glob 
import tensorflow as tf
from sklearn.model_selection import train_test_split



def load_data(path, split = 0.1):    
        path = "D:/DUT/21TCLC-KHDL/sem7/Data Processing/CVC-ClinicDB"


        image_pattern = os.path.join(path, "images/*.jpg")
        mask_pattern = os.path.join(path, "mask/*.jpg")
        
        print("Looking for images in:", image_pattern)
        print("Looking for masks in:", mask_pattern)

        images = sorted(glob.glob(image_pattern))
        masks = sorted(glob.glob(mask_pattern))

        print(f"Found {len(images)} images")
        print(f"Found {len(masks)} masks")


        total_size = len(images)
        valid_size = int(split*total_size)
        test_size  = int(split*total_size)
        valid_size = 0.2

        train_x, valid_x = train_test_split(images, test_size= valid_size, random_state=42 )
        train_y, valid_y = train_test_split(masks, test_size= valid_size, random_state=42 )
        
        train_x, test_x = train_test_split(train_x, test_size= test_size, random_state=42 )
        train_y, test_y = train_test_split(train_y, test_size= test_size, random_state=42 )

        return (train_x, train_y), (valid_x, valid_y), (test_x, test_y)

def read_image(path):
        #path.decode(): Giải mã chuỗi byte thành chuỗi ký tự (string). 
        #Điều này cần thiết nếu đường dẫn path đang ở dạng byte (ví dụ: nếu bạn sử dụng TensorFlow hoặc một số thư viện khác trả về đường dẫn dưới dạng byte string).
        path = path.decode()
        x = cv2.imread(path, cv2.IMREAD_COLOR)
        x = cv2.resize(x, (256, 256))
        x = x/255.0
        # (256, 256, 3) - 3 là 3 kênh màu của ảnh RBG
        return x

def read_mask(path):
        path = path.decode()
        x = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        x = cv2.resize(x, (256, 256))
        x = x/255.0
        # (256, 256)
        x = np.expand_dims(x, axis=-1)
        # (256, 256, 1) - 1 là ảnh xám
        return x

def tf_parse(x,y):
        def _parse(x, y):
                x = read_image(x)
                y = read_mask(y)
                return x, y
        
        x, y = tf.numpy_function(_parse, [x,y], [tf.float64, tf.float64])
        x.set_shape([256,256,3])
        y.set_shape([256,256,1])

        return x,y

def tf_dataset(x, y, batch = 8):
        dataset = tf.data.Dataset.from_tensor_slices((x,y))
        dataset = dataset.map(tf_parse)
        dataset = dataset.batch(batch)
        dataset = dataset.repeat()
        return dataset


if __name__ == "__main__":
        print("")
        path = "CVC-ClinicDB"
        (train_x, train_y), (valid_x, valid_y), (test_x, test_y) = load_data(path)
        print(len(train_x), len(valid_x), len(test_x))

        ds = tf_dataset(test_x, test_y)
        for x, y in ds:
                print(x.shape, y.shape)
                break

