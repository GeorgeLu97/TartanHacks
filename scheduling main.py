import icalendar
import overlap

from schedule_object import Schedule, Event

def FileStringToICal(SCF,OwnerArray):
    cals = []
    for i in SCF:
        cals.append(Schedule(i,OwnerArray[i]))
    sh1 = overlap.overlapping_wrapper(cals)
    cal = icalendar.Calendar()
    for i in sh1.events():
        event = icalendar.event()
        event.add('summary',i.summary)
        event.add('dtstart',i.startt)
        event.add('dtend',i.endt)
        event.add('location',i.location)
        event.add('rrule',"FREQ=WEEKLY;")
        cal.add_component(event)
    x = open(OwnerArray.join(),'wb')
    x.write(cal.as_string())
    x.close