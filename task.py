def my_datetime(num_sec):
    """ Function finds the date by the seconds that have passed
     since 1-1-1970.
     """
    one_day = 86400
    month = 1
    year = 1970
    day = 1

    passed_days = num_sec // one_day
    if passed_days > 0:
        year_value = calculate_year(passed_days + 1, year)
        month_value = calculate_month(year_value[0], year_value[1], month)
        day = month_value[0]
        month = month_value[2]
        year = month_value[1]
    if day < 10:
        day = "0" + str(day)
    if month < 10:
        month = "0" + str(month)
    date = str(month) + "-" + str(day) + "-" + str(year)
    return date


def calculate_year(passed_days, year):
    """ Helper function finds the years that have passed and returns
    the found year and leftover days.
    """
    while passed_days > 366:
        if year % 4 != 0:
            passed_days = passed_days - 365
            year += 1
        else:
            if leap_year(year) is True:
                passed_days = passed_days - 366
                year += 1
            else:
                passed_days = passed_days - 365
                year += 1
    return passed_days, year


def calculate_month(passed_days, year, month):
    """ Helper function uses passed days to find the
    month and day of the date.
     """
    months_with_31_days = [1, 3, 5, 7, 8, 10, 12]
    months_with_30_days = [4, 6, 9, 11]
    february = [2]
    while passed_days > 31:
        if month in months_with_31_days:
            passed_days = passed_days - 31
            month += 1
        elif month in months_with_30_days:
            passed_days = passed_days - 30
            month += 1
        elif month in february:
            check_if_leap_year = leap_year(year)
            if check_if_leap_year is True:
                passed_days = passed_days - 29
                month += 1
            else:
                passed_days = passed_days - 28
                month += 1
    if passed_days >= 28 and month == 2:
        check_if_leap_year = leap_year(year)
        if check_if_leap_year is False:
            passed_days = passed_days - 28
            month += 1
        elif passed_days == 30:
            passed_days = passed_days - 29
            month += 1
    if month == 13:
        month = 1
        year += 1
    return passed_days, year, month


def leap_year(year):
    """ Helper function calculates if the year was a leap year"""
    if year % 4 == 0:
        if year % 100 != 0:
            return True
        if year % 100 == 0 and year % 400 == 0:
            return True
    else:
        return False


def conv_endian(num, endian='big'):
  """Function to convert decimal number to hexadecimal(little/big endian)"""
  num = str(num)
  is_negative = False
  hex_num = []
  pocket = ""
  result = []
  str_result = ""
  
  if num[0] == '-':
    is_negative = True
    num = num[1:]

  num = int(num)
  bin_num = num_to_bin(num)
  hex_num = bin_to_hex(bin_num)

  if(len(hex_num)%2) != 0:
    hex_num.append('0')

  hex_num.reverse()
  
  for i in hex_num:
    if len(pocket) < 2:
      pocket = pocket+i

    if len(pocket) == 2:
      result.append(pocket)
      pocket = ''
      
  if endian == 'big':
    for i in result:
      str_result = str_result+ i + " "

  elif endian == "little":
    result.reverse()
    for i in result:
      str_result = str_result+ i + " "

  else:
    return None

  if is_negative == True:
    str_result = '-'+str_result
    
  return str_result



def num_to_bin(num):
  """Helper Function to convert decimal to binary"""
  binn = []
  while(num > 0):
    pocket = num%2
    binn.append(pocket)
    num = num//2
  binn.reverse()
  return binn


def bin_to_hex(bin):
  """Helper Function to convert binary to hexadecimal"""
  stri = ''.join(str(e) for e in bin)
  position = []
  hex = []

  while len(stri) != 0:
    if len(stri) >= 4:
      position.append(stri[-4:])
      stri = stri[:-4]

    if len(stri) < 4 and len(stri) > 0:
      while len(stri) != 4:
        stri = "0"+stri

  for i in position:
    pocket = 0
    if i[0] == '1':
      pocket = pocket+8

    if i[1] == '1':
      pocket = pocket+4

    if i[2] == '1':
      pocket = pocket+2

    if i[3] == '1':
      pocket = pocket+1

    pocket = str(pocket)
    
    if pocket == '10':
      pocket = 'A'

    if pocket == '11':
      pocket = 'B'

    if pocket == '12':
      pocket = 'C'

    if pocket == '13':
      pocket = 'D'

    if pocket == '14':
      pocket = 'E'

    if pocket == '15':
      pocket = 'F'
      
    hex.append(pocket)
      
  return hex