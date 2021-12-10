import matlab.engine

def start_execution():

    eng = matlab.engine.start_matlab()
    eng.demo_single_tracker(nargout=0)
    #eng.quit()
