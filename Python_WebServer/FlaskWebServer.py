import json
import uuid
import pprint

from flask import Flask, request, render_template
import flask

app = Flask(__name__)


class Student(object):
    def __init__(self, name, age):
        self.id = str(uuid.uuid4())
        self.student_age = age
        self.student_name = name

    def get_as_dict(self):
        """Returns the representation of an object in a json format"""
        return {"name": self.student_name,
                "age": self.student_age,
                "id": self.id}


"""Create three students objects in a list"""
STUDENTS = [
    Student("John", 21),
    Student("Mathew", 22),
    Student("Diana", 24),
    Student("Maria", 25)]


def as_json(func):
    def new_func(*args, **kwargs):
        resp = func(*args, **kwargs)
        if isinstance(resp, dict):
            response_text = flask.make_response(json.dumps(resp))
            response_text.headers['Content-type'] = 'text/json'
            return response_text
        return resp

    return new_func


def get_students_id():
    return {'students': [{'id': student.id, 'name': student.student_name, 'age': student.student_age} for student in STUDENTS]}


pprint.pprint(get_students_id())


@app.route("/student/<resource_id>", methods=['GET', 'PUT', 'POST', 'PATCH', 'DELETE'])
@app.route("/student", methods=["GET", "POST"])
@as_json
def students_with_id(resource_id=None):
    #  get an existent source
    if request.method == "GET":
        if resource_id is None:
            return get_students_id()
        for student in STUDENTS:
            if student.id == resource_id:
                return student.get_as_dict()
        flask.abort(404)
    # create a new source in the container
    elif request.method == "POST":
        try:
            data = json.loads(request.get_data())
            student = Student(data["name"], data["age"])
            STUDENTS.append(student)
            return "ok"
        except:
            flask.abort(400)  # raise bad request
    # overwrite an existent resource
    elif request.method == "PUT":
        try:
            data = json.loads(request.get_data())
            data["age"] = int(data["age"])
            student_found = None
            for student in STUDENTS:
                if student.id == resource_id:
                    student_found = student
            new_student = Student(data['name'], data['age'])
            new_student.id = student_found.id
            STUDENTS.append(new_student)
            return 'ok'
        except Exception as esc:
            flask.abort(400)
            return esc  # raise bad request
    elif request.method == 'DELETE':
        for student in STUDENTS:
            if student.id == resource_id:
                STUDENTS.remove(student)
                return 'ok'
            flask.abort(400)


# @app.route("/gimme")
# def gimme():
#     return render_template('index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8081, debug=True)

