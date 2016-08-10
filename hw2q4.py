#This program reads number of days, hours, minutes worked of two users , and prints the total time both of them worked together as days, hours, minutes.

jdays=int(input('Please enter the number of days John has worked: '))
jhours=int(input('Please enter the number of hours John has worked: '))
jmins=int(input('Please enter the number of minutes John has worked: '))
bdays=int(input('Please enter the number of days Bill has worked: '))
bhours=int(input('Please enter the number of hours Bill has worked: '))
bmins=int(input('Please enter the number of minutes Bill has worked: '))

sec_in_day= 60 * 60 * 24

sec_in_hour= 60 * 60

sec_in_min= 60


j_sec_in_day= jdays * sec_in_day

j_sec_in_hour= jhours * sec_in_hour

j_sec_in_min= jmins * sec_in_min


jwork_in_sec= j_sec_in_day + j_sec_in_hour + j_sec_in_min


b_sec_in_day= bdays * sec_in_day

b_sec_in_hour= bhours * sec_in_hour

b_sec_in_min= bmins * sec_in_min


bwork_in_sec= b_sec_in_day + b_sec_in_hour + b_sec_in_min


total_sec= jwork_in_sec + bwork_in_sec


total_min= total_sec // sec_in_min
rem_sec= total_sec % sec_in_min

total_hours= total_min // 60
rem_min= total_min % 60

total_days= total_hours // 24
rem_hours= total_hours % 24


print('The total time both of them worked together is:',total_days,'days,', rem_hours,'hours and', rem_min, 'minutes')






