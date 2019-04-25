from datetime import *


def kalkuler_turnusuke():
    start_uke = datetime.today().isocalendar()[1]
    for i in range(20):
        turnus_uke = start_uke % 6
        print("UKEnr: " + str(start_uke) + " Turnusuke: " + str(turnus_uke + 1) + ' ' + finn_vakter_turnusuke(turnus_uke))
        start_uke += 1


def finn_vakter_turnusuke(turnusuke):
    indent = '  '
    vakter_turnusuke = ['Lørdag: 09:00 - 14:30', 'Ingen vakter',
                        'Fredag: 14:00 - 19:00 \n ' + indent * 11 + 'Lørdag: 12:00 - 18:00', 'Lørdag: 15:00 - 22:15',
                        'Fredag: 16:00 - 23:15 \n ' + indent * 11 + 'Lørdag: 15:00 - 22:15', 'Ingen vakter']
    return vakter_turnusuke[turnusuke]


kalkuler_turnusuke()
