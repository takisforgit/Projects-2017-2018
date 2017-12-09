import sys
print(sys.version_info[:2])

if sys.version_info[:2] < (2, 3):
    print("Python version 2.3 or later is required for NetworkX (%d.%d detected)." %  sys.version_info[:2] )
    sys.exit(-1)
else:
    print("Python version (%d.%d detected)." %  sys.version_info[:2] )
  

del sys

