import streamlit as st
import os
import torch
from torchvision.transforms import transforms
from PIL import Image
from pathlib import Path


# this is for saving images and prediction
def save_image(uploaded_file):
    if uploaded_file is not None:
        #check if there's already an image in the images folder and delete it
        #save new image to images
        save_path = os.path.join("images", "input.jpeg")
        if os.path.exists(save_path):
            os.remove(save_path)

        #save the new image
        with open(save_path, "wb") as f:
            f.write(uploaded_file.read())
        st.success(f"Image saved to {save_path}")
        ##model path
        # Construct the file path using os.path.join to handle platform differences
        model_path = os.path.join('model', 'model_a.pt')
        model = torch.load(model_path)

        ## transforming the image
        trans = transforms.Compose([
            transforms.RandomHorizontalFlip(),
            transforms.Resize(224),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            ])

        image = Image.open(Path('images/input.jpeg'))

        input = trans(image)

        input = input.view(1, 1, 224, 224).repeat(1, 3, 1, 1)

        output = model(input)

        prediction = int(torch.max(output.data, 1)[1].numpy())
        print(prediction)

        if (prediction == 1):
            print ('Normal')
            st.text_area(label="Prediction:", value="Normal", height=100)
        if (prediction == 0):
            print ('PNEUMONIA')
            st.text_area(label="Prediction:", value="PNEUMONIA", height=100)





## running the streamlit app
if __name__ == "__main__":
    st.title("Xray lung classifier")
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])
    save_image(uploaded_file)


    