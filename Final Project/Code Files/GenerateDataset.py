import random # for sorting and creating data pts

if __name__ == "__main__":
    file = open("8192.txt","w")        # Open the dataset file
    for i in range(8192):
        x = random.uniform(-100,100)
        y = random.uniform(-100,100)
        coordinate = str(round(x,2)) + " " + str(round(y,2))
        # print(coordinate)
        file.writelines(coordinate + "\n")