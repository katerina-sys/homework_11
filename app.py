from flask import Flask, request, render_template
import utils

app = Flask(__name__)

@app.route('/')
def page_list():
    candidates = utils.load_candidates_from_json()
    return render_template('list.html', candidates=candidates)

@app.route('/candidate/<int:candidate_id>')
def page_candidate_id(candidate_id):
    candidate = utils.get_candidate_by_id(candidate_id)

    if candidate is None:
        return "Нет такого кандидата"
    return render_template('card.html', candidate=candidate)

@app.route('/search/<candidate_name>')
def page_candidate_name(candidate_name):
    candidates = utils.get_candidates_by_name(candidate_name)
    number_of_candidates = len(candidates)
    return render_template('search.html', candidates=candidates, number_of_candidates=number_of_candidates)

@app.route('/skill/<skill_name>')
def page_candidate_skills(skill_name):
    candidates = utils.get_candidates_by_skill(skill_name)
    number_of_candidates = len(candidates)
    return render_template('skill.html', candidates=candidates, number_of_candidates=number_of_candidates, skill_name=skill_name)


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8000, debug=True)