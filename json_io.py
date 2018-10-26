from textgenrnn import textgenrnn
from flask import Flask
app = Flask(__name__)

textgen = textgenrnn(weights_path='texts/sonnets/sonnets_two_weights.hdf5',
                     vocab_path='texts/sonnets/sonnets_two_vocab.json',
                     config_path='texts/sonnets/sonnets_two_config.json')

sober = textgen.generate(
    n=5, temperature=0.2, return_as_list=True)[0]
drunk = textgen.generate(
    n=5, temperature=0.2, return_as_list=True)[0]


@app.route("/output")
def output():
    return sober


if __name__ == "__main__":
    app.run()
