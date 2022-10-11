def revers_row(num, row, new_row):
    if num < 1:
        return new_row
    else:
        if num == 1:
            new_row = row[0] + new_row
            num -= 1
            return revers_row(num, row, new_row)
        else:
            new_row = row[1] + row[0] + new_row
            row = row[2:]
            num -= 1
            return revers_row(num, row, new_row)
