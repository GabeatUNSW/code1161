def super_asker(low, high):
    message = "Give me a number between {low}, and {high}: ".format(low=low, high=high)
  
    while True:
        try: 
            input_number = int(input(message))
            if low < input_number < high:
                print ("{} looks good.".format(input_number))
                return input_number
        except Exception as e:
            print ("try again ({})".format(e))
        else:
            print ("{input} isn't between {low}, {high}".format(input=input_number, low=low, high=high))
    
    
    



if __name__ == "__main__":
    # this section does a quick test on your results and prints them nicely.
    # It's NOT the official tests, they are in tests.py as usual.
    # Add to these tests, give them arguments etc. to make sure that your
    # code is robust to the situations that you'll see in action.
    # NOTE: because some of these take user input you can't run them from
    


    
    print("\nsuper_asker")
    super_asker(33, 42)
