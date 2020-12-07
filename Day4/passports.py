import os, re

with open("passports.txt", 'r') as file:
    lines = file.readlines()

passports = []
tmp_passport = ""
for line in lines:
    tmp_passport += line
    if line == '\n':
        passports.append(tmp_passport)
        tmp_passport = ""
passports.append(tmp_passport)

count = 0
required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
for passport in passports:
    print("Start" + str1 + " End")
    # if all(reqs in passport for reqs in required):
    #     count += 1
    
print(count)