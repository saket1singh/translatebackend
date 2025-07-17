from flask import Flask, request, jsonify
from flask_cors import CORS
from deep_translator import GoogleTranslator
from indic_transliteration.sanscript import transliterate, TELUGU, ITRANS

app = Flask(__name__)
CORS(app)

@app.route('/translate', methods=['POST'])
def translate():
    text = request.json['text']
    translated = GoogleTranslator(source='hi', target='te').translate(text)
    return jsonify({"translation": translated})

@app.route('/translate-live', methods=['POST'])
def translate_live():
    text = request.json['text']
    translated = GoogleTranslator(source='te', target='hi').translate(text)
    return jsonify({"translation": translated})

@app.route('/breakdown', methods=['POST'])
def breakdown():
    telugu_text = request.json['text']
    words = telugu_text.strip().replace("?", "").replace("।", "").split()

    breakdown = []
    for word in words:
        try:
            hindi_meaning = GoogleTranslator(source='te', target='hi').translate(word)
        except:
            hindi_meaning = "—"
        try:
            roman = transliterate(word, TELUGU, ITRANS)
        except:
            roman = "—"
        
        breakdown.append({
            "telugu": word,
            "roman": roman,
            "hindi": hindi_meaning
        })

    return jsonify({"breakdown": breakdown})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
