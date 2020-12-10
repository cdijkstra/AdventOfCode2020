import os, re

lines = [line.rstrip() for line in open('passports.txt')]

passports = []
tmp_passport = {}
for line in lines:
    if len(line) == 0 or line.isspace():
        passports.append(tmp_passport)
        tmp_passport = {}
    else:
        tmp_passport.update({entry.split(":")[0]:entry.split(":")[1] for entry in line.split(" ")})
passports.append(tmp_passport)

count = 0
required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
for passport in passports:
    if (
        all(reqs in passport for reqs in required) and
        1920 <= int(passport["byr"]) <= 2002 and
        2010 <= int(passport["iyr"]) <= 2020 and
        2020 <= int(passport["eyr"]) <= 2030 and
        ( 
            (passport["hgt"][-2:] == "cm" and 150 <= int(passport["hgt"][:-2]) <= 193) or
            (passport["hgt"][-2:] == "in" and 59 <= int(passport["hgt"][:-2]) <= 76)
        ) and
        re.match("#[\da-f]{6}", passport["hcl"]) and
        passport["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"] and
        len(passport["pid"]) == 9 and passport["pid"].isnumeric()
    ):
        count += 1
    
print("Count = " + str(count))