points = 174  # use this input to make your submission


# write your if statement here
if points < 50:
    prize = "wooden rabbit"
    result_str = "Congratulations! You won a {}!".format(prize)
elif points < 150:
    prize = "no prize"
    result_str = "Oh dear, {} this time.".format(prize)
elif points < 180:
    prize = "wafer-thin mint"
    result_str = "Congratulations! You won a {}!".format(prize)
else:
    prize = "penguin"
    result_str = "Congratulations! You won a {}!".format(prize)
    
    
result = result_str # replace None with appropriate code
