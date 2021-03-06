import sys


def cal_2720():
    tot_num = int(sys.stdin.readline())
    for idx in range(tot_num):
        each_num = int(sys.stdin.readline())
        quarter_num = 0
        dime_num = 0
        nickel_num = 0
        penny_num = 0
        quarter_num = each_num // 25
        each_num = each_num - (quarter_num * 25)
        dime_num = each_num // 10
        each_num = each_num - (dime_num * 10)
        nickel_num = each_num // 5
        penny_num = each_num - (nickel_num * 5)
        sys.stdout.write(f"{quarter_num} {dime_num} {nickel_num} {penny_num}\n")


def cal_16435():
    tot_arr = list(map(int, sys.stdin.readline().split()))
    case_arr = list(map(int, sys.stdin.readline().split()))
    case_arr.sort()
    first_num = tot_arr[1]
    for num in case_arr:
        if first_num >= num:
            first_num += 1
    sys.stdout.write(f"{first_num}")


if __name__ == "__main__":
    # cal_2720()
    cal_16435()
