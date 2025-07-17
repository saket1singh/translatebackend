from flask import Flask, request, jsonify
from flask_cors import CORS
from googletrans import Translator
from indic_transliteration.sanscript import transliterate, TELUGU, ITRANS

app = Flask(__name__)
CORS(app)

translator = Translator()

@app.route('/translate', methods=['POST'])
def translate():
    text = request.json['text']
    translated = translator.translate(text, src='hi', dest='te')
    return jsonify({"translation": translated.text})

@app.route('/translate-live', methods=['POST'])
def translate_live():
    text = request.json['text']
    translated = translator.translate(text, src='te', dest='hi')
    return jsonify({"translation": translated.text})

@app.route('/breakdown', methods=['POST'])
def breakdown():
    telugu_text = request.json['text']
    words = telugu_text.strip().replace("?", "").replace("।", "").split()

    breakdown = []
    for word in words:
        try:
            hindi_meaning = translator.translate(word, src='te', dest='hi').text
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
    app.run(debug=True)
