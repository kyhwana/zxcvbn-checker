__author__ = 'kyhwana'
import zxcvbn
import sys
passwordfile = open(sys.argv[1], 'r')
entropyscore = sys.argv[2]

for line in passwordfile:
    result = zxcvbn.password_strength(line.rstrip("\n"))
    if result["entropy"] > float(entropyscore):
        print("Password: " + result["password"] + " Score:" + repr(result["score"]) + " Entropy:" + repr(result["entropy"]) )




