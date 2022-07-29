from random import randint
dic = [' ','й','ц','у','к','е','н','г','ш','щ','з','х','ъ','ф','ы','в','а','п','р','о','л','д','ж','э','я','ч','с','м','и','т','ь','б','ю','ё', 'Й','Ц','У','К','Е','Н','Г','Ш','Щ','З','Х','Ъ','Ф','Ы','В','А','П','Р','О','Л','Д','Ж','Э','Я','Ч','С','М','И','Т','Ь','Б','Ю','Ё']
dic_key = ['@','#', '$']
class Main:
    def __init__(self, check_work):
        self.check_work = check_work
    def start(self):
        while joker.check_work == 1:
            joker.body()
    def body(self):
        print("1). Coding")
        print("2). Decoding")
        print("3). Exit")
        a = int(input())
        if a == 1:
            joker.coding()
        elif a == 2:
            joker.decoding()
        elif a == 3:
            joker.check_work = 0
            print("Program stoped")
        else:
            print("Invalid input")
    def coding(self):
        user_input = str(input())
        answer = ''
        for h in range(len(user_input)):
            user_num = None
            time = None
            a = []
            b = [[1,2,3], [4,5,6],[7,8,9]]
            b[1][1] = dic_key[randint(0,2)]
            for l in range(len(dic)):
                if user_input[h] == dic[l]:
                    user_num = l
                    break
            if user_num < 10:
                user_num = str(0) + str(user_num)
            b[1][0] = randint(0,9)
            b[1][2] = randint(0,9)
            time = int(str(user_num)[0]) + b[1][0] + b[1][2]
            if time < 10:
                b[0][0] = 0
                b[0][2] = time
            else:
                b[0][0] = str(time)[0]
                b[0][2] = str(time)[1]
            b[0][1] = randint(0,9)
            b[2][1] = randint(0,9)
            time = int(str(user_num)[1]) + b[0][1] + b[2][1]
            if time < 10:
                b[2][0] = 0
                b[2][2] = time
            else:
                b[2][0] = str(time)[0]
                b[2][2] = str(time)[1]
            an = ''
            for k in range(len(b)):
                for l in range(len(b)):
                    an += str(b[k][l]) 
            answer += an
        print(answer)
    def decoding(self):
        user = str(input())
        answer = ''
        a = 0
        b = 9
        while b <= len(user):
            user_input = user[a:b]
            ans_1 = int(user_input[0] + user_input[2]) - (int(user_input[3]) + int(user_input[5]))
            ans_2 = int(user_input[6] + user_input[8]) - (int(user_input[1]) + int(user_input[7]))
            ad = int(str(ans_1) + str(ans_2))
            ans_all = str(dic[ad])
            a += 9
            b += 9
            answer += ans_all
        print(answer)
joker = Main(1)
joker.start()
