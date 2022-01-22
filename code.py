studentNum = [123,124,125]
groups = [[12,13],[124,123,125],[234,543,123],[124,125,127]]

def are_valid_groups(groups, studentNum):

    length = len(studentNum)
    count = 0
    
    for group in groups:
        count = 0
        for students in studentNum:
            if (group.count(students) == 0):
                break
            if (group.count(students) == 1):
                count += 1
        
        if count == length:
            return True
        
    return False

print(are_valid_groups(groups, studentNum))