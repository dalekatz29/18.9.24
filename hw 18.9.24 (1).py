# START

negative_num_count = 0
odd_num = 0
positive_num_count = 0
even_num = 0
num_dividing_by7 = 0

for i in range(10):
    num = int(input("Enter a number between -1000 to 1000 (to finish the program enter -9999 and to exit the loop -999):"))
    if num == -999:
        break
    if num < -1000 or num > 1000:
        continue
    if num > 0:
        positive_num_count += 1
    else:
        negative_num_count += 1
    if num % 7 == 0:
        num_dividing_by7 += 1
    if num % 2 == 0:
        even_num = num
        odd_num = None
    else:
        even_num = None
        odd_num = num

if num != -999:
    print(
        f"The las odd number: {odd_num}, the last even number: {even_num}, positive numbers count: {positive_num_count}, negative numbers count: {negative_num_count}, number that dividing by 7: {num_dividing_by7}")

# END
