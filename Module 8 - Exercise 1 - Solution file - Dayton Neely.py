# Module 8 - Exercise 1 - Solution file
# Dayton Neely - SDEV120

HIGH_VALUE = 99999

def read_record(file):
    line = file.readline()
    if line == "":                      # eof
        return [HIGH_VALUE, "", "", ""]
    fields = line.strip().split(",")
    return [int(fields[0]), fields[1].strip(), fields[2], fields[3]]

# housekeeping
geraldine_file = open("Geraldines Businesses.csv")
gerard_file = open("Geralds Businesses.csv")
merged_file = open("Merged Customers.csv", "w")
geraldine = read_record(geraldine_file)
gerard = read_record(gerard_file)

# mergeRecords loop
while not (geraldine[0] == HIGH_VALUE and gerard[0] == HIGH_VALUE):
    if geraldine[0] <= gerard[0]:
        record = geraldine
        geraldine = read_record(geraldine_file)
    else:
        record = gerard
        gerard = read_record(gerard_file)
    line = f"{record[0]},{record[1]},{record[2]},{record[3]}"
    merged_file.write(line + "\n")
    print(line)

# finishUp
geraldine_file.close()
gerard_file.close()
merged_file.close()
