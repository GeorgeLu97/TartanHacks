import icalendar
import overlap

from schedule_object import Schedule, Event

def FileStringToICal(SCF,OwnerArray):
    #How do you get days of week
    cals = []
    for i in SCF:
        cals.append(Schedule(i,OwnerArray[i]))
    sh1 = overlap.overlapping_wrapper(cals)
    cal = icalendar.Calendar()
    for i in sh1.events():
        event = icalendar.event()
        event.add('summary',i.summary)
        event.add('dtstart',i.get_start_dt())
        event.add('dtend',i.get_end_dt())
        event.add('location',i.location)
        event.add('rrule',"FREQ=WEEKLY;")
        cal.add_component(event)
    x = open(OwnerArray.join() + '.ics','wb')
    x.write(cal.as_string())
    x.close()
    return (OwnerArray.join() + '.ics')

def GroupIcal(SCF, OwnerArray):
    #Literally least efficient way
    cals = []
    for x in range (0, len(SCF)):
        SCF[0],SCF[x] = SCF[x],SCF[0]
        OwnerArray[0], OwnerArray[x] = OwnerArray[x], OwnerArray[0]
        cals.append(FileStringToICal(SCF,OwnerArray))
    return cals