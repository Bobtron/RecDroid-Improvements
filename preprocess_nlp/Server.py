from nltk.parse.corenlp import CoreNLPServer

server = CoreNLPServer(
    '../pre_trained_models/stanford-corenlp-4.0.0.jar',
    '../pre_trained_models/stanford-corenlp-4.0.0-models.jar'
)

server.start()