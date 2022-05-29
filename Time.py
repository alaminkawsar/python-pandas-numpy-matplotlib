import time

#time() function return time in seconds from 1970 that is called epoch
seconds = time.time()
print("Seconds since epoch =", seconds)	


# seconds passed since epoch
#seconds = 1545925769.9618232
#ctime(parameter) return current time(week,month date,clock,year format)
local_time = time.ctime(seconds)
print("Local time:", local_time)

#The sleep() function suspends (delays) execution of the current thread for the given number of seconds.
print("This is printed immediately.")
#time.sleep(2.4)
print("This is printed after 2.4 seconds.")

#time.struct_time 
#time.struct_time(tm_year=2020, tm_mon=12, tm_mday=27, tm_hour=6, tm_min=35, tm_sec=17, tm_wday=3, tm_yday=361, tm_isdst=0)




#The localtime() function takes the number of seconds passed since epoch as an argument and returns struct_time in local time.
result = time.localtime(1645925769)
print("result:", result)
print("\nyear:", result.tm_year)
print("tm_hour:", result.tm_hour)

#The gmtime() function takes the number of seconds passed since epoch as an argument and returns struct_time in UTC.
result = time.gmtime(1645925769)
print("result:", result)
print("\nyear:", result.tm_year)
print("tm_hour:", result.tm_hour)







#inverse function as local time, that makes as second of 9 touple
t = (2018, 12, 28, 8, 44, 4, 4, 362, 0)

local_time = time.mktime(t)
print("Local time:", local_time)

seconds = 1545925769

# returns struct_time
t = time.localtime(seconds)
print("t1: ", t)

# returns seconds from struct_time
s = time.mktime(t)
print("\s:", seconds)







#convert 9 touple to standard time format

t = (2018, 12, 28, 8, 44, 4, 4, 362, 0)

result = time.asctime(t)
print("Result:", result)






#different format for local time
named_tuple = time.localtime() # get struct_time
time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)

print(time_string)



#The strptime() function parses a string representing time and returns struct_time.
time_string = "21 June, 2018"
result = time.strptime(time_string, "%d %B, %Y")

print(result)