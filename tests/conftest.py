import os
import sys
import pytest
import pandas as pd

sys.path.append(os.path.realpath(''))
from src import Explorer, DataGenerator, Preprocess, Tokenizer

@pytest.fixture
def explorer():
    data = pd.read_csv("tests/fake_data.csv")
    return Explorer(data)

@pytest.fixture
def generator():
    data = pd.read_csv("tests/fake_data.csv")
    return DataGenerator(data)

@pytest.fixture
def preprocessor():
    return Preprocess()

@pytest.fixture
def tokenizer():
    return Tokenizer()

@pytest.fixture
def url():
    return "http://0.0.0.0:8000/is_real_name/"