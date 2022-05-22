import json

PATH = "candidates.json"


def load_data(path=PATH):
    """Загружает список кандидатов из файла"""
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
        return data


def load_candidates_from_json():
    """Получает список всех кандидатов"""
    data = load_data()
    return data


def get_candidate_by_id(candidate_id):
    """Получает кандидата по id"""
    candidates = load_data()
    for candidate in candidates:
        if candidate["id"] == candidate_id:
            return candidate


def get_candidates_by_name(candidate_name):
    """Получает кандидата по имени"""
    candidates_found = []
    candidates = load_data()
    for candidate in candidates:
        if candidate_name.lower() in candidate["name"].lower():
            candidates_found.append(candidate)
    return candidates_found


def get_candidates_by_skill(skill_name):
    """Получает кандидата по его навыкам(skill_name)"""

    skill_candidates = []
    skill_lower = skill_name.lower()

    candidates = load_data()
    for candidate in candidates:
        skills = candidate["skills"].lower().strip().split(", ")
        if skill_lower in skills:
            skill_candidates.append(candidate)
            continue

    return skill_candidates

print(get_candidates_by_skill("go"))
