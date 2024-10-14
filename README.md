# Secure-Data-Transfer-over-the-Internt-using-Image-Steganography
* * *

# Table of Contents:

-[Overview](#Overview)

-[Dataset](#Dataset)

-[Techniques Used](#Techniques Used)

* * *


# Overview:

This project aims is to implement the Image Steganography for a more secure data transfer, especially over the internet using Least Significant Bit and to develop a system that serves as a security measure by hidden communication to cover a message from third party.

Steganography hides secret data within regular files, like images. It's essential for digital security. Unlike cryptography, which encodes messages, steganography conceals their existence. By embedding data in images, it offers a low-cost way to protect information during transmission. This project creates new encryption methods for hiding messages in images, enhancing digital privacy and security.

## What is Steganography?

Steganography is a method of hiding secret data, embedding it into an audio, video, image or text file.


![image](https://github.com/user-attachments/assets/c428a4c4-1ec1-4071-9bcf-4d55c9e27a16)



The word Steganography is derived from two Greek words- ‘stegos’ meaning ‘to cover’ and ‘grayfia’, meaning ‘writing’, thus translating to ‘covered writing’, or ‘hidden writing’. 

The process of hiding information which can be text, image or video inside a cover image is called Steganography. 

# Basic Steganography Model

![image](https://github.com/user-attachments/assets/63e7538a-93b1-4cf0-8cd6-a86bfbb3ddd8)


# Techniques Used:


1. Encoding Module
   Input:
   - Text message: The text message to be encoded into the image.
   - Image File: The input image file in which the message will be hidden.
     -# Encoded Image: The output image file with the hidden message embedded in it.

 2. Decoding Module
    Input:
    -Encoded Image: The image file containing the hidden message.
    -Decoded Message: The original text message hidden in the image.

3. Image Processing Module
   Input:
  - Image file: The input image file on which image processing operations will be applied.
  - Processed Image: The output image file with the applied mask and filters for improved 
   quality and security.

