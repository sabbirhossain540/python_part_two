try:
    f = open('simple.txt','w')
    f.write("Test write ti Simple text!!")
except:
    print("Error: Could Not Find file or Read Data")
else:
    print("Success!")
    f.close()
