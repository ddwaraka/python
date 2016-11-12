import xlsxwriter
lines = []
    
def generate_input_file():
    for line in lines:
        name, age = line.strip().split(",")
        age = int(age)
    
        if not age in age_and_names:
            age_and_names[age]=[]
    
        age_and_names[age].append(name)
    
    write_to_excel()
        

def write_to_excel():
    workbook = xlsxwriter.Workbook('demo.xlsx')
    worksheet = workbook.add_worksheet()
    
    worksheet.set_column('B:B', 12)
    
    worksheet.write(0, 0, "Age")
    worksheet.write(0, 1, "Names Count")
    worksheet.write(0, 2, "Names")
    
    
    row = 0
    col = 0
    
    for key in sorted(age_and_names):#.keys():
        row += 1   #Leaves a blank row after every entry is done 
        worksheet.write(row, col, key)
        worksheet.write(row, col+1, len(age_and_names[key]))
        worksheet.write(row, col+2, ",".join(age_and_names[key]))

    workbook.close()  

if __name__ == "__main__":
    with open ("input2.txt") as input_fd:
        lines = input_fd.readlines()
    
    age_and_names = {}
    generate_input_file()    


#For debugging only
#print age_and_names  
#for key in sorted(age_and_names): 
#print "Age: {}, Names Count: {}, Names: {}".format(key, len(age_and_names[key]), ",".join(age_and_names[key]))

