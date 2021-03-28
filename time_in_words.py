import time

# Hours and Quarters in a List
Hours = [0, 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine',
         'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen',
         'Seventeen', 'Eighteen', 'Nineteen', 'Twenty']

Quarters = ["%s O' Clock", "Quarter Past %s", "Half Past %s", "Quarter to %s"]


# Function to convert Numerical Time into Word Time
def timeInWord():
    for i in range(1, 10):
        Hours.append('Twenty %s' % Hours[i])

    h = int(input("[Note: Hours in 12 Hours format in 1 - 12]"
                  "\nPlease Enter Hour: "))

    m = int(input("[Note: Minutes in 0 - 59]"
                  "\nPlease Enter Minute: "))
    print()

    start = time.time()

    hour = Hours[h] if (m < 31) else Hours[h+1]

    if not m % 15:
        print(Quarters[m//15] % hour)
        print("The time taken to work it out was", time.time() - start,
              "seconds.")
    elif m < 30:
        print("%s Minute" % Hours[m]+"s"*(m == 1) + " Past %s" % hour)
        print("The time taken to work it out was", time.time() - start,
              "seconds.")
    else:
        print("%s Minute" % Hours[60-m]+"s"*(m == 59) + " to %s" % hour)
        print("The time taken to work it out was", time.time() - start,
              "seconds.")


if __name__ == '__main__':
    timeInWord()
