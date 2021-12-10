import os


def run_demo():
    mydir = os.getcwd()
    #print(mydir)
    mydir_temp = mydir + "\\original_dependencies\\"
    os.chdir(mydir_temp)
    #print(os.getcwd())
    from demorun import start_execution
    start_execution()

if __name__ == "__main__":

    run_demo()
