
startx = int(input("start x:"))
starty = int(input("start y:"))

def laplace(points):
    e = ""
    equation = ""
    x = 0
    for point in points:
        for p in points:
            if not p == point:
                if p[0] == 0:
                    e+=f"(x)*"
                elif p[0] > 0:
                    e+=f"(x-{p[0]})*"
                else:
                    e+=f"(x+{-p[0]})*"
            else:
                x = p[0]    
        if point[1] == 0:
            e = ""
            continue
        if eval(e[:-1])/point[1] > 1:
            e+="1/"+str(round(eval(e[:-1])/point[1]))
        else:
            e+=str(round(eval(e[:-1])/point[1]))
        equation+=f"+{e}"
        e = ""

    return equation

def straight(points):
    equation = ""
    e = ""
    for i in range(len(points)):
        if i == len(points)-1:
            break
        if points[i][0] == 0:
            e += f"(abs(x)/(x)+1)*"
        elif points[i][0] > 0:
            e += f"(abs(x-{points[i][0]})/(x-{points[i][0]})+1)*"
        else:
            e += f"(abs(x+{-points[i][0]})/(x+{-points[i][0]})+1)*"

        if points[i+1][0] == 0:
            e += f"(abs(x)/(x)-1)*"
        elif points[i+1][0] > 0:
            e += f"(abs(x-{points[i+1][0]})/(x-{points[i+1][0]})-1)*"
        else:
            e += f"(abs(x+{-points[i+1][0]})/(x+{-points[i+1][0]})-1)*"

        if points[i][0] > 0 and points[i][1] > 0:
            e+=f"({round((points[i+1][1]-points[i][1])/(points[i+1][0]-points[i][0]),3)}(x-{points[i][0]})+{points[i][1]})"
        elif points[i][0] < 0 and points[i][1] > 0:
            e+=f"({round((points[i+1][1]-points[i][1])/(points[i+1][0]-points[i][0]),3)}(x+{-points[i][0]})+{points[i][1]})"
        elif points[i][0] > 0 and points[i][1] < 0:
            e+=f"({round((points[i+1][1]-points[i][1])/(points[i+1][0]-points[i][0]),3)}(x-{points[i][0]})-{-points[i][1]})"
        else:
            e+=f"({round((points[i+1][1]-points[i][1])/(points[i+1][0]-points[i][0]),3)}(x+{-points[i][0]})-{-points[i][1]})"

        equation+=f"-1/4{e}"
        e = ""
    return equation

def straightnobreaks(points):
    equation = ""
    e = ""
    for i in range(len(points)):
        if i == len(points)-1:
            break
        if points[i][0] == 0:
            e += f"(abs(x-1)-abs(x)-1)*"
        elif points[i][0] > 0:
            e += f"(abs((x-{points[i][0]})-1)-abs((x-{points[i][0]}))-1)*"
        else:
            e += f"(abs((x+{-points[i][0]})-1)-abs((x+{-points[i][0]}))-1)*"

        if points[i+1][0] == 0:
            e += f"(abs(x-1)-abs(x)+1)*"
        elif points[i+1][0] > 0:
            e += f"(abs((x-{points[i+1][0]})-1)-abs((x-{points[i+1][0]}))+1)*"
        else:
            e += f"(abs((x+{-points[i+1][0]})-1)-abs((x+{-points[i+1][0]}))+1)*"

        if points[i][0] > 0 and points[i][1] > 0:
            e+=f"({round((points[i+1][1]-points[i][1])/(points[i+1][0]-points[i][0]),3)}(x-{points[i][0]})+{points[i][1]})"
        elif points[i][0] < 0 and points[i][1] > 0:
            e+=f"({round((points[i+1][1]-points[i][1])/(points[i+1][0]-points[i][0]),3)}(x+{-points[i][0]})+{points[i][1]})"
        elif points[i][0] > 0 and points[i][1] < 0:
            e+=f"({round((points[i+1][1]-points[i][1])/(points[i+1][0]-points[i][0]),3)}(x-{points[i][0]})-{-points[i][1]})"
        else:
            e+=f"({round((points[i+1][1]-points[i][1])/(points[i+1][0]-points[i][0]),3)}(x+{-points[i][0]})-{-points[i][1]})"

        equation+=f"-1/4{e}"
        e = ""
    return equation



while True:
    points = [[startx,starty]]
    while True:
        x = input("x:")
        if x == "":
            break
        y = int(input("y:"))
        x=int(x)

        points.append([x,y])

    print(straightnobreaks(points))