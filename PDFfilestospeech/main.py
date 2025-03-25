from google.cloud import texttospeech
import os
from PyPDF2 import PdfReader

# 1. PDF Text Extraction
def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, "rb") as f:
        reader = PdfReader(f)
        for page in reader.pages:
            text += page.extract_text()
    return text

# 2. Google Cloud Setup
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/sdasa/AppData/Roaming/gcloud/application_default_credentials.json"

def convert_with_client_library(text):
    client = texttospeech.TextToSpeechClient()

    synthesis_input = texttospeech.SynthesisInput(text=text)

    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        name="en-US-Wavenet-C"
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    response = client.synthesize_speech(
        input=synthesis_input,
        voice=voice,
        audio_config=audio_config
    )

    with open("output.mp3", "wb") as f:
        f.write(response.audio_content)



# 5. Main Execution
if __name__ == "__main__":
    pdf_path = "resume.pdf"

    # Extract text from PDF
    text = extract_text_from_pdf(pdf_path)
    if not text:
        print("Error: No text extracted from PDF")
        exit(1)

    # Convert to speech
    convert_with_client_library(text[:5000])  # Limit to 5000 characters (API limit)