def is_leap(year):
    if year % 4 == 0:  # Leap years are divisible by 4
        if year % 100 == 0:  # Unless they are divisible by 100
            if year % 400 == 0:  # Except when they are divisible by 400
                return True
            else:
                return False
        else:
            return True
    else:
        return False

if __name__ == '__main__':
    year = int(input().strip())
    print(is_leap(year))
