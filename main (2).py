import time


class Biblio():
    def __init__(self):
        self.book = []
        self.date = []
        self.autor = []
        self.tupe = []

    class Diary(object):
        def __init__(self):
            self.m = {'Time': 0, 'Squats': 0, 'Push-ups': 0, 'Pull-ups': 0, 'Distance': 0, 'Calories': 0}
            self.t = {'Time': 0, 'Squats': 0, 'Push-ups': 0, 'Pull-ups': 0, 'Distance': 0, 'Calories': 0}
            self.w = {'Time': 0, 'Squats': 0, 'Push-ups': 0, 'Pull-ups': 0, 'Distance': 0, 'Calories': 0}
            self.th = {'Time': 0, 'Squats': 0, 'Push-ups': 0, 'Pull-ups': 0, 'Distance': 0, 'Calories': 0}
            self.f = {'Time': 0, 'Squats': 0, 'Push-ups': 0, 'Pull-ups': 0, 'Distance': 0, 'Calories': 0}
            self.sat = {'Time': 0, 'Squats': 0, 'Push-ups': 0, 'Pull-ups': 0, 'Distance': 0, 'Calories': 0}
            self.sun = {'Time': 0, 'Squats': 0, 'Push-ups': 0, 'Pull-ups': 0, 'Distance': 0, 'Calories': 0}
            print("\nYou successfully created a diary\n")

        def upgrade_day(self, day):
            flag = False
            try:
                if day == "Monday":
                    time = int(input("Give training time(in minutes)\n"))
                    self.m["Time"] = str(time)
                    pric = int(input("Give Number of squats(number)\n"))
                    self.m["Squats"] = str(pric)
                    otz = int(input("Give Number of push-ups(number)\n"))
                    self.m["Push-ups"] = str(otz)
                    pod = int(input("Give Number of pull-ups(number)\n"))
                    self.m["Pull-ups"] = str(pod)
                    km = int(input("Give Number of kilometers traveled(number)\n"))
                    self.m["Distance"] = str(km)
                    kal = int(input("Give count of calories(Ate))(number)\n"))
                    self.m["Calories"] = str(kal)
                    flag = True
                if day == "Tuesday":
                    time = int(input("Give training time(in minutes)\n"))
                    self.t["Time"] = str(time)
                    pric = int(input("Give Number of squats(number)\n"))
                    self.t["Squats"] = str(pric)
                    otz = int(input("Give Number of push-ups(number)\n"))
                    self.t["Push-ups"] = str(otz)
                    pod = int(input("Give Number of pull-ups(number)\n"))
                    self.t["Pull-ups"] = str(pod)
                    km = int(input("Give Number of kilometers traveled(number)\n"))
                    self.t["Distance"] = str(km)
                    kal = int(input("Give count of calories(Ate))(number)\n"))
                    self.t["Calories"] = str(kal)
                    flag = True
                if day == "Wednesday":
                    time = int(input("Give training time(in minutes)\n"))
                    self.w["Time"] = str(time)
                    pric = int(input("Give Number of squats(number)\n"))
                    self.w["Squats"] = str(pric)
                    otz = int(input("Give Number of push-ups(number)\n"))
                    self.w["Push-ups"] = str(otz)
                    pod = int(input("Give Number of pull-ups(number)\n"))
                    self.w["Pull-ups"] = str(pod)
                    km = int(input("Give Number of kilometers traveled(number)\n"))
                    self.w["Distance"] = str(km)
                    kal = int(input("Give count of calories(Ate))(number)\n"))
                    self.w["Calories"] = str(kal)
                    flag = True
                if day == "Thursday":
                    time = int(input("Give training time(in minutes)\n"))
                    self.th["Time"] = str(time)
                    pric = int(input("Give Number of squats(number)\n"))
                    self.th["Squats"] = str(pric)
                    otz = int(input("Give Number of push-ups(number)\n"))
                    self.th["Push-ups"] = str(otz)
                    pod = int(input("Give Number of pull-ups(number)\n"))
                    self.th["Pull-ups"] = str(pod)
                    km = int(input("Give Number of kilometers traveled(number)\n"))
                    self.th["Distance"] = str(km)
                    kal = int(input("Give count of calories(Ate))(number)\n"))
                    self.th["Calories"] = str(kal)
                    flag = True
                if day == "Friday":
                    time = int(input("Give training time(in minutes)\n"))
                    self.f["Time"] = str(time)
                    pric = int(input("Give Number of squats(number)\n"))
                    self.f["Squats"] = str(pric)
                    otz = int(input("Give Number of push-ups(number)\n"))
                    self.f["Push-ups"] = str(otz)
                    pod = int(input("Give Number of pull-ups(number)\n"))
                    self.f["Pull-ups"] = str(pod)
                    km = int(input("Give Number of kilometers traveled(number)\n"))
                    self.f["Distance"] = str(km)
                    kal = int(input("Give count of calories(Ate))(number)\n"))
                    self.f["Calories"] = str(kal)
                    flag = True
                if day == "Saturday":
                    time = int(input("Give training time(in minutes)\n"))
                    self.sat["Time"] = str(time)
                    pric = int(input("Give Number of squats(number)\n"))
                    self.sat["Squats"] = str(pric)
                    otz = int(input("Give Number of push-ups(number)\n"))
                    self.sat["Push-ups"] = str(otz)
                    pod = int(input("Give Number of pull-ups(number)\n"))
                    self.sat["Pull-ups"] = str(pod)
                    km = int(input("Give Number of kilometers traveled(number)\n"))
                    self.sat["Distance"] = str(km)
                    kal = int(input("Give count of calories(Ate))(number)\n"))
                    self.sat["Calories"] = str(kal)
                    flag = True
                if day == "Sunday":
                    time = int(input("Give training time(in minutes)\n"))
                    self.sun["Time"] = str(time)
                    pric = int(input("Give Number of squats(number)\n"))
                    self.sun["Squats"] = str(pric)
                    otz = int(input("Give Number of push-ups(number)\n"))
                    self.sun["Push-ups"] = str(otz)
                    pod = int(input("Give Number of pull-ups(number)\n"))
                    self.sun["Pull-ups"] = str(pod)
                    km = int(input("Give Number of kilometers traveled(number)\n"))
                    self.sun["Distance"] = str(km)
                    kal = int(input("Give count of calories(Ate))(number)\n"))
                    self.sun["Calories"] = str(kal)
                    flag = True
            except ValueError:
                print("\nYou did wrong input!!\n")
                return
            if flag is False:
                print("\nYou did wrong day!!!\n")
                return

        def sort_cal(self, par):
            flag = False
            list = []
            if par == "Time":
                flag = True
                list.append(int(self.m.get("Time")))
                list.append(int(self.t.get("Time")))
                list.append(int(self.w.get("Time")))
                list.append(int(self.th.get("Time")))
                list.append(int(self.f.get("Time")))
                list.append(int(self.sat.get("Time")))
                list.append(int(self.sun.get("Time")))
                copy_list = [1, 2, 3, 4, 5, 6, 7]
                for i in range(len(list) - 1):
                    for j in range(len(list) - i - 1):
                        if list[j] < list[j + 1]:
                            list[j], list[j + 1] = list[j + 1], list[j]
                            copy_list[j], copy_list[j+1] = copy_list[j+1], copy_list[j]
                for i in range(len(copy_list)):
                    if copy_list[i] == 1:
                        print("Monday", self.m)
                    if copy_list[i] == 2:
                        print("Tuesday", self.t)
                    if copy_list[i] == 3:
                        print("Wednesday", self.w)
                    if copy_list[i] == 4:
                        print("Thursday", self.th)
                    if copy_list[i] == 5:
                        print("Friday", self.f)
                    if copy_list[i] == 6:
                        print("Saturday", self.sat)
                    if copy_list[i] == 7:
                        print("Sunday", self.sun)
            if par == "Squats":
                flag = True
                list.append(int(self.m.get("Squats")))
                list.append(int(self.t.get("Squats")))
                list.append(int(self.w.get("Squats")))
                list.append(int(self.th.get("Squats")))
                list.append(int(self.f.get("Squats")))
                list.append(int(self.sat.get("Squats")))
                list.append(int(self.sun.get("Squats")))
                copy_list = [1, 2, 3, 4, 5, 6, 7]
                for i in range(len(list) - 1):
                    for j in range(len(list) - i - 1):
                        if list[j] < list[j + 1]:
                            list[j], list[j + 1] = list[j + 1], list[j]
                            copy_list[j], copy_list[j+1] = copy_list[j+1], copy_list[j]
                for i in range(len(copy_list)):
                    if copy_list[i] == 1:
                        print("Monday", self.m)
                    if copy_list[i] == 2:
                        print("Tuesday", self.t)
                    if copy_list[i] == 3:
                        print("Wednesday", self.w)
                    if copy_list[i] == 4:
                        print("Thursday", self.th)
                    if copy_list[i] == 5:
                        print("Friday", self.f)
                    if copy_list[i] == 6:
                        print("Saturday", self.sat)
                    if copy_list[i] == 7:
                        print("Sunday", self.sun)
            if par == "Push-ups":
                flag = True
                list.append(int(self.m.get("Push-ups")))
                list.append(int(self.t.get("Push-ups")))
                list.append(int(self.w.get("Push-ups")))
                list.append(int(self.th.get("Push-ups")))
                list.append(int(self.f.get("Push-ups")))
                list.append(int(self.sat.get("Push-ups")))
                list.append(int(self.sun.get("Push-ups")))
                copy_list = [1, 2, 3, 4, 5, 6, 7]
                for i in range(len(list) - 1):
                    for j in range(len(list) - i - 1):
                        if list[j] < list[j + 1]:
                            list[j], list[j + 1] = list[j + 1], list[j]
                            copy_list[j], copy_list[j+1] = copy_list[j+1], copy_list[j]
                for i in range(len(copy_list)):
                    if copy_list[i] == 1:
                        print("Monday", self.m)
                    if copy_list[i] == 2:
                        print("Tuesday", self.t)
                    if copy_list[i] == 3:
                        print("Wednesday", self.w)
                    if copy_list[i] == 4:
                        print("Thursday", self.th)
                    if copy_list[i] == 5:
                        print("Friday", self.f)
                    if copy_list[i] == 6:
                        print("Saturday", self.sat)
                    if copy_list[i] == 7:
                        print("Sunday", self.sun)
            if par == "Pull-ups":
                flag = True
                list.append(int(self.m.get("Pull-ups")))
                list.append(int(self.t.get("Pull-ups")))
                list.append(int(self.w.get("Pull-ups")))
                list.append(int(self.th.get("Pull-ups")))
                list.append(int(self.f.get("Pull-ups")))
                list.append(int(self.sat.get("Pull-ups")))
                list.append(int(self.sun.get("Pull-ups")))
                copy_list = [1, 2, 3, 4, 5, 6, 7]
                for i in range(len(list) - 1):
                    for j in range(len(list) - i - 1):
                        if list[j] < list[j + 1]:
                            list[j], list[j + 1] = list[j + 1], list[j]
                            copy_list[j], copy_list[j+1] = copy_list[j+1], copy_list[j]
                for i in range(len(copy_list)):
                    if copy_list[i] == 1:
                        print("Monday", self.m)
                    if copy_list[i] == 2:
                        print("Tuesday", self.t)
                    if copy_list[i] == 3:
                        print("Wednesday", self.w)
                    if copy_list[i] == 4:
                        print("Thursday", self.th)
                    if copy_list[i] == 5:
                        print("Friday", self.f)
                    if copy_list[i] == 6:
                        print("Saturday", self.sat)
                    if copy_list[i] == 7:
                        print("Sunday", self.sun)
            if par == "Distance":
                flag = True
                list.append(int(self.m.get("Distance")))
                list.append(int(self.t.get("Distance")))
                list.append(int(self.w.get("Distance")))
                list.append(int(self.th.get("Distance")))
                list.append(int(self.f.get("Distance")))
                list.append(int(self.sat.get("Distance")))
                list.append(int(self.sun.get("Distance")))
                copy_list = [1, 2, 3, 4, 5, 6, 7]
                for i in range(len(list) - 1):
                    for j in range(len(list) - i - 1):
                        if list[j] < list[j + 1]:
                            list[j], list[j + 1] = list[j + 1], list[j]
                            copy_list[j], copy_list[j+1] = copy_list[j+1], copy_list[j]
                for i in range(len(copy_list)):
                    if copy_list[i] == 1:
                        print("Monday", self.m)
                    if copy_list[i] == 2:
                        print("Tuesday", self.t)
                    if copy_list[i] == 3:
                        print("Wednesday", self.w)
                    if copy_list[i] == 4:
                        print("Thursday", self.th)
                    if copy_list[i] == 5:
                        print("Friday", self.f)
                    if copy_list[i] == 6:
                        print("Saturday", self.sat)
                    if copy_list[i] == 7:
                        print("Sunday", self.sun)
            if par == "Calories":
                flag = True
                list.append(int(self.m.get("Calories")))
                list.append(int(self.t.get("Calories")))
                list.append(int(self.w.get("Calories")))
                list.append(int(self.th.get("Calories")))
                list.append(int(self.f.get("Calories")))
                list.append(int(self.sat.get("Calories")))
                list.append(int(self.sun.get("Calories")))
                copy_list = [1, 2, 3, 4, 5, 6, 7]
                for i in range(len(list) - 1):
                    for j in range(len(list) - i - 1):
                        if list[j] < list[j + 1]:
                            list[j], list[j + 1] = list[j + 1], list[j]
                            copy_list[j], copy_list[j+1] = copy_list[j+1], copy_list[j]
                for i in range(len(copy_list)):
                    if copy_list[i] == 1:
                        print("Monday", self.m)
                    if copy_list[i] == 2:
                        print("Tuesday", self.t)
                    if copy_list[i] == 3:
                        print("Wednesday", self.w)
                    if copy_list[i] == 4:
                        print("Thursday", self.th)
                    if copy_list[i] == 5:
                        print("Friday", self.f)
                    if copy_list[i] == 6:
                        print("Saturday", self.sat)
                    if copy_list[i] == 7:
                        print("Sunday", self.sun)
            if flag is False:
                print("\nYou did wrong parament\n")
                return

        def best_med(self, par):
            best = 0
            sum = 0
            flag = False
            if par == "Time":
                if int(self.m.get("Time")) > best:
                    best = int(self.m.get("Time"))
                    sum = sum + int(self.m.get("Time"))
                if int(self.t.get("Time")) > best:
                    best = int(self.t.get("Time"))
                    sum = sum + int(self.t.get("Time"))
                if int(self.w.get("Time")) > best:
                    sum = sum + int(self.w.get("Time"))
                    best = int(self.w.get("Time"))
                if int(self.th.get("Time")) > best:
                    sum = sum + int(self.w.get("Time"))
                    best = int(self.th.get("Time"))
                if int(self.f.get("Time")) > best:
                    sum = sum + int(self.f.get("Time"))
                    best = int(self.f.get("Time"))
                if int(self.sat.get("Time")) > best:
                    sum = sum + int(self.sat.get("Time"))
                    best = int(self.sat.get("Time"))
                if int(self.sun.get("Time")) > best:
                    sum = sum + int(self.sun.get("Time"))
                    best = int(self.sun.get("Time"))
                flag = True
                print("Best " + str(par), best)
                print("Medium " + str(par), round(sum/7, 0))
            if par == "Squats":
                if int(self.m.get("Squats")) > best:
                    sum = sum + int(self.m.get("Squats"))
                    best = int(self.m.get("Squats"))
                if int(self.t.get("Squats")) > best:
                    sum = sum + int(self.t.get("Squats"))
                    best = int(self.t.get("Squats"))
                if int(self.w.get("Squats")) > best:
                    sum = sum + int(self.w.get("Squats"))
                    best = int(self.w.get("Squats"))
                if int(self.th.get("Squats")) > best:
                    sum = sum + int(self.th.get("Squats"))
                    best = int(self.th.get("Squats"))
                if int(self.f.get("Squats")) > best:
                    sum = sum + int(self.f.get("Squats"))
                    best = int(self.f.get("Squats"))
                if int(self.sat.get("Squats")) > best:
                    sum = sum + int(self.sat.get("Squats"))
                    best = int(self.sat.get("Squats"))
                if int(self.sun.get("Squats")) > best:
                    sum = sum + int(self.sun.get("Squats"))
                    best = int(self.sun.get("Squats"))
                flag = True
                print("Best" + str(par), best)
                print("Medium " + str(par), round(sum / 7, 0))
            if par == "Push-ups":
                if int(self.m.get("Push-ups")) > best:
                    sum = sum + int(self.m.get("Push-ups"))
                    best = int(self.m.get("Push-ups"))
                if int(self.t.get("Push-ups")) > best:
                    sum = sum + int(self.t.get("Push-ups"))
                    best = int(self.t.get("Push-ups"))
                if int(self.w.get("Push-ups")) > best:
                    sum = sum + int(self.w.get("Push-ups"))
                    best = int(self.w.get("Push-ups"))
                if int(self.th.get("Push-ups")) > best:
                    sum = sum + int(self.th.get("Push-ups"))
                    best = int(self.th.get("Push-ups"))
                if int(self.f.get("Push-ups")) > best:
                    sum = sum + int(self.f.get("Push-ups"))
                    best = int(self.f.get("Push-ups"))
                if int(self.sat.get("Push-ups")) > best:
                    sum = sum + int(self.sat.get("Push-ups"))
                    best = int(self.sat.get("Push-ups"))
                if int(self.sun.get("Push-ups")) > best:
                    sum = sum + int(self.sun.get("Push-ups"))
                    best = int(self.sun.get("Push-ups"))
                flag = True
                print("Best" + str(par), best)
                print("Medium " + str(par), round(sum / 7, 0))
            if par == "Pull-ups":
                if int(self.m.get("Pull-ups")) > best:
                    sum = sum + int(self.m.get("Pull-ups"))
                    best = int(self.m.get("Pull-ups"))
                if int(self.t.get("Pull-ups")) > best:
                    sum = sum + int(self.t.get("Pull-ups"))
                    best = int(self.t.get("Pull-ups"))
                if int(self.w.get("Pull-ups")) > best:
                    sum = sum + int(self.w.get("Pull-ups"))
                    best = int(self.w.get("Pull-ups"))
                if int(self.th.get("Pull-ups")) > best:
                    sum = sum + int(self.th.get("Pull-ups"))
                    best = int(self.th.get("Pull-ups"))
                if int(self.f.get("Pull-ups")) > best:
                    sum = sum + int(self.f.get("Pull-ups"))
                    best = int(self.f.get("Pull-ups"))
                if int(self.sat.get("Pull-ups")) > best:
                    sum = sum + int(self.sat.get("Pull-ups"))
                    best = int(self.sat.get("Pull-ups"))
                if int(self.sun.get("Pull-ups")) > best:
                    sum = sum + int(self.sun.get("Pull-ups"))
                    best = int(self.sun.get("Pull-ups"))
                flag = True
                print("Best" + str(par), best)
                print("Medium " + str(par), round(sum / 7, 0))
            if par == "Distance":
                if int(self.m.get("Distance")) > best:
                    sum = sum + int(self.m.get("Distance"))
                    best = int(self.m.get("Distance"))
                if int(self.t.get("Distance")) > best:
                    sum = sum + int(self.t.get("Distance"))
                    best = int(self.t.get("Distance"))
                if int(self.w.get("Distance")) > best:
                    sum = sum + int(self.w.get("Distance"))
                    best = int(self.w.get("Distance"))
                if int(self.th.get("Distance")) > best:
                    sum = sum + int(self.th.get("Distance"))
                    best = int(self.th.get("Distance"))
                if int(self.f.get("Distance")) > best:
                    sum = sum + int(self.f.get("Distance"))
                    best = int(self.f.get("Distance"))
                if int(self.sat.get("Distance")) > best:
                    sum = sum + int(self.sat.get("Distance"))
                    best = int(self.sat.get("Distance"))
                if int(self.sun.get("Distance")) > best:
                    sum = sum + int(self.sun.get("Distance"))
                    best = int(self.sun.get("Distance"))
                flag = True
                print("Best" + str(par), best)
                print("Medium " + str(par), round(sum / 7, 0))
            if par == "Calories":
                if int(self.m.get("Calories")) > best:
                    sum = sum + int(self.m.get("Calories"))
                    best = int(self.m.get("Calories"))
                if int(self.t.get("Calories")) > best:
                    sum = sum + int(self.t.get("Calories"))
                    best = int(self.t.get("Calories"))
                if int(self.w.get("Calories")) > best:
                    sum = sum + int(self.w.get("Calories"))
                    best = int(self.w.get("Calories"))
                if int(self.th.get("Calories")) > best:
                    sum = sum + int(self.th.get("Calories"))
                    best = int(self.th.get("Calories"))
                if int(self.f.get("Calories")) > best:
                    sum = sum + int(self.f.get("Calories"))
                    best = int(self.f.get("Calories"))
                if int(self.sat.get("Calories")) > best:
                    sum = sum + int(self.sat.get("Calories"))
                    best = int(self.sat.get("Calories"))
                if int(self.sun.get("Calories")) > best:
                    sum = sum + int(self.sun.get("Calories"))
                    best = int(self.sun.get("Calories"))
                flag = True
                print("Best" + str(par), best)
                print("Medium " + str(par), round(sum / 7, 0))
            if flag is False:
                print("\n You did wront parament\n")
                return

        def call_kall(self, day):
            flag = False
            if day == "Monday":
                print("\nMonday\n")
                t = int(self.m.get("Time"))
                p = int(self.m.get("Squats"))
                o = int(self.m.get("Push-ups"))
                pod = int(self.m.get("Pull-ups"))
                km = int(self.m.get("Distance"))
                kal = int(self.m.get("Calories"))
                over = (p*0.05 + o * 0.05 + pod * 0.03 + km * 0.07 + km*0.1) * t
                print("Количество потраченных калорий за день -", round(over, 0))
                print("Разница полученных и потраченных калорий - ", round(kal - over, 0))
                flag = True
            if day == "Tuesday":
                print("\nTuesday\n")
                t = int(self.t.get("Time"))
                p = int(self.t.get("Squats"))
                o = int(self.t.get("Push-ups"))
                pod = int(self.t.get("Pull-ups"))
                km = int(self.t.get("Distance"))
                kal = int(self.t.get("Calories"))
                over = (p*0.05 + o * 0.05 + pod * 0.03 + km * 0.07 + km*0.1) * t
                print("Количество потраченных калорий за день -", round(over, 0))
                print("Разница полученных и потраченных калорий - ", round(kal - over, 0))
                flag = True
            if day == "Wednesday":
                print("\nWednesday\n")
                t = int(self.w.get("Time"))
                p = int(self.w.get("Squats"))
                o = int(self.w.get("Push-ups"))
                pod = int(self.w.get("Pull-ups"))
                km = int(self.w.get("Distance"))
                kal = int(self.w.get("Calories"))
                over = (p*0.05 + o * 0.05 + pod * 0.03 + km * 0.07 + km*0.1) * t
                print("Количество потраченных калорий за день -", round(over, 0))
                print("Разница полученных и потраченных калорий - ", round(kal - over, 0))
                flag = True
            if day == "Thursday":
                print("\nThursday\n")
                t = int(self.th.get("Time"))
                p = int(self.th.get("Squats"))
                o = int(self.th.get("Push-ups"))
                pod = int(self.th.get("Pull-ups"))
                km = int(self.th.get("Distance"))
                kal = int(self.th.get("Calories"))
                over = (p*0.05 + o * 0.05 + pod * 0.03 + km * 0.07 + km*0.1) * t
                print("Количество потраченных калорий за день -", round(over, 0))
                print("Разница полученных и потраченных калорий - ", round(kal - over, 0))
                flag = True
            if day == "Friday":
                print("\nFriday\n")
                t = int(self.f.get("Time"))
                p = int(self.f.get("Squats"))
                o = int(self.f.get("Push-ups"))
                pod = int(self.f.get("Pull-ups"))
                km = int(self.f.get("Distance"))
                kal = int(self.f.get("Calories"))
                over = (p*0.05 + o * 0.05 + pod * 0.03 + km * 0.07 + km*0.1) * t
                print("Количество потраченных калорий за день -", round(over, 0))
                print("Разница полученных и потраченных калорий - ", round(kal - over, 0))
                flag = True
            if day == "Saturday":
                print("\nSaturday\n")
                t = int(self.sat.get("Time"))
                p = int(self.sat.get("Squats"))
                o = int(self.sat.get("Push-ups"))
                pod = int(self.sat.get("Pull-ups"))
                km = int(self.sat.get("Distance"))
                kal = int(self.sat.get("Calories"))
                over = (p*0.05 + o * 0.05 + pod * 0.03 + km * 0.07 + km*0.1) * t
                print("Количество потраченных калорий за день -", round(over, 0))
                print("Разница полученных и потраченных калорий - ", round(kal - over, 0))
                flag = True
            if day == "Sunday":
                print("\nSunday\n")
                t = int(self.sun.get("Time"))
                p = int(self.sun.get("Squats"))
                o = int(self.sun.get("Push-ups"))
                pod = int(self.sun.get("Pull-ups"))
                km = int(self.sun.get("Distance"))
                kal = int(self.sun.get("Calories"))
                over = (p*0.05 + o * 0.05 + pod * 0.03 + km * 0.07 + km*0.1) * t
                print("Количество потраченных калорий за день -", round(over, 0))
                print("Разница полученных и потраченных калорий - ", round(kal - over, 0))
                flag = True
            if flag is False:
                print("\nYou give wrong day\n")
                return

        def write_all(self, day):
            flag = False
            if day == "Monday":
                print("\nMonday\n")
                flag = True
                for key, value in self.m.items():
                    print("{0}: {1}".format(key, value))
            if day == "Tuesday":
                print("\nTuesday\n")
                flag = True
                for key, value in self.t.items():
                    print("{0}: {1}".format(key, value))
            if day == "Wednesday":
                print("\nWednesday\n")
                flag = True
                for key, value in self.w.items():
                    print("{0}: {1}".format(key, value))
            if day == "Thursday":
                print("\nThursday\n")
                flag = True
                for key, value in self.th.items():
                    print("{0}: {1}".format(key, value))
            if day == "Friday":
                flag = True
                print("\nFriday\n")
                for key, value in self.f.items():
                    print("{0}: {1}".format(key, value))
            if day == "Saturday":
                print("\nSaturday\n")
                flag = True
                for key, value in self.sat.items():
                    print("{0}: {1}".format(key, value))
            if day == "Sunday":
                print("\nSunday\n")
                flag = True
                for key, value in self.sun.items():
                    print("{0}: {1}".format(key, value))
            if flag is False:
                print("\nYpu did wrong day\n")
                return

    def write_search_date(self, checker):
        try:
            valid_date = time.strptime(checker, '%m/%d/%Y')
        except ValueError:
            print('\nInvalid date!\n')
            return
        check_list = []
        iner_list = []
        for i in range(len(self.date)):
            if self.date[i] == valid_date:
                check_list.append(self.date[i])
                iner_list.append(i)
        if len(check_list) == 0:
            print("\nGot nothing for your search\n")
        else:
            print("\nFind by date - ", str(checker), "\n")
            for j in range(len(iner_list)):
                print("№ {}".format(j + 1), self.book[iner_list[j]], self.autor[iner_list[j]], self.tupe[iner_list[j]])

    def write_search_book(self, checker):
        check_list = []
        iner_list = []
        for i in range(len(self.book)):
            if self.book[i] == str(checker):
                check_list.append(self.book[i])
                iner_list.append(i)
        if len(check_list) == 0:
            print("\nGot nothing for your search\n")
        else:
            print("\nFind by name of book - ", str(checker), "\n")
            for j in range(len(iner_list)):
                print("№ {}".format(j + 1),
                      str(self.date[iner_list[j]].tm_mon) + "/" + str(self.date[iner_list[j]].tm_mday)
                      + "/" + str(self.date[iner_list[j]].tm_year), self.autor[iner_list[j]], self.tupe[iner_list[j]])

    def write_search_tupe(self, checker):
        check_list = []
        iner_list = []
        for i in range(len(self.tupe)):
            if self.tupe[i] == str(checker):
                check_list.append(self.tupe[i])
                iner_list.append(i)
        if len(check_list) == 0:
            print("\nGot nothing for your search\n")
        else:
            print("\nFind by type - ", str(checker), "\n")
            for j in range(len(iner_list)):
                print("№ {}".format(j + 1), self.book[iner_list[j]],
                      str(self.date[iner_list[j]].tm_mon) + "/" + str(self.date[iner_list[j]].tm_mday)
                      + "/" + str(self.date[iner_list[j]].tm_year), self.autor[iner_list[j]])

    def write_search_autor(self, checker):
        check_list = []
        iner_list = []
        for i in range(len(self.autor)):
            if self.autor[i] == str(checker):
                check_list.append(self.autor[i])
                iner_list.append(i)
        if len(check_list) == 0:
            print("\nGot nothing for your search\n")
        else:
            print("\nFind by author  - ", str(checker), "\n")
            for j in range(len(iner_list)):
                print("№ {}".format(j + 1), self.book[iner_list[j]],
                      str(self.date[iner_list[j]].tm_mon) + "/" + str(self.date[iner_list[j]].tm_mday)
                      + "/" + str(self.date[iner_list[j]].tm_year), self.tupe[iner_list[j]])

    def Writer(self):
        for i in range(len(self.book)):
            print(self.book[i], str(self.date[i].tm_mon) + "/" + str(self.date[i].tm_mday)
                  + "/" + str(self.date[i].tm_year), self.autor[i], self.tupe[i])

    def add(self, name, date, autor, tupe):

        if type(name) != str and type(date) != str and type(autor) != str and type(tupe) != str:
            print("\nWrong input\n")
        else:
            try:
                valid_date = time.strptime(date, '%m/%d/%Y')
                self.book.append(name)
                self.date.append(valid_date)
                self.autor.append(autor)
                self.tupe.append(tupe)
                print("\nYou successfully added a book to the lib\n")
            except ValueError:
                print('\nInvalid type of date\n')

    def sort_by_date(self):
        b = self.date
        print("\nSort by date\n")
        for i in range(len(b) - 1):
            for j in range(len(b) - i - 1):
                pass
                if int(b[j].tm_year) > int(b[j + 1].tm_year):
                    b[j], b[j + 1] = b[j + 1], b[j]
                else:
                    if int(b[j].tm_year) == int(b[j + 1].tm_year):
                        if int(b[j].tm_mday) > int(b[j + 1].tm_mday):
                            b[j], b[j + 1] = b[j + 1], b[j]
                        else:
                            if int(b[j].tm_mday) == int(b[j + 1].tm_mday):
                                if int(b[j].tm_mon) > int(b[j + 1].tm_mon):
                                    b[j], b[j + 1] = b[j + 1], b[j]
        for i in range(len(b)):
            for j in range(len(self.date)):
                if int(self.date[j].tm_year) == int(b[i].tm_year) and int(self.date[j].tm_mon) == int(b[i].tm_mon) \
                        and int(self.date[j].tm_mday) == int(b[i].tm_mday):
                    print("№ {}".format(i + 1), str(b[i].tm_mon) + "/" + str(b[i].tm_mday) + "/" + str(b[i].tm_year),
                          self.book[j], self.autor[j], self.tupe[j])


