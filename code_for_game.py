studentNum = ["123","124"]
groups = [["123","126"],["122","126"],["125","126","125"]]

def are_valid_groups(groups, studentNum):

    length = len(studentNum)
    countID = 0   

    for students in studentNum:
        count = 0
        for group in groups:
            if (group.count(students) > 0):
                count += group.count(students)

        if (count == 1):
            countID += 1
        else:
            return False
    if (countID == length):
        return True

    return False

print(are_valid_groups(groups, studentNum))

