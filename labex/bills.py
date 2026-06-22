bill_thickness = 0.11 #in mm
tower_height = 442 * 1000 # in mm

bill_tower_height = bill_thickness # height of bill tower
day = 1

while(bill_tower_height <= tower_height):
    print(day, bill_tower_height, tower_height)
    bill_tower_height *= 2
    day += 1
