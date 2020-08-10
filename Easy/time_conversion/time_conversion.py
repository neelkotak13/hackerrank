#/usr/bin/env python3
'''
input: a single string s containing a time in 12-hour clock format
(i.e.: hh:mm:ssAM or hh:mm:ssPM)

output: convert and print the given time in 24 hr format

solution:
    1. split the input string into hh, mm, ss, and AM/PM
    2. if input is AM, return same output, but remove the PM, if value is 12,
       replace with 00
    3. if input is PM, add 12 to hh and return the modified hh w/same mm and ss
       but remove the PM, do not add 12, if value is not 12
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
        # need to change 12 to 00
        if s[0] == '12':
            s[0] = '00'
        return ':'.join(s[:len(s)-1])
    # if PM, add 12 to hh and then return value omitting PM
    else:
        # need to leave 12 the same
        if s[0] == '12':
            return ':'.join(s[:len(s)-1]) 
        new_val = int(s[0]) + 12
        s[0] = str(new_val)
        return ':'.join(s[:len(s)-1]) 

if __name__ == '__main__':
    s = input()
    result = time_conversion(s)
    print(result)
