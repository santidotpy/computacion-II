from subprocess import Popen, PIPE


# returns commands messages
def exe_commands(cmd):
    proc = Popen([cmd], stdout=PIPE, stderr=PIPE, shell=True)
    out, err = proc.communicate()

    if err != b'':
        return 'ERROR\n' + err.decode()
    else:
        return 'OK\n' + out.decode()