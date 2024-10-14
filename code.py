from PIL import Image
import numpy as np
# Convert the hidden message to bytes

def encode_text(text, encoding='utf-8', errors='surrogatepass'):
bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
return bits.zfill(8 * ((len(bits) + 7) // 8))
def decode_text(bits, encoding='utf-8', errors='surrogatepass'):
n = int(bits, 2)
 return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'
#To convert text into binary
hidden_message = "India is My Country"
encoded_text = encode_text(hidden_message)
decoded_text = decode_text(encoded_text)
print("encoded:", encoded_text)
print("decoded:", decoded_text)
def encode_in_image(filename, text_message):
 # Open the image, store the shape and convert to one-dimensional list
 input_im = Image.open(filename, 'r').convert("RGB")
 image_shape = np.asarray(input_im).shape
 flat_array = np.asarray(input_im).flatten()
 # Encode the message and add prefix
 encoded_text = encode_text(text_message + "<STOP>")
 # Enter message in the least significant bit where necessary
  encoded_array = [
  (0b11111110 & value) | int(encode_bit) if ix < len(encoded_text) else value
 for ix, (encode_bit, value) in enumerate(zip(encoded_text.ljust(len(flat_array),  '0'), flat_array))]
 # Turn encoded array into image and return
 encoded_im = np.array(encoded_array).reshape(image_shape)    
 return Image.fromarray(np.uint8(encoded_im)).convert('RGB')
encoded_im = encode_in_image('modi.jpg', "Attch on China")
encoded_im.save('hidden.png')
encoded_im
def extract_from_image(filename):
# Open image
encoded_im = np.asarray(Image.open(filename, 'r').convert("RGB"))
# Extract least significant bits from flat (one-dimensional) image
extracted_bits = [str(0b00000001 & value) for value in encoded_im.flatten()]
# Join bits together, decode and split at <STOP>
extracted_bits = ''.join(extracted_bits)
return decode_text(extracted_bits, errors='replace').split('<STOP>')[0]  
extract_from_image('hidden.png')
def encode_in_image(filename, text_message):
# Open the image, store the shape and convert to one-dimensional list
input_im = Image.open(filename, 'r').convert("RGB")
image_shape = np.asarray(input_im).shape
flat_array = np.asarray(input_im).flatten()

# Encode the message and add prefix
encoded_text = encode_text(text_message + "<STOP>")
# Enter message in the least significant bit where necessary
encoded_array = [
(0b11111110 & value) | int(encode_bit) if ix < len(encoded_text) else value
for ix, (encode_bit, value) in enumerate(zip(encoded_text.ljust(len(flat_array), '0'), flat_array))]
 # Turn encoded array into image and return
 encoded_im = np.array(encoded_array).reshape(image_shape)    
 return Image.fromarray(np.uint8(encoded_im)).convert('RGB')
encoded_im = encode_in_image('7112.png', "Hello India")
encoded_im.save('hidden.png')
encoded_im
def extract_from_image(filename):
 # Open image
 encoded_im = np.asarray(Image.open(filename, 'r').convert("RGB"))
 # Extract least significant bits from flat (one-dimensional) image
 extracted_bits = [str(0b00000001 & value) for value in encoded_im.flatten()]
 # Join bits together, decode and split at <STOP>
extracted_bits = ''.join(extracted_bits)
 return decode_text(extracted_bits, errors='replace').split('<STOP>')[0]
 extract_from_image('hidden.png')
def encode_in_image(filename, text_message):
 # Open the image, store the shape and convert to one-dimensional list
 input_im = Image.open(filename, 'r').convert("RGB")
 image_shape = np.asarray(input_im).shape
 flat_array = np.asarray(input_im).flatten()
 # Encode the message and add prefix
 encoded_text = encode_text(text_message + "<STOP>")
 # Enter message in the least significant bit where necessary
 encoded_array = [
 (0b11111110 & value) | int(encode_bit) if ix < len(encoded_text) else value
 for ix, (encode_bit, value) in enumerate(zip(encoded_text.ljust(len(flat_array), '0'),   flat_array))
 # Turn encoded array into image and return
 encoded_im = np.array(encoded_array).reshape(image_shape)    
 return Image.fromarray(np.uint8(encoded_im)).convert('RGB')
encoded_im = encode_in_image('army.png', "Indian army always for your Security")
encoded_im.save('hidden.png')
encoded_im
def extract_from_image(filename):
# Open image
 encoded_im = np.asarray(Image.open(filename, 'r').convert("RGB"))
 # Extract least significant bits from flat (one-dimensional) image
 extracted_bits = [str(0b00000001 & value) for value in encoded_im.flatten()]
 # Join bits together, decode and split at <STOP>
extracted_bits = ''.join(extracted_bits)
return decode_text(extracted_bits, errors='replace').split('<STOP>')[0]    
extract_from_image('hidden.png')
from PIL import Image, ImageFilter
import numpy as np
def create_circle_mask(image_size):
# Create a black image
mask = np.zeros(image_size, dtype=np.uint8)
# Calculate center coordinates
center_x, center_y = image_size[0] // 2, image_size[1] // 2
# Calculate radius (smaller of the two dimensions)
radius = min(image_size) // 4
# Create a white circle in the center
mask[center_x-radius:center_x+radius, center_y-radius:center_y+radius] = 255
return mask
def apply_mask(input_image_path, mask_image, output_image_path):
# Open the input image
 input_img = Image.open(input_image_path)
 # Convert the mask array to a PIL Image
 mask_img = Image.fromarray(mask_image, mode='L')
 # Ensure both images have the same size
 if input_img.size != mask_img.size:
 raise ValueError("Input image and mask image must have the same size")
 # Apply the mask to the input image
 masked_img = Image.composite(input_img, Image.new("RGB", input_img.size, "black"), mask_img)
 # Save the masked image
 masked_img.save(output_image_path)
 print("Masking completed. Masked image saved at:", output_image_path)
def filter_image(image_path, filter_type, output_path):
# Open the image
img = Image.open(image_path)
# Apply the specified filter
if filter_type.lower() == "blur":
filtered_img = img.filter(ImageFilter.BLUR)
elif filter_type.lower() == "smooth":
filtered_img = img.filter(ImageFilter.SMOOTH)
    elif filter_type.lower() == "edge enhance":
        filtered_img = img.filter(ImageFilter.EDGE_ENHANCE)
    else:
        raise ValueError("Invalid filter type. Supported types: 'blur', 'smooth', 'edge enhance'")
 # Save the filtered image
 filtered_img.save(output_path)
 print("Filtering completed. Filtered image saved at:", output_path)
# Paths
input_image_path = "army.png"
mask_image_path = "mask_army.png"  
masked_output_path = "masked_army.png"
filtered_output_path = "filtered_army.png"
# Open the input image to get its size
input_img = Image.open(input_image_path)
input_img_size = input_img.size
# Create a circular mask with the same dimensions as the input image
mask_image = create_circle_mask(input_img_size)  # Use the size of the input image
# Create a circular mask
#mask_image = create_circle_mask((200, 200))  # Specify the size of the mask image
# Apply the mask to the input image
apply_mask(input_image_path, mask_image, masked_output_path)
# Filter the input image
filter_type = "blur"  # Change the filter type as needed
filter_image(input_image_path, filter_type, filtered_output_path)
import matplotlib.pyplot as plt
# Display the masked image
masked_img = Image.open(masked_output_path)
plt.figure(figsize=(8, 8))
plt.subplot(1, 2, 1)
plt.imshow(masked_img)
plt.title('Masked Image')
# Display the filtered image
filtered_img = Image.open(filtered_output_path)
plt.subplot(1, 2, 2)
plt.imshow(filtered_img)
plt.title('Filtered Image')
plt.show()
import cv
# Read the filtered image using OpenCV
filtered_img_cv = cv2.imread(filtered_output_path)
# Convert the image to grayscale
gray_img = cv2.cvtColor(filtered_img_cv, cv2.COLOR_BGR2GRAY)
# Perform edge detection using the Canny edge detector
edges = cv2.Canny(gray_img, 50, 150)
# Display the edge-detected image
plt.figure(figsize=(8, 8))
plt.imshow(edges, cmap='gray')
plt.title('Edge-Detected Image')
plt.show()


