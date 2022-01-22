studentNum = [123,124]
groups = [[12,13],[123,124],[123,123,124]]

def are_valid_groups(groups, studentNum):

    length = len(studentNum)
    count = 0
    countID = 0
    
    for group in groups:
        count = 0
        countID = 0
        for students in studentNum:
            if (group.count(students) == 0):
                break
            if (group.count(students) >= 1):
                count += group.count(students)
                countID += 1
        
        if (count >= length) and (countID == length):
            return True
        
    return False

print(are_valid_groups(groups, studentNum))