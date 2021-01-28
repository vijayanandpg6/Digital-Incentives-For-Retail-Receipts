import sumTwoNumbers
import productMatch
import companyMatch
import execPyScript
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class sumNumbers(Resource):
    def get(self, first_number, second_number):
        return {'data': sumTwoNumbers.sumTwo(first_number,second_number)}

class productMatcher(Resource):
    def get(self, product):
        return {'data': productMatch.productMatch(product)}

class ExecuteObjectSegmentation(Resource):
    def get(self):
        return {'data': execPyScript.execPyScript()}

class companyMatcher(Resource):
    def get(self, company):
        return {'data': companyMatch.companyMatch(company)}

# api.add_resource(sumNumbers, '/sumtwonumbers/<first_number>/<second_number>')
api.add_resource(productMatcher, '/productMatch/<product>')
api.add_resource(companyMatcher, '/companyMatch/<company>')
api.add_resource(ExecuteObjectSegmentation, '/segmentObject/')

if __name__ == '__main__':
     app.run()