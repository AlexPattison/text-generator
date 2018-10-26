from textgenrnn import textgenrnn
textgen = textgenrnn(weights_path='sonnets/sonnets_two_weights.hdf5',
                     vocab_path='sonnets/sonnets_two_vocab.json',
                     config_path='sonnets/sonnets_two_config.json')

sober = textgen.generate(
    n=5, temperature=0.2, return_as_list=True)[0]
drunk = textgen.generate(
    n=5, temperature=0.2, return_as_list=True)[0]
print(sober)
print('YO YO YO')
print(drunk)
