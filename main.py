from flask import Flask, render_template
import psutil
import datetime
import platform

app = Flask(__name__)


@app.route("/")
def index():
    cpu_stats = psutil.cpu_stats()  # Retorna estatisticas da CPU:
    print(cpu_stats)

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
    system, node, release, version, arch, processor = platform.uname()
    system = system.split('-')[0]

    #print("Machine OS: {} \nNode: {} \nRelease: {} \nVersion {} \nArchiteture: {} \nProcessor: {} ".format(system, node, release,version, arch, processor))
    return render_template('stats.html', physical=physical, logical=logical, boot=boot, system=system, node=node, release=release, version=version,arch=arch, processor=processor)

if __name__ == '__main__':
    app.run(debug=True)
