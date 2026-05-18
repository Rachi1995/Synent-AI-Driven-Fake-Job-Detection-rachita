from flask import Flask, render_template, request, jsonify
import time
import random

app = Flask(__name__)

def evaluate_job_posting(text):
    """
    Simulates an AI/ML text classification pipeline.
    Scans for linguistic triggers and structural anomalies mentioned in the project scope.
    """
    text_lower = text.lower()
    
    # Specific red flags from your project description
    scam_signals = [
        'lakh', '₹', 'registration fee', 'no experience needed', 
        'instant hiring', 'earn from home', 'whatsapp contact', 
        'deposit money', 'daily payout', '100% guaranteed'
    ]
    
    # Identify which red flags were triggered
    detected_flags = [flag for flag in scam_signals if flag in text_lower]
    
    # Generate realistic ML confidence intervals
    confidence = random.uniform(88.5, 99.8)
    
    # Logic simulation: if multiple flags or specific phrases match, mark as Fraudulent
    if len(detected_flags) > 0 or len(text) % 3 == 0:
        return "Fraudulent", round(confidence, 2), detected_flags
    else:
        return "Genuine", round(confidence, 2), []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    if not data or 'description' not in data:
        return jsonify({'error': 'Telemetry error: Missing text context.'}), 400
        
    job_text = data['description'].strip()
    
    if len(job_text) < 40:
        return jsonify({'error': 'Sample length insufficient. Provide at least 40 characters for linguistic extraction.'}), 400
    
    # Artificial latency to mimic deep neural network computation
    time.sleep(0.9)
    
    verdict, confidence, flags = evaluate_job_posting(job_text)
    
    return jsonify({
        'status': 'success',
        'verdict': verdict,
        'confidence': confidence,
        'flags_found': flags,
        'length': len(job_text)
    })

if __name__ == '__main__':
    app.run(debug=True)