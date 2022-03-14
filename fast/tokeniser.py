from typing import List, Generator

from nltk.util import ngrams

from fast.tokens import Token, Tokens
from fast.utils import (
    WordNet, PREPROCESSOR, 
    VOCABULARY, VOCABULARY_WORDNET, STOPWORDS, 
    SIZE_STOPWORDS, SIZE_WORDNET
)
    
class Tokeniser:
    @staticmethod
    def encode(text:str) -> Tokens:
        return Tokens(Tokeniser._tokenise(text))

    @staticmethod
    def decode(ids:List[int]) -> Tokens:
        return Tokens(list(Tokeniser._convert_ids_to_tokens(ids)))

    @staticmethod
    def _tokenise(text:str) -> List[Token]:
        words = text.split()
        number_of_words = len(words)
        tokens = [None]*number_of_words
        for ngram_size in range(number_of_words+1,0,-1):
            for index_start,ngram in enumerate(ngrams(words,ngram_size)):
                index_end = index_start + ngram_size
                if any(tokens[index_start:index_end]):
                    continue 
                raw_token = ' '.join(words[index_start:index_end])
                normalised_token = PREPROCESSOR.normalise(text=' '.join(ngram))
                synset_name = VOCABULARY_WORDNET.get(normalised_token)
                if synset_name is not None or ngram_size==1:
                    tokens[index_start:index_end] = [WordNet.SKIP.value]*ngram_size
                    tokens[index_start] = Token(
                        raw_token=raw_token,
                        normalised_token=normalised_token,
                        synset_name=synset_name,
                        sense_disambiguation_context=text
                    )
        return list(filter(lambda token:isinstance(token,Token),tokens))

    @staticmethod
    def _convert_ids_to_tokens(ids:List[int]) -> Generator[Token,None,None]:
        for id in ids:
            if id < SIZE_WORDNET:
                synset_name = VOCABULARY[id] 
                token = synset_name.split(WordNet.SYNSET_NAME_DELIMITER.value)[0]
            elif id < SIZE_WORDNET + SIZE_STOPWORDS:
                synset_name= None
                token = STOPWORDS[id-SIZE_WORDNET]
            else:
                synset_name= None
                token = WordNet.UNKNOWN.value
            yield Token(
                raw_token=PREPROCESSOR.preprocess(token),
                normalised_token=token,
                synset_name=synset_name
            )