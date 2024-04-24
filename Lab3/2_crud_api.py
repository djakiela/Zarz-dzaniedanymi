from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

students = []

class StudentNames(Resource):
    def get(self,name):
        print(students)

        for stud in students:
            if stud['name'] == name:
                return stud
        
        return {'name': None}, 404
    
    def post(self,name):
        stud = {'name': name}
        students.append(stud)
        print(students)
        return stud
    
    def delete(self,name):
        for ind, stud in enumerate(students):
            if stud['name'] == name:
                delted_stud = students.pop(ind)
                return {'note': 'delete successful'}

class AllNames(Resource):

    def get(self):
        return {'students': students}

api.add_resource(StudentNames, '/student/<string:name>')
api.add_resource(AllNames, '/students')

if __name__ == '__main__':
    app.run(debug=True)