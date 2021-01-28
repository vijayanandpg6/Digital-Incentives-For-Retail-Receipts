import os
# os.system("D:\\Osmosis-2020\\Main\\models-1.13.0\\research\\object_detection\\object_detection_tutorial.py")

def execPyScript():
    try:
        os.chdir("D:\\Osmosis-2020\\Main\\models-1.13.0\\research\\object_detection\\")
        os.system("object_detection_tutorial.py")
    except:
        return "Failed"
    return "Success"