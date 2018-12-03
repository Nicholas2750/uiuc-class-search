import csv
import sys

with open('./uiuc-gpa-dataset.csv') as grades:
    csv_reader = csv.reader(grades)
    grades_data = list(csv_reader)
    grades_data.pop(0)

def data_filter(grades_data, column):
    selection = []

    for datas in grades_data:
        if datas[column] not in selection:
            selection = [datas[column]] + selection

    selection.sort()

    for choice in selection:
        print('-' + choice)


    selected = input('\nYour choice: ')
    print('\n')
    if selected == '':
        return grades_data

    new_grades_data = []
    for datas in grades_data:
        if datas[column].lower() == selected.lower():
            new_grades_data.append(datas)

    if len(new_grades_data) == 0:
        print('\nThere is no course that fits your selection.')
        sys.exit()

    return new_grades_data



print('Year of the course you are looking for (leave blank if you do no want to filter by year):')
grades_data = data_filter(grades_data, 0)

print('Term of the course you are looking for (leave blank if you do no want to filter by term):')
grades_data = data_filter(grades_data, 1)

print('Subject of the course you are looking for (leave blank if you do no want to filter by subject):')
grades_data = data_filter(grades_data, 3)

print('Number of the course you are looking for (leave blank if you do no want to filter by number):')
grades_data = data_filter(grades_data, 4)

grades_data.sort()

for datas in grades_data:
    total_student = 0
    gpa_sum = 0

    gpa_sum += 4.00 * int(datas[6])
    gpa_sum += 4.00 * int(datas[7])
    gpa_sum += 3.67 * int(datas[8])
    gpa_sum += 3.33 * int(datas[9])    
    gpa_sum += 3.00 * int(datas[10])
    gpa_sum += 2.67 * int(datas[11])
    gpa_sum += 2.33 * int(datas[12])
    gpa_sum += 2.00 * int(datas[13])
    gpa_sum += 1.67 * int(datas[14])
    gpa_sum += 1.33 * int(datas[15])
    gpa_sum += 1.00 * int(datas[16])
    gpa_sum += 0.67 * int(datas[17])

    for i in range(6, 20):
        total_student += int(datas[i])

    print(datas[3] + ' ' + datas[4] + ' (' + datas[5] + ', ' + datas[1] + ' ' + datas[0] + ')' + ' with ' + datas[20] + ':')
    print('Average GPA: ' + str(gpa_sum / (total_student - int(datas[19])))[0:4])
    print('Out of ' + str(total_student) + ' students:')
    print('-' + datas[6] + ' earned A+')
    print('-' + datas[7] + ' earned A')
    print('-' + datas[8] + ' earned A-')
    print('-' + datas[9] + ' earned B+')
    print('-' + datas[10] + ' earned B')
    print('-' + datas[11] + ' earned B-')
    print('-' + datas[12] + ' earned C+')
    print('-' + datas[13] + ' earned C')
    print('-' + datas[14] + ' earned C-')
    print('-' + datas[15] + ' earned D+')
    print('-' + datas[16] + ' earned D')
    print('-' + datas[17] + ' earned D-')
    print('-' + datas[18] + ' earned F')
    print('-' + datas[19] + ' earned W\n')