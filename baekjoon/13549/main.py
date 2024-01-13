import sys
max_coor = 100000
subin, sister = map(int, sys.stdin.readline().split())
# subin, sister = 99999, 0
if sister <= subin:
    print(subin - sister)
    sys.exit()
visited_subin = set()
def teleport(subin_list):
    new_subin_list = set()
    for subin in subin_list:
        for i in range(17):
            new_subin_vol = subin * (2 ** i)
            if  new_subin_vol < sister*2:
                new_subin_list.add(new_subin_vol)
            else:
                break
    return new_subin_list

def walking(subin_list):
    return {subin + 1 for subin in subin_list if subin + 1 <= max_coor} | {subin - 1 for subin in subin_list if subin - 1 >= 0}

step = 0
subin_list = {subin}
while True:
    subin_list = teleport(subin_list)
    visited_subin |= subin_list
    if sister in subin_list:
        print(step)
        break
    step += 1
    subin_list = walking(subin_list)
    subin_list -= visited_subin