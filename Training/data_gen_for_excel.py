import string
import xlsxwriter
import random


def random_word(length):
    return "".join(random.choice(string.lowercase) for i in range(length))


if __name__ == "__main__":
    workbook = xlsxwriter.Workbook('demo2.xlsx')
    worksheet = workbook.add_worksheet()
    
    for i in range(0, 10):
        worksheet.write(i, 0, random_word(5))
        worksheet.write(i, 1, random.randrange(1, 10))
    
    workbook.close()
        