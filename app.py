from flask import Flask, render_template, jsonify

app = Flask(__name__)

surveys = [

    {
        "id":1,
        "title":"New Student Survey",
        "desc":"Question for first year student",
        "nq":2,
        "qs":[
            "3",
            "4"
        ]

    },

    {
        "id":2,
        "title":"Student Survey",
        "desc":"Question for master program student",
        "nq":2,
        "qs":[
             "1",
             "2",
            "3",
            "4"
        ]

    }

]




questions = [
    
    {
        "id":1,
        "type":"rate",
        "title": "Were you satisfied with the organisation of the course?",
        "description": "On the scale of 1(lowest) to 5(highest) were you satisfied with the organisation of the course?",
        "options": [
            "1",
            "2",
            "3",
            "4",
            "5"
        ]

    },

    {
        "id":2,
        "type":"rate",
        "title": "Were you satisfied with the organisation of the course?",
        "description": "On the scale of 1(lowest) to 5(highest) were you satisfied with the organisation of the course?",
        "options": [
            "1",
            "2",
            "3",
            "4",
            "5"
        ]

    },

    {

     "id":3,
        "type":"rate",
        "title": "Rate our education centre",
        "description": "On the scale of 1(lowest) to 5(highest) were you satisfied with the organisation of the course?",
        "options": [
            "1",
            "2",
            "3",
            "4",
            "5"
        ]
    },
     {

     "id":4,
        "type":"free",
        "title": "Why did you select the course",
        "description": "Pleas describe the reason why you selected the course?",
        "options": []
    }

]


@app.route('/')
def homepage():
    return render_template("home.html")

@app.route('/api/surveys/', methods=['GET'])
def get_surveys():
    return jsonify(surveys)

@app.route('/api/surveys/<int:survey_id>', methods=['GET'])
def get_survey(survey_id):
    survey = [survey for survey in surveys if survey['id'] == survey_id]
    if len(survey) == 0:
        return jsonify({'error': 'survey not found'}), 404
    return jsonify(survey[0])

@app.route('/api/questions/', methods=['GET'])
def get_questions():
    return jsonify(questions)

@app.route('/api/questions/<int:question_id>', methods=['GET'])
def get_question(question_id):
    question  = [question for question in questions if question['id'] == question_id]
    if len(question) == 0:
        return jsonify({'error': 'question not found'}), 404
    return jsonify(question[0])



if __name__ == "__main__":
    app.run(debug=True)





