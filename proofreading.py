import csv
from janome.tokenizer import Tokenizer
import re

class Proofreading:
    """
    文書構成を実行するクラス
    """
    def __init__(self, rule_file="change.csv"):
        self._change_rule_dic = self._load_change_rule(rule_file)
        self._tokenizer = Tokenizer()

    def _load_change_rule(self, rule_file):
        """
        変更ルールのファイルを読み込む

        :param rule_file: 変更ルールのファイルパス
        :return: 変更ルールの辞書型
        """
        with open(rule_file, encoding="utf-8-sig") as f:
            data = csv.DictReader(f)
            for d in data:
                return d
　
    def _multiple_replace(self, text):
        """
        変更ルールを適用する

        :param text: ルールを適用する文字列
        :return: ルールを適用した文字列
        """
        for key, value in self._change_rule_dic.items():
            text = re.sub(key, value ,text)
        return text

    def proof_with_word_base(self, text):
        """
        形態素単位での校正を実行する

        :param text: 入力文字列
        :return:校正済み文字列
        """
        words = self._tokenizer.tokenize(text, wakati=True)

        replaced_words = [self._multiple_replace(w) for w in words]

        result_text = "".join(replaced_words)

        return result_text