if __name__ == '__main__':
    ob = Biblio()
    print("Program will have some info before start")
    ob.add("Clause", "11/01/2019", "Spiner", "Fantastic")
    ob.add("Dark", "11/03/2019", "Django", "History")
    ob.add("Hope", "5/04/2019", "Django", "Fantastic")
    # ob.Writer()
    # ob.write_search_date("12/01/2019")
    # ob.write_search_book("Clause")
    # ob.write_search_tupe("Fantastic")
    # ob.write_search_autor("Spiner")
    # ob.sort_by_date()
    while True:
        print("\nWrite 1 - to add a book to library(Name, Date(xx/xx/xxxx), Author, Type)")
        print("Write 2 - to see all books in the library")
        print("Write 3 - to search by date(xx/xx/xxxx)")
        print("Write 4 - to search by book(Name)")
        print("Write 5 - to search by type of a book(Type)")
        print("Write 6 - to search by author(Author)")
        print("Write 7 - to sort all books by date")
        print("Write 8 - to create a diary")
        print("Write Stop to quit programm\n")
        x = input()
        if x == "1":
            name = input("Give name of a book\n")
            date = input("Give date of a book(xx/xx/xxxx)\n")
            aut = input("Give author of a book\n")
            tp = input("Give type of a book\n")
            ob.add(name, date, aut, tp)
        if x == "2":
            ob.Writer()
        if x == "Stop":
            quit()
        if x == "3":
            date = input("Give date(xx/xx/xxxx)\n")
            ob.write_search_date(date)
        if x == "4":
            book = input("Give name of a book\n")
            ob.write_search_book(book)
        if x == "5":
            tp = input("Give type of a book\n")
            ob.write_search_tupe(tp)
        if x == "6":
            aut = input("Give Author\n")
            ob.write_search_autor(aut)
        if x == "7":
            ob.sort_by_date()
        if x == "8":
            ob1 = Biblio.Diary()
            while True:
                print("Write 1 to add/upgrade a day")
                print("Write 2 to get best and medium of parameter")
                print("Write 3 to Call count of calories out and it")
                print("Write 4 to print a day")
                print("Write 5 to sort by parameter")
                print("Write back to back")
                print("Write Stop to quit program\n")
                y = input()
                if y == "1":
                    day = input("Give name of a day(Monday/Tuesday/Wednesday/Thursday/Friday/Saturday/Sunday\n")
                    ob1.upgrade_day(day)
                if y == "2":
                    par = input("Give parameter(Time/Squats/Push-ups/Pull-ups/Distance/Calories)\n")
                    ob1.best_med(par)
                if y == "3":
                    day = input("Give a day to call calories\n")
                    ob1.call_kall(day)
                if y == "4":
                    day = input("Give name of a day(Monday/Tuesday/Wednesday/Thursday/Friday/Saturday/Sunday\n")
                    ob1.write_all(day)
                if y == "5":
                    par = input("Give parameter for sort(Time/Squats/Push-ups/Pull-ups/Distance/Calories)\n")
                    ob1.sort_cal(par)
                if y == "Back":
                    break
                if y == "Stop":
                    quit()
