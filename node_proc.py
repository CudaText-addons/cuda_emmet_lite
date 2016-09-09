import os
import subprocess

MSG_CANNOT_RUN_NODE = "Cannot run Node.js. Make sure it's in your PATH."

def run_node(text, params_list):
    enc = 'utf8'
    if os.name!='posix':
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        startupinfo.wShowWindow = subprocess.SW_HIDE
        try:
            p = subprocess.Popen(['node'] + params_list, 
              startupinfo=startupinfo, 
              stdout=subprocess.PIPE, 
              stdin=subprocess.PIPE, 
              stderr=subprocess.PIPE)
        except OSError:
            raise Exception(MSG_CANNOT_RUN_NODE)
    else:
        try:
            p = subprocess.Popen(['nodejs'] + params_list, 
              stdout=subprocess.PIPE, 
              stdin=subprocess.PIPE, 
              stderr=subprocess.PIPE)
        except OSError:
            raise Exception(MSG_CANNOT_RUN_NODE)
    

    stdout, stderr = p.communicate(text.encode(enc))
    if stdout:
        return stdout.decode(enc)
    else:
        raise Exception('Error:\n' + stderr.decode(enc))
