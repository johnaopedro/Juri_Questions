import sys
try:
        vetordematriz = []
        for line in sys.stdin:
            ordem=int(line)
            if ordem==0:
                print("vai ter copa!")
            else:
                print("vai ter duas!")
except Exception as e:
    print("Ocorreu um erro:", e)