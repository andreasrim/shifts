from datetime import *


def calculate_shiftweek():
    curr_week = datetime.today().isocalendar()[1]
    for i in range(40):
        shift_week = (curr_week - 2) % 6
        print("UKEnr: " + str(curr_week) + " Turnusuke: " + str(shift_week + 1) + ' ' + find_shifts_for_week(shift_week))
        curr_week += 1


def find_shifts_for_week(shift_week):
    indent = '  '
    shifts_each_week = ['Lørdag: 11:00 - 17:00', 'Ingen vakter',
                        'Fredag: 14:00 - 19:00 \n ' + indent * 11 + 'Lørdag: 12:00 - 18:00', 'Lørdag: 15:00 - 21:00',
                        'Fredag: 16:00 - 22:00 \n ' + indent * 11 + 'Lørdag: 15:00 - 22:15', 'Ingen vakter']
    return shifts_each_week[shift_week]


calculate_shiftweek()
