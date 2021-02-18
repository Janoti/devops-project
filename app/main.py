from flask import Flask, render_template, jsonify, abort, request
import psutil
import datetime
import platform
import os
import database.banco

app = Flask(__name__)
port = int(os.environ.get("PORT", 5000))

users = [ # Array of dictionaries. Memory Database of users
     {
      'name': 'User 1',
      'sobrenome': 'Sobrenome 1',
      'cpf': '11111111111',
      'email': 'user1@yahoo.com.br',
      'data_nasc': '09/05/1985'
      },
      {
      'name': 'User 2',
      'sobrenome': 'Sobrenome 2',
      'cpf': '22222222222',
      'email': 'user2@yahoo.com.br',
      'data_nasc': '10/06/1985'
      },
      {
      'name': 'User 3',
      'sobrenome': 'Sobrenome 3',
      'cpf': '33333333333',
      'email': 'user3@yahoo.com.br',
      'data_nasc': '13/08/1985'
      }
]


@app.route("/")
def index():
    #rows  = 0 
   # cpu_stats = psutil.cpu_stats()  # Retorna estatisticas da CPU:
    #print(cpu_stats)

    # ctx_switches: number of context switches (voluntary + involuntary) since boot.
    # /interrupts: number of interrupts since boot.
    # /soft_interrupts: number of software interrupts since boot. Always set to 0 on Windows and SunOS.
    # syscalls: number of system calls since boot. Always set to 0 on Linux.

    cpu_logical_count = psutil.cpu_count(logical=True)  # Número de CPUs lógicas (Physical cores only (hyper thread excluded)
    cpu_physical_count = psutil.cpu_count(logical=False)  # Numero de CPUs Físicas
    logical = "Your computer have {} logical cpus cores !".format(cpu_logical_count)
    #print(logical)
    physical = "Your computer have {} physical cpus cores !".format(cpu_physical_count)
    #print(physical)

    boot_time = datetime.datetime.fromtimestamp(psutil.boot_time())

    boot = "You are logged in your system since: {}".format(boot_time)
    #print(boot)

    # biblioteca Platform. plataform.uname retorna 6 atributos (system, node, release, version, machine e processor)
    system = platform.system()
    node = platform.node()
    release = platform.release()
    version = platform.version()
    py_ver = platform.python_version()
    proc = platform.processor()


    conn = database.banco.create_connection()
    database.banco.create_table(conn)

    if conn is not None:
        counter = database.banco.insert_table(conn, physical, logical, boot, system, node, release, version, py_ver, proc)
    else:
        print ("ERROR")

    # database.banco.print_data()
  
    #print("Machine OS: {} \nNode: {} \nRelease: {} \nVersion {} \nArchiteture: {} \nProcessor: {} ".format(system, node, release,version, py_ver, processor))
    return render_template('stats.html', counter = counter, physical=physical, logical=logical, boot=boot, system=system, node=node, release=release, version=version,py_ver=py_ver, proc=proc)

@app.route("/db")
def db_list():
   conn = database.banco.create_connection()
   rows =  database.banco.print_data(conn)
   return render_template('database.html', rows = rows)

@app.route("/login")
def login():
    hello = "Criar uma tela de login (todo)"
    return render_template('login.html', hello=hello)

@app.route("/users") 
def get_users():
    return jsonify({'users': users})


@app.route("/users/<string:cpf>", methods=['GET']) 
def search_cpf(cpf):
    user = [user for user in users if user['cpf'] == cpf]
    if len(user) == 0:
        abort(404)
    return jsonify({'user': user[0]})


@app.route("/users", methods=['POST'])
def insert_user():
    if not request.json:
        abort(400)
    payload = request.get_json(force=True)
    user = {
        'nome': payload['nome'],
        'sobrenome': payload['sobrenome'],
        'cpf': payload['cpf'],
        'email': payload['email'],
        'data_nasc': payload['data_nasc']
    }
    users.append(user)
    return jsonify({'users': user}), 201

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=port)

