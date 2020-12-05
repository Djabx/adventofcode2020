import shared
import re

RE_YEAR = re.compile(r"\d{4}")


def valid_byr(v):
    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    if v and RE_YEAR.match(v):
        vi = int(v)
        return 1920 <= vi and vi <= 2002
    return False


def valid_iyr(v):
    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    if v and RE_YEAR.match(v):
        vi = int(v)
        return 2010 <= vi and vi <= 2020
    return False


def valid_eyr(v):
    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    if v and RE_YEAR.match(v):
        vi = int(v)
        return 2020 <= vi and vi <= 2030
    return False


def valid_hgt(v):
    # hgt (Height) - a number followed by either cm or in:
    # If cm, the number must be at least 150 and at most 193.
    # If in, the number must be at least 59 and at most 76.
    if v:
        m = re.match(r"(?P<size>\d{2,3})(?P<unit>in|cm)", v)
        if m:
            size = int(m.group("size"))
            min, max = (150, 193) if m.group("unit") == "cm" else (59, 76)
            return min <= size and size <= max
    return False


def valid_hcl(v):
    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    return v and re.match(r"#[a-f0-9]{6}", v)


def valid_ecl(v):
    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    return v and re.match(r"(amb|blu|brn|gry|grn|hzl|oth)", v)


def valid_pid(v):
    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    return v and re.match(r"\d{9}", v)


def valid_cid(v):
    # cid (Country ID) - ignored, missing or not.
    return True


FIELDS = {
    "byr": (True, valid_byr),  # "Birth Year"
    "iyr": (True, valid_iyr),  # "Issue Year"
    "eyr": (True, valid_eyr),  # "Expiration Year"
    "hgt": (True, valid_hgt),  # "Height"
    "hcl": (True, valid_hcl),  # "Hair Color"
    "ecl": (True, valid_ecl),  # "Eye Color"
    "pid": (True, valid_pid),  # "Passport ID"
    "cid": (False, valid_cid),  # "Country ID"
}

passport = []
current_passport = []
for l in shared.get_data(num_day=4):
    if len(l) == 0:
        if len(current_passport):
            passport.append(" ".join(current_passport))
            current_passport = []
    else:
        current_passport.append(l)
passport.append(" ".join(current_passport))

valid = 0
invalid = 0
uncorrect = 0
optional = 0
for i, pstr in enumerate(passport):
    fields = pstr.split(" ")
    fields_present = {k: False for k in FIELDS}
    fields_present_or_optional = {k: False for k in FIELDS}
    fields_valid = {k: False for k in FIELDS}
    p = {}
    for f in fields:
        k, v = f.split(":")
        p[k] = v
        fields_present[k] = True
        fields_present_or_optional[k] = True

    for k, (required, validator) in FIELDS.items():
        val = validator(p.get(k, None))
        fields_valid[k] = val
        if not val:
            print(f"Not Valid {k} {p.get(k)}")
        if not required:
            fields_present_or_optional[k] = True

    if all(fields_valid.values()):
        if all(fields_present.values()):
            valid += 1
        elif all(fields_present_or_optional.values()):
            optional += 1
        else:
            invalid += 1
    else:
        uncorrect += 1

print("#" * 5)
print(
    f"Found: valid {valid} ({valid+optional}) invalid {invalid} ({invalid+optional}) uncorrect {uncorrect} ({uncorrect+invalid}) optional {optional} passports"
)
