def add_time(startTime, duration, startingDay=''):
    start_hr = int(startTime.split(':')[0])
    start_min = int(startTime.split(':')[1].split(' ')[0])
    am_pm = startTime.split(':')[1].split(' ')[1]
    #print(start_hr, start_min, am_pm)

    duration_hr = int(duration.split(':')[0])
    duration_min = int(duration.split(':')[1])
    #print('\n', duration_hr, duration_min)

    hours = start_hr+duration_hr
    minutes = start_min + duration_min
    hour = 0
    mins = 0
    if (minutes >= 60):
        hour += int(minutes/60)
        mins += minutes%60
    else:
        mins += minutes

    if(hours > 12):
        hour += hours%12
    else:
        hour += hours


    # AM PM
    days = int(hours/24)
    periods = int(hours/12)
    Rhours = hours%12
    a_p = ''
    if Rhours == 0:
        Rhours=12
    if (periods % 2 == 1) or (periods%2==0 and mins > 0):
        print(periods, mins)
        if am_pm == 'AM':
            a_p = 'PM'
        else:
            a_p = 'AM'
            days += 1

    startingDay = startingDay.lower()
    week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    if startingDay != '':
        pass

    # return statements
    if (hours <= 12) or (hours < 24 and am_pm == 'AM'):
        print(f"{hour}:{mins:02d} {a_p}")
    else:
        print("else:",hours, a_p)
    #print(f"{hour}:{mins:02d} {am_pm}, ({days} days later)")
    
    
    #if (days_passed > 1):
    #    print(f"{hour}:{mins:02d} {am_pm}, ({days_passed} days later)")

'''
add_time('10:10 PM', '3:30')
add_time('11:43 PM', '24:20', 'tueSday')
add_time('6:30 PM', '205:12')
add_time('2:59 AM', '24:00')
add_time('8:16 PM', '466:02')
add_time('2:59 AM', '24:00', 'saturDay')
add_time('11:59 PM', '24:05', 'Wednesday')
add_time('8:16 PM', '466:02', 'tuesday')

add_time('11:30 AM', '2:32', 'Monday')
add_time('11:43 AM', '00:20')
add_time('11:55 AM', '3:12')

add_time('3:00 PM', '3:10') # 0 days later
add_time('3:30 PM', '2:12') # 0 days later
'''
add_time('3:30 PM', '2:12', 'Monday') # 0 days later
