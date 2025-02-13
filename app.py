# from flask import Flask, render_template, request, jsonify
# from flask_cors import CORS
# from scrape import scrape_response_sheet
# from answer_key import ANSWER_KEY
# from evaluate import evaluate_responses

# app = Flask(__name__)
# CORS(app)

# @app.route("/")
# def home():
#     return render_template("home.html")

# @app.route("/evaluate", methods=["POST"])
# def evaluate():
#     data = request.json
#     response_url = data.get("response_url")

#     if not response_url:
#         return jsonify({"error": "No URL provided"}), 400

#     # Scrape response sheet
#     scraped_data = scrape_response_sheet(response_url)

#     if not scraped_data:
#         return jsonify({"error": "Failed to process response sheet"}), 500

#     exam_date = scraped_data["exam_date"]
#     slot_time = scraped_data["slot_time"]

#     # Check if answer key exists
#     if exam_date not in ANSWER_KEY or slot_time not in ANSWER_KEY[exam_date]:
#         return jsonify({"error": "Answer key not found for this date & slot"}), 500

#     correct_answers = ANSWER_KEY[exam_date][slot_time]

#     # Evaluate responses
#     result = evaluate_responses(scraped_data["questions"], correct_answers)

#     return jsonify({
#         "total_marks": result["total_marks"],
#         "correct": result["correct"],
#         "incorrect": result["incorrect"],
#         "unattempted": result["unattempted"],
#         "subject_scores": result["subject_scores"],
#         "subject_questions": result["subject_questions"],
#         "exam_date": exam_date,
#         "slot_time": slot_time
#     })

# if __name__ == "__main__":
#     app.run(host='0.0.0.0',debug=True)


from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home_page.html")

@app.route("/jee-mains")
def jee_mains():
    return "<h1>JEE Mains Page - Coming Soon!</h1>"

@app.route("/gate")
def gate():
    return "<h1>GATE Page - Coming Soon!</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
