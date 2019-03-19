import sys,os, shutil

folder = sys.argv[1]

path = "./%s/" % folder
length = len(os.listdir(path))

os.makedirs("./awsfish/validation")
os.makedirs("./awsfish/train")
#os.makedirs("./awsfish/test")

train = length * 0.8
validation = length - train
#test = length - train - validation
i = 1

for filename in os.listdir(path):
    print(filename)
    if i <= train:
        shutil.move(path + filename, "./awsfish/train/" + filename)
    else:
        shutil.move(path + filename, "./awsfish/validation/" + filename)
    #else:
        #shutil.move(path + filename, "./awsfish/test/" + filename)
    i +=1
