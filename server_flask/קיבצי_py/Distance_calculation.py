know_distans0 = 131
know_height0 = 82
know_distans2 =271
know_height2 = 89
know_distans4 = 187
know_height4 = 94
know_distans1 = 163
know_height1 = 78
know_distans6= 151
know_height6 = 240 
know_distans3 = 120
know_height3 = 177

focal_langth_class0= 776.4146341463414
focal_langth_class4= 841.5

def focal_length_finder(known_dis, know_height, height_we_found):
    focal_length = (height_we_found* known_dis)/ know_height
    return focal_length
def distans_finder(focal_length, know_height, height_we_found):
    distance = (know_height * focal_length)/ height_we_found
    return distance