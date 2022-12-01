from utils import *
from flask import Flask


app = Flask(__name__)


@app.route('/')
def name_pos_skills():
   '''
   :return: выводит представление всех кандидатов, их имена, позиции, и умения
   '''
   candidates = load_candidates()
   result = ''
   for candidate in candidates:
      name = candidate['name']
      position = candidate['position']
      str_skills = candidate['skills']
      if result == '':
         result += '<pre>\n' + name + '\n' + position + '\n' + str_skills + '\n</pre>'
      else:
         result += '<pre>\n' + name + '\n' + position + '\n' + str_skills + '\n</pre>\n\n'

   return result


@app.route('/candidates/<int:pk>')
def candidate_pk(pk):
   '''
   :param pk: получает номер пк
   :return: выводит фото, имя, позицию, и умения кандидата
   '''
   candidate = get_by_pk(pk)
   name = candidate['name']
   position = candidate['position']
   str_skills = candidate['skills']
   picture = candidate['picture']
   result = f"<img src='{picture}'>\n\n<pre>\n" + name + '\n' + position + '\n' + str_skills + '\n</pre>'
   return result


@app.route('/skills/<skill>')
def candidate_skill(skill):
   '''
   :param skill: получает название умения
   :return: выводит список кандидатов - имя, позицию, умения
   '''
   candidates = get_by_skill(skill)
   result = ''
   for candidate in candidates:
      name = candidate['name']
      position = candidate['position']
      str_skills = candidate['skills']
      if result == '':
         result += '<pre>\n' + name + '\n' + position + '\n' + str_skills + '\n</pre>'
      else:
         result += '<pre>\n' + name + '\n' + position + '\n' + str_skills + '\n</pre>\n\n'
   return result

app.run()
