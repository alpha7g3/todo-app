feet_inches = input("Enter feet and inches:")


def parse(feetinches):
    pat = feet_inches.split(" ")
    feet = float(pat[0])
    inches = float(pat[1])
    return(feet,inches)


def convert(feet,inches):
     meter = feet * 0.3048 * inches * 0.0254
     return meter
f, i = parse(feet_inches)
print("fi", f, i)
part = convert(f, i)

if part < 1 :
    print('your kid is not old enough')
else:
    print('your kid can enjoy the slide')
