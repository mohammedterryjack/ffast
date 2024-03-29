from setuptools import setup, find_packages

VERSION = '0.4.10'
DESCRIPTION = 'FFAST: Fast Fourier Analysis for Sentence embeddings and Tokenisation'
LONG_DESCRIPTION = 'Fast and lightweight NLP pipeline for ML tasks: powerful tokeniser and (model-free) sentence embeddings using Fast Fourier transforms, power means, positional encoding and Wordnet or Poincare Embeddings'

setup(
    name="ffast",
    version=VERSION,
    author="Mohammed Terry-Jack",
    author_email="<mohammedterryjack@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    setup_requires = ['nltk'],
    include_package_data=True,
    package_data={'':[
        'poincare/poincare.txt',
        'wordnet/nltk_data/corpora/wordnet.zip',
        'wordnet/nltk_data/corpora/omw-1.4.zip',
        'wordnet/nltk_data/corpora/stopwords.zip',
    ] 
    },
    install_requires=['nltk', 'jellyfish', 'Unidecode', 'numpy', 'scipy'],
    keywords=['python', 'embedding', 'tokenisation', 'fast fourier', 'nlp', 'nlu', "poincare", "wordnet", "lite", "fast", "sentence encoder"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
    ]
)