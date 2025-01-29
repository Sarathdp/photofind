import cv2
import face_recognition
import requests
import os

def banner():
    print("""
    ███████╗ █████╗ ██████╗  █████╗ ████████╗██╗  ██╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██║  ██║
    ███████╗███████║██████╔╝███████║   ██║   ███████║
    ╚════██║██╔══██║██╔═══╝ ██╔══██║   ██║   ██╔══██║
    ███████║██║  ██║██║     ██║  ██║   ██║   ██║  ██║
    ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝
    SARATH - Social Media Image Finder
    """)

def download_image(image_url, filename):
    response = requests.get(image_url, stream=True)
    if response.status_code == 200:
        with open(filename, 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        print("Image downloaded successfully.")
    else:
        print("Failed to download the image.")

def reverse_image_search(image_path):
    search_url = "https://lens.google.com/uploadbyurl?url=" + image_path
    print(f"Perform a reverse image search here: {search_url}")

def save_results(data):
    with open("results.txt", "w") as file:
        file.write(data)
    print("Results saved to results.txt")

def process_image(image_path):
    image = cv2.imread(image_path)
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    face_locations = face_recognition.face_locations(rgb_image)
    
    if face_locations:
        print("Faces detected in the image.")
    else:
        print("No faces detected.")
    
    reverse_image_search(image_path)
    save_results("Reverse image search performed. Check results.")

def main():
    banner()
    image_path = input("Enter the image file path (png, jpg, jpeg): ")
    
    if os.path.exists(image_path):
        process_image(image_path)
    else:
        print("File not found. Please enter a valid path.")

if __name__ == "__main__":
    main()
