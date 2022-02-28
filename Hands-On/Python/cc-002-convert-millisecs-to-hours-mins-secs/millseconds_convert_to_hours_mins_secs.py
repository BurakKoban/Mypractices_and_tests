def convert(milliseconds):
     hour_in_milliseconds = 60*60*1000
    # calculate the hours within given milliseconds
    hours = milliseconds // hour_in_milliseconds
    # calculate milliseconds left over when hours subtracted
    milliseconds_left = milliseconds % hour_in_milliseconds
    # one minute in milliseconds
    minutes_in_milliseconds = 60*1000
    # calculate the minutes within remainder milliseconds
    minutes = milliseconds_left // minutes_in_milliseconds
    # calculate milliseconds left over when minutes subtracted
    milliseconds_left %= minutes_in_milliseconds
    # calculate the seconds within remainder milliseconds
    seconds = milliseconds_left // 1000
    # format the output string
    return f'{hours} hour/s'*(hours != 0) + f' {minutes} minute/s'*(minutes != 0) + f' {seconds} second/s' *(seconds != 0) or f'just {milliseconds} millisecond/s' * (milliseconds < 1000)
# flag to show warning to the user, default is False.



is_invalid = False

while True:
    info = """

        ###  This program converts milliseconds into hours, minutes, and seconds ###
        (To exit the program, please type "exit")
        Please enter the milliseconds (should be greater than zero) :"""
    milli_time = input('\nNot Valid Input !!!\n'*is_invalid + info).strip()

    if not milli_time.isdecimal():

        if milli_time.lower == 'exit':

            print('\nExiting the program... Good Bye')
            break
        else:
            is_invalid = True
            continue
    
    number = int(milli_time)

    if 1< number:
        print(
            f'\n "{milli_time}"" is equal to {convert(number)}')

        is_invalid = False
    else:
        is_invalid = True

