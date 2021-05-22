import csv
from janome.tokenizer import Tokenizer
import re

tokenizer = Tokenizer()

def load_change_rule(rule_file):
    with open(rule_file, encoding="utf-8-sig") as f:
        data = csv.DictReader(f)
        for d in data:
            return d

def multiple_replace(text):
    for key, value in load_change_rule("change_test.csv").items():
        text = re.sub(key, value ,text)
    return text

def proof_with_word_base(text):
    words = tokenizer.tokenize(text, wakati=True)

    replaced_words = [multiple_replace(w) for w in words]

    result_text = "".join(replaced_words)

    return result_text
