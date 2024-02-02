nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum = 0

for num in range(1, 6):
    print("Sayı: " + str(num))
for num in nums:
    sum += num
    if sum > 25:
        break
if sum > 54:
    print("Kesilme yok")
    print("Break kullanılmamış")
else:
    print("Kesildi")
    print("Break devreye girmiş")
print(sum)
num = 0
while num < 6:
    print("While Sayı: " + str(num))
    num = num + 1
for num in nums:
    sum += num


def mpg(km, litre):
    try:
        kml = km / litre
    except ZeroDivisionError:
        kml = None
    return kml


print(mpg(50, 10))
