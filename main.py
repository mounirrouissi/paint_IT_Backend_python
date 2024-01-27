from fastapi import FastAPI, UploadFile, File,Response
from PIL import Image
from  io import BytesIO
import io
from fastapi.middleware.cors import CORSMiddleware
import base64
import cv2

from rembg import remove
# Import the libraries
# from summarizer import Summarizer
# import numpy as np
app = FastAPI()

origins = [
    "http://localhost:3000",  # React app
    "http://localhost:8080", 
    "http://localhost:5173" # FastAPI server
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

""" @app.get("/")
def read_root():
    # Load the BERT model
    model = Summarizer('bert-base-uncased')

# Define the text to be summarized
    text = "Yes, you can use the ViewShot component with Expo to capture a screenshot of the SVG image. ViewShot is a React Native component that allows you to take a snapshot of any view and save it as an image1. It works with Expo, as it does not require any native dependencies2. Then, you can wrap the SVG image component with the ViewShot component and pass some options, such as the format and quality of the image. You also need to create a reference to the ViewShot component with useRef and use the capture method to get the image URI."


# Generate the summary
    summary = model(text, num_sentences=1)

# Print the summary
    print(summary)
    return summary        
    # return {"Hello": "World"}
 """
@app.post("/api/process_image")
async def process_image(image: UploadFile = File(...)):
    print("called  process_image",image)
    image_contents = await image.read()
    # Remove the background from the image
    output_data = remove(image_contents)
    img = Image.open(io.BytesIO(output_data))
    # img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    # # Change black (also shades of blacks)
    # # pixels to white
    # img[np.where((img==[0,0,0]).all(axis=2))] = [255,255,255]
    # # Convert image back to PIL.Image format
    # img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    buffer = io.BytesIO()  # Initialize buffer before using it
    img.save(buffer, format="PNG")
    print("called  image")
    print("called  image")

    buffer.seek(0)
    imageStr = base64.b64encode(buffer.getvalue()).decode()  # Encode as base64 string
    print(imageStr) 
    return Response(content=imageStr, media_type="image/png")