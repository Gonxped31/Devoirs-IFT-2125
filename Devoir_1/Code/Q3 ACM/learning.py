import math
import time
start_timeFinal = time.time()


"""class Number:
    def __init__(self, value):
        self._value = value
        self._checked = True
        pass

    def set_checked(self, newChecked):
        self._checked = newChecked

    def get_checked(self):
        return self._checked

    def get_value(self):
        return self._value
"""


def supBornForTheLimit(m):
    return m*math.log(((m)*(math.log(m))))


m = 1000000
limit = supBornForTheLimit(m)
print(f"limit : {limit}")
AllNumber = []
primeNumber = []
start_time = time.time()
for i in range(0, int(limit+1)):
    AllNumber.append((1, i))

print("Initialisation tab")
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
for i in range(2, int((limit)**(1/2) + 1)):
    if AllNumber[i][0] == 1:
        for j in range(i**2, int(limit+1)):
            if (AllNumber[j][1] % AllNumber[i][1] == 0):
                AllNumber[j] = ((0, AllNumber[j][0]))
print("--- %s seconds --- 1er boucle" % (time.time() - start_time))


start_time = time.time()
for i in range(2, int(limit)):
    if AllNumber[i][0]:
        # print(AllNumber[i][1])
        primeNumber.append(AllNumber[i][1])
print("--- %s seconds --- 2er boucle" % (time.time() - start_time))


print(f" the {m} th prime number is {
      primeNumber[m-1]}")

print("--- %s seconds --- END :" % (time.time() - start_timeFinal))


print(bool(1))
