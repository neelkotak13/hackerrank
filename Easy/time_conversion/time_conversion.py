#/usr/bin/env python3
'''
input: a single string s containing a time in 12-hour clock format
(i.e.: hh:mm:ssAM or hh:mm:ssPM)

output: convert and print the given time in 24 hr format

solution:
    1. split the input string into hh, mm, ss, and AM/PM
    2. if input is AM, return same output, but remove the PM
    3. if input is PM, add 12 to hh and return the modified hh w/same mm and ss
       but remove the PM
'''
def time_conversion(s):
    # add colon in front of AM/PM to use as delimeter
    s = s[:8] + ":" + s[8:]
    # split input using the colon as a delimeter
    s = s.split(':')
    # get AM/PM meridian value with ss value
    meridian = s[len(s)-1]
    # if AM, no change, return same value, except omit AM
    if meridian == 'AM':
        return ':'.join(s[:len(s)-1])
    # if PM, add 12 to hh and then return value omitting PM
    else:
        new_val = int(s[0]) + 12
        s[0] = str(new_val)
        return ':'.join(s[:len(s)-1]) 

if __name__ == '__main__':
    s = input()
    result = time_conversion(s)
    print(result)
