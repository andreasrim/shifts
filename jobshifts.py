from datetime import *


def calculate_shiftweek():
    start_week = datetime.today().isocalendar()[1]
    for i in range(20):
        shift_week = shift_week % 6
        print("UKEnr: " + str(start_week) + " Turnusuke: " + str(shift_week + 1) + ' ' + find_shifts_for_week(shift_week))
        start_week += 1


def find_shifts_for_week(shift_week):
    indent = '  '
    shifts_each_week = ['Lørdag: 09:00 - 14:30', 'Ingen vakter',
                        'Fredag: 14:00 - 19:00 \n ' + indent * 11 + 'Lørdag: 12:00 - 18:00', 'Lørdag: 15:00 - 22:15',
                        'Fredag: 16:00 - 23:15 \n ' + indent * 11 + 'Lørdag: 15:00 - 22:15', 'Ingen vakter']
    return shifts_each_week[shift_week]


calculate_shiftweek()
