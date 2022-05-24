from flask import Flask, render_template, request, jsonify
from proofreading import proofreading

app = Flask(__name__)
pr = Proofreading()


@app.route('/proofreading_run', methods=["POST"])
def proofreading_run():
    input_text = request.json["text"]

    result_text = pr.proof_with_word_base(input_text)

    return jsonify({"result": result_text})


@app.route('/')
def index():
    return render_template('index.html', title='proofreading_tool')


if __name__ == "__main__":
    app.run(debug=True)
