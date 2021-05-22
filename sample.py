from proofreading import Proofreading


pr = Proofreading()


def main():
    input_text = "一斉に走る"

    result_text = pr.proof_with_word_base(input_text)

    print(result_text)


if __name__ == "__main__":
    main()