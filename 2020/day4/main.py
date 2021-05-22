import re

with open('input.file', 'r') as f:
  x = f.readlines()

accpEyes = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
req = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
opt = ['cid']

'''
byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
If cm, the number must be at least 150 and at most 193.
If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
cid (Country ID) - ignored, missing or not.
'''

def checkPassport(passport):
  reqCount = 0
  for field in passport:
    field = field.split(":")
    name,value = field[0], field[1]
    if name in req:
      # following mess is part 2
      if name == 'byr' and int(value) >= 1920 and int(value) <= 2002:
        reqCount += 1
      elif name == 'iyr' and int(value) >= 2010 and int(value) <= 2020:
        reqCount += 1
      elif name == 'eyr' and int(value) >= 2002 and int(value) <= 2030:
        reqCount += 1
      elif name == 'hgt':
        if value[-2:] == 'in':
          if int(value[:-2]) >= 59 and int(value[:-2]) <= 76:
            reqCount += 1
        elif value[-2:] == 'cm':
          if int(value[:-2]) >= 150 and int(value[:-2]) <= 193:
            reqCount += 1
      elif name == 'hcl' and value[0] == '#' and len(value[1:]) == 6:
        check = re.compile('[0-9a-f]+') # FUCK, regex
        if check.fullmatch(value[1:]):
          reqCount += 1
      elif name == 'ecl':
        if value in accpEyes:
          reqCount += 1
      elif name == 'pid' and len(value) == 9:
        try:
          int(value)
          reqCount += 1
        except:
          continue
    # reqCount += 1 #part 1
  if reqCount == 7:   # 7 required fields, 1 optional one
    return True
  return False

# fuck regex
def parsePassports(x):
  passports = []
  passport = []
  # print(x)
  for i in range(len(x)+1):
    if i >= len(x):   # sad
      passport = [val for sublist in passport for val in sublist]
      passports.append(passport)
      return passports
    if x[i] == '\n':
      passport = [val for sublist in passport for val in sublist]
      passports.append(passport)
      passport = []
    else:
      passport.append(x[i].strip().split())

validCount = 0
passports = parsePassports(x)  # get list of passports
for passport in passports:
  check = checkPassport(passport)   # get each passport in list
  if check:
    validCount += 1   # if valid + 1 you know what TF is up

print(validCount)