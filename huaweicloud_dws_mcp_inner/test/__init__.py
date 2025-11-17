import os
import sys
test_path = os.path.split(os.path.realpath(__file__))[0]
sys.path.append("{}/../src".format(test_path))