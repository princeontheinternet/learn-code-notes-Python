day = "friday"
temperature = 30
raining = False

#    (  F             and     T )            or  T              =   F or T = T
if (day == "saturday" and temperature >= 27) or not raining:
    print("Go for swimming")
else:
    print("Don't go")

# *** Note ***
# 1. "and" logical operator has more precedence than "or" logical operator.
# 2. Always use parenthesis when you mix "and" & "or" logical operator.

#   Output:

# Go for swimming
