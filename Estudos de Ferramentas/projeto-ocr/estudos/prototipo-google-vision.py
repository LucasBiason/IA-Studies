import os
from google.cloud import vision


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] ='vision_key.json'


def detect_text(path):
    """Detects text in the file."""

    client = vision.ImageAnnotatorClient()

    with open(path, "rb") as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    ocr_text = []

    for text in texts:
        ocr_text.append(f"\r\n{text.description}")

    if response.error.message:
        raise Exception(
            "{}\nFor more info on error messages, check: "
            "https://cloud.google.com/apis/design/errors".format(response.error.message)
        )

    return ocr_text


print("== recibo005.png =================================")
text = detect_text('../recursos/images/recibo005.png')
print(text)