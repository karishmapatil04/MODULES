import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.metrics.pairwise import cosine_similarity

from textblob import TextBlob

from colorama import init, Fore

import time

import sys

init(autoreset=True)

def load_data(file_path=’imdb_top_1000.csv’):

