def conv_num(num_str):
    """Converts a provided string to either an int or a float if possible,
    else returns None"""

    valid_nums = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
                  "7": 7, "8": 8, "9": 9}
    valid_hex = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
                 "7": 7, "8": 8, "9": 9, "A": 10, "a": 10, "B": 11, "b": 11,
                 "C": 12, "c": 12, "D": 13, "d": 13, "E": 14, "e": 14,
                 "F": 15, "f": 15}

    decimal_count = 0
    hexadecimal = False
    negative = False
    ret = 0
    mult = 10

    # Hexadecimal found, change mult to 16 and remove leading 2 characters
    if len(num_str) >= 2 and (num_str[0:2] == "0x" or num_str[0:2] == "0X"):
        num_str = num_str[2:]
        hexadecimal = True
        mult = 16

    # Empty string. Placed after hex check to catch empty hex strings
    if len(num_str) == 0:
        return None

    for index in range(len(num_str)):
        if num_str[index] == ".":
            decimal_count += 1
            mult = 0.1

            if decimal_count == 2 or hexadecimal:
                return None

        elif num_str[index] == "-":
            negative = True

            if index != 0:
                return None

        else:
            if (num_str[index] in valid_nums or
                    (num_str[index] in valid_hex and hexadecimal)):
                num = (valid_nums[num_str[index]] if not hexadecimal else
                       valid_hex[num_str[index]])

                # Move current ret left
                if decimal_count == 0:
                    ret = ret*mult + num

                # Move provided num right
                else:
                    ret += num*mult
                    mult *= mult
            else:
                return None

    if negative:
        ret *= -1

    return ret
