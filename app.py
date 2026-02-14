from flask import Flask, render_template, request, jsonify, session
import requests
import base64
import json
from io import BytesIO
from PyPDF2 import PdfReader
from PIL import Image
import os

app = Flask(__name__)
app.secret_key = 'ollama-web-secret-key'

OLLAMA_BASE_URL = "http://localhost:11434"
OLLAMA_UPLOAD_FOLDER = 'uploads'
os.makedirs(OLLAMA_UPLOAD_FOLDER, exist_ok=True)

def get_ollama_models():
    try:
        response = requests.get(f"{OLLAMA_BASE_URL}/api/tags", timeout=5)
        if response.status_code == 200:
            data = response.json()
            return [m["name"] for m in data.get("models", [])]
        return []
    except Exception as e:
        print(f"Error getting models: {e}")
        return []

def get_vision_models():
    models = get_ollama_models()
    return [m for m in models if any(x in m.lower() for x in ["vision", "llava", "ocr", "qwen2vl", "minicpm"])]

def chat_with_ollama(model, messages, stream=False):
    url = f"{OLLAMA_BASE_URL}/api/chat"
    payload = {
        "model": model,
        "messages": messages,
        "stream": stream
    }
    
    try:
        if stream:
            response = requests.post(url, json=payload, stream=True, timeout=120)
            return response
        else:
            response = requests.post(url, json=payload, timeout=120)
            if response.status_code == 200:
                return response.json()
            return None
    except Exception as e:
        print(f"Error in chat: {e}")
        return None

def extract_pdf_text(file):
    try:
        pdf = PdfReader(file)
        text = ""
        for page in pdf.pages:
            text += page.extract_text() + "\n"
        return text
    except Exception as e:
        print(f"Error extracting PDF: {e}")
        return None

def encode_image_to_base64(image):
    buffered = BytesIO()
    image.save(buffered, format=image.format or 'PNG')
    return base64.b64encode(buffered.getvalue()).decode("utf-8")

def ocr_with_vision(image, model, prompt="请仔细识别这张图片中的所有文字内容，直接输出文字，不要其他解释。"):
    img_b64 = encode_image_to_base64(image)
    url = f"{OLLAMA_BASE_URL}/api/chat"
    payload = {
        "model": model,
        "messages": [
            {
                "role": "user",
                "content": prompt,
                "images": [img_b64]
            }
        ],
        "stream": False
    }
    
    try:
        response = requests.post(url, json=payload, timeout=120)
        if response.status_code == 200:
            return response.json().get("message", {}).get("content", "")
        return None
    except Exception as e:
        print(f"Error in OCR: {e}")
        return None

@app.route('/')
def index():
    models = get_ollama_models()
    vision_models = get_vision_models()
    return render_template('index.html', models=models, vision_models=vision_models)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    model = data.get('model')
    message = data.get('message')
    history = data.get('history', [])
    
    if not model or not message:
        return jsonify({'error': 'Missing model or message'}), 400
    
    messages = history + [{"role": "user", "content": message}]
    result = chat_with_ollama(model, messages, stream=False)
    
    if result:
        return jsonify({
            'response': result.get('message', {}).get('content', ''),
            'model': model
        })
    return jsonify({'error': 'Failed to get response from Ollama'}), 500

@app.route('/chat/stream', methods=['POST'])
def chat_stream():
    data = request.json
    model = data.get('model')
    message = data.get('message')
    history = data.get('history', [])
    
    if not model or not message:
        return jsonify({'error': 'Missing model or message'}), 400
    
    messages = history + [{"role": "user", "content": message}]
    response = chat_with_ollama(model, messages, stream=True)
    
    if response:
        def generate():
            for line in response.iter_lines():
                if line:
                    try:
                        data = json.loads(line)
                        content = data.get("message", {}).get("content", "")
                        yield f"data: {json.dumps({'content': content})}\n\n"
                    except:
                        pass
        return generate(), {'Content-Type': 'text/event-stream'}
    return jsonify({'error': 'Failed to get response from Ollama'}), 500

@app.route('/ocr', methods=['POST'])
def ocr():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file'}), 400
    
    file = request.files['image']
    model = request.form.get('model')
    prompt = request.form.get('prompt', '请仔细识别这张图片中的所有文字内容，直接输出文字，不要其他解释。')
    
    if not model:
        return jsonify({'error': 'No model selected'}), 400
    
    try:
        image = Image.open(file)
        result = ocr_with_vision(image, model, prompt)
        
        if result:
            return jsonify({'result': result})
        return jsonify({'error': 'OCR failed'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/chat/image', methods=['POST'])
def chat_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file'}), 400
    
    model = request.form.get('model')
    prompt = request.form.get('prompt', '请描述这张图片的内容。')
    
    if not model:
        return jsonify({'error': 'No model selected'}), 400
    
    try:
        image = Image.open(request.files['image'])
        result = ocr_with_vision(image, model, prompt)
        
        if result:
            return jsonify({'response': result})
        return jsonify({'error': 'Failed to process image'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/pdf', methods=['POST'])
def pdf():
    if 'pdf' not in request.files:
        return jsonify({'error': 'No PDF file'}), 400
    
    file = request.files['pdf']
    model = request.form.get('model', '')
    
    try:
        text = extract_pdf_text(file)
        if text:
            return jsonify({'text': text})
        return jsonify({'error': 'Failed to extract text'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/models/refresh')
def refresh_models():
    models = get_ollama_models()
    vision_models = get_vision_models()
    return jsonify({'models': models, 'vision_models': vision_models})

if __name__ == '__main__':
    print("Starting Ollama Web Interface...")
    print("Please ensure Ollama is running: ollama serve")
    app.run(debug=True, port=5000)
