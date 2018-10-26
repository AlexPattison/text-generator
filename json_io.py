from textgenrnn import textgenrnn
from flask import Flask, request
from flask_cors import CORS, cross_origin
import json

app = Flask(__name__)
CORS(app)

textgen_word = textgenrnn(weights_path='texts/sonnets/sonnets_two_weights.hdf5',
                          vocab_path='texts/sonnets/sonnets_two_vocab.json',
                          config_path='texts/sonnets/sonnets_two_config.json')

textgen_letter = textgenrnn(weights_path='texts/sonnets/sonnets_by_letter_weights.hdf5',
                            vocab_path='texts/sonnets/sonnets_by_letter_vocab.json',
                            config_path='texts/sonnets/sonnets_by_letter_config.json')

sober_word = textgen_word.generate(
    n=5, temperature=0.2, return_as_list=True, max_gen_length=1000)

letter = textgen_letter.generate(
    n=5, temperature=0.8, return_as_list=True, max_gen_length=1000)


@app.route("/drunk")
@cross_origin()
def drunk():
    return json.dumps(letter)


@app.route("/sober")
@cross_origin()
def sober():
    return json.dumps(sober_word)


if __name__ == "__main__":
    app.run(debug=True)
