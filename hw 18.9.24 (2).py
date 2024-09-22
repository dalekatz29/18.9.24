# START

world_record = 6.23
good_tries = 0
good_try_sum = 0
best_try = 0
new_record_holder = None

for i in range(7):
    jump_result: float = float(input('Enter the jump result: '))
    if jump_result < 5.80:
        continue
    else:
        good_tries += 1
        good_try_sum += jump_result
        if jump_result > best_try:
            best_try = jump_result
        if jump_result > world_record:
            world_record = jump_result
            new_record_holder = input("Enter the name of the new world record holder: ")

jump_avg = good_try_sum / good_tries

print(f"{good_tries} good tries and there average is {jump_avg:.2f}, the best result is {best_try},")
if new_record_holder == None:
    print(None)
else:
    print(f"The the world record holder is {new_record_holder} with result of {world_record}")














# END