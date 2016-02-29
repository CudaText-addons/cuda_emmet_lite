import subprocess

def run_with_text(text, params):
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    startupinfo.wShowWindow = subprocess.SW_HIDE
    
    enc = 'cp866'
    
    try:
        p = subprocess.Popen(params, 
          startupinfo=startupinfo, 
          stdout=subprocess.PIPE, 
          stdin=subprocess.PIPE, 
          stderr=subprocess.PIPE)
    except OSError:
        raise Exception("""Cannot find executable "%s". Make sure it's in your PATH.""" % params[0])

    stdout, stderr = p.communicate(text.encode(enc))
    if stdout:
        return stdout.decode(enc)
    else:
        raise Exception('Error:\n' + stderr.decode(enc))
