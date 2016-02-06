import datetime

def get_dt(hour, day):
    '''goes from hour and day of week to a datetime object'''
    daymap = {'MO':11,'TU':12,'WE':13,'TH':14,'FR':15,'SA':16,'SU':17}
    if hour == 24:
        hour = 23.9999 #can't do 24 hours
    return datetime.datetime(2016,1,daymap[day],int(hour),int(60*(hour-int(hour))))
