import subprocess

def do_pull():
    try:
        res = subprocess.check_output( ['git', 'pull'] )
        print "res = [%s]" % res
    except subprocess.CalledProcessError:
        print "Something went wrong with pulling from git..."
