import random
import time
import matplotlib.pyplot as mpl
import numpy as np
from datetime import datetime


def user_choice():
    user_choice1: int = int(input('''Enter 1 for Instructions\n Enter 2 to Practice Squares \n Enter 3 to revise squares 
Enter 4 to Practice Cube \n Enter 5 to revise Cube :'''))
    return user_choice1


def instructions():
    print('''-----INSTRUCTION-----
     1) This Program Helps you to Practice your Squares and cubes chose one and get 
    started
     2) Enter How many Questions You want
     3) Enter the starting number and ending number 
     e.g if you enter start number = 5 end number = 10 then you will be given questions from the range of 5-10 (6,9,7,8)
      provided you entered no of questions as 4 
    4) It also provides a little detailed insight such as how much time you are taking 
    against a particular number 
    5) You can check your previous scores on text-file named 'upload-time.txt' placed in 
    your main python directory 
    6) To Practice Re-Run the Program,Hope you Enjoy
            GodsOwn Knight
                  
                  ''')


def common_input():
    global tries, ques1, ques2
    tries = int(input("Enter No. of questions you want?"))
    ques1 = int(input("Enter the Starting Range number: "))
    ques2 = int(input("Enter the End Range number: "))


def condition_check():
    if tries > (ques2 - ques1) + 1:
        print("ERROR!!! Generating", tries, "unique numbers is not possible in ", ques1, "-", ques2, " range! Only ",
              (ques2 - ques1) + 1, "numbers are possible")
        status: bool = False
        return status
    else:
        status = True

        return status


def generate_num():
    global num
    a = condition_check()
    if a:
        num = random.sample(range(ques1, ques2 + 1), tries)
    else:
        exit()


def common_var():
    global score, time_list, ans_list, i, wrong_ques_list_square, wrong_ans_list_square, wrong_ques_list_cube, \
        wrong_ans_list_cube
    score = 0
    i = 0
    time_list = []
    ans_list = []
    wrong_ques_list_square = []
    wrong_ans_list_square = []
    wrong_ques_list_cube = []
    wrong_ans_list_cube = []

    return score, time_list, ans_list, i, wrong_ques_list_square, wrong_ans_list_square, wrong_ans_list_cube, \
        wrong_ques_list_cube


def square():
    global score, i, wrong_ques_list_square, wrong_ans_list_square
    common_var()

    while i < tries:
        t = time.time()
        ans = int(input("Enter Square of " + str(num[i]) + ":"))
        t1 = time.time()
        a = t1 - t
        b = round(a, 2)
        time_list.append(b)
        actual_ans = num[i] * num[i]
        ans_list.append(actual_ans)
        i += 1
        if ans == actual_ans:
            print("Correct!!!!")
            print("You took ", b, " sec")
            score += 1
        else:
            print("Wrong answer! BOO", "\n", "Correct Answer is :", actual_ans)
            score += 0
            wrong_ques_list_square.append(num[i - 1])
            wrong_ans_list_square.append(actual_ans)


def wrong_ans_square():
    if tries == score:
        print("You are Bloody Brilliant!!\n You didn't made any mistakes:)")
    else:
        print("Don't Worry We all makes mistakes along our journey\n You made mistakes in these questions")
        show_mistake = "\n".join(
            "Square of {} ----> {}".format(x, y) for x, y in zip(wrong_ques_list_square, wrong_ans_list_square))
        print(show_mistake)


def upload_time_square():
    file = open("upload-time.txt", "a")
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    file.write("\n" + dt_string + "\t Score :" + str(score) + "/" + str(
        len(num)) + " Incorrect Square Questions: " + str(wrong_ques_list_square))


def upload_time_cube():
    file = open("upload-time.txt", "a")
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    file.write("\n" + dt_string + "\t Score :" + str(score) + "/" + str(
        len(num)) + " Incorrect Cube Questions: " + str(wrong_ques_list_cube))


def cube():
    common_var()
    global score, i
    while i < tries:
        t = time.time()
        ans = int(input("Enter Cube of " + str(num[i]) + ":"))
        t1 = time.time()
        a = t1 - t
        b = round(a, 2)
        time_list.append(b)
        actual_ans = num[i] * num[i] * num[i]
        i += 1
        if ans == actual_ans:
            print("Correct!!!!")
            print("You took ", b, " sec")
            score += 1
        else:
            print("Wrong answer! BOO", "\n", "Correct Answer is :", actual_ans)
            score += 0
            wrong_ques_list_cube.append(num[i - 1])
            wrong_ans_list_cube.append(actual_ans)


def wrong_ans_cube():
    if tries == score:
        print("You are Bloody Brilliant!!\n You didn't made any mistakes:)")
    else:
        print("Don't Worry We all makes mistakes along our journey\n you made mistakes in these questions")
        show_mistake = "\n".join(
            "Square of {} ----> {}".format(x, y) for x, y in zip(wrong_ques_list_cube, wrong_ans_list_cube))
        print(show_mistake)


def display_score():
    res = "\n".join("{}      {}s".format(x, y) for x, y in zip(num, time_list))
    print("Time taken per Number")
    print(res)
    sum_list = round(sum(time_list), 2)
    avg = round(sum_list / len(time_list), 2)
    print("Total Time Taken:", sum_list, "sec", "\n", " Average time per question:", avg, "s")
    print("Pie-Chart showing time per question")
    y = np.array(time_list)
    mpl.pie(y, labels=num, autopct="%1.0f%%", shadow=True)
    mpl.title("Your Score: " + str(score) + "/" + str(len(num)) + "\n Time taken per Question(percent-wise):",
              pad=-100,
              loc="center",
              color='b',
              fontsize=15)
    mpl.show()

    print("--Coded By Ganesh---")


def revise_square():
    pract_list = [x for x in range(1, 41)]

    def squares(n):
        pract_ans = [number * number for number in range(1, n + 1)]
        return pract_ans

    res1 = "\n".join("Square of {} ----> {}".format(x, y) for x, y in zip(pract_list, squares(40)))
    print(res1)


def revise_cube():
    pract_list = [x for x in range(1, 26)]

    def squares(n):
        pract_ans = [number * number * number for number in range(1, n + 1)]
        return pract_ans

    res1 = "\n".join("Cube of {} ----> {}".format(x, y) for x, y in zip(pract_list, squares(40)))
    print(res1)


def square_control():
    common_input()
    generate_num()
    condition_check()
    square()
    display_score()
    wrong_ans_square()
    upload_time_square()


def cube_control():
    common_input()
    generate_num()
    condition_check()
    cube()
    display_score()
    wrong_ans_cube()
    upload_time_cube()


return_userchoice = user_choice()
if return_userchoice == 1:
    instructions()
elif return_userchoice == 2:
    square_control()
elif return_userchoice == 3:
    revise_square()
elif return_userchoice == 4:
    cube_control()
elif return_userchoice == 5:
    revise_cube()
else:
    print("Invalid Input")
