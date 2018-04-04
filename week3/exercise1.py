# -*- coding: UTF-8 -*-
"""Week 3.

Modify each function until the tests pass.
"""




def loop_ranger(start, stop=None, step=1):
  new_list = []
  for i in range(start,stop,step):  
    new_list.append(i)
  return new_list  
"""Return a list of numbers between start and stop in steps of step.

    Do this using any method apart from just using range()
"""



def lone_ranger(start, stop, step):
  return range(start, stop, step)
"""Duplicate the functionality of range.

    Look up the docs for range() and wrap it in a 1:1 way
"""
  


def two_step_ranger(start, stop, step=2):
    new_list = []
    for i in range(start,stop,step):  
      new_list.append(i)
    return new_list  
    """Make a range that steps by 2.

    Sometimes you want to hide complexity.
    Make a range function that always has a step size of 2
    """



def stubborn_asker(low, high):
  message = "Give me a number between {low}, and {high}: ".format(low=low, high=high)
  
  while True:
    input_num = int(input(message))
    if low < input_num < high:
      print ("Thanks! {} looks good.".format(input_num))
    else:
      print ("{input} isn't between {low}, and {high}" .format(input=input_num, low=low, high=high))
  return
  """Ask for a number between low and high until actually given one.

    Ask for a number, and if the response is outside the bounds keep asking
    until you get a number that you think is OK
  """


def not_number_rejector():
  while True:
    try:
        data = int(input("Please enter a number: "))
    except ValueError:
        print("Sorry, plaase type a number.")
        #better try again... Return to the start of the loop
        continue
    else:
        print (data, "is a number!!")
        break
  return data  

"""Ask for a number repeatedly until actually given one.

    Ask for a number, and if the response is actually NOT a number (e.g. "cow",
    "six", "8!") then throw it out and ask for an actual number.
    When you do get a number, return it.
"""
"""def not_number_rejector(message):
  if message > -100000000:
    return ("You have a number!")
  else:
    return ("That's a string, put a number")
#print (not_number_rejector(-100000001))
  try:
    message = int(input("Type a number:"))
    print ("Thats a number")
  except ValueError:
    print("This is not a number.")
"""


#def super_asker(low, high):
"""Robust asking function.

    Combine stubborn_asker and not_number_rejector to make a function
    that does it all!
"""
def super_asker(message):
  message = int(input('enter a number:'))
  if message == 5:
    return ('YES, 5 is the number!')
  elif message > -100000000:
    return ("You have a number!")  
  else:
    return ('keep trying')

    


if __name__ == "__main__":
    # this section does a quick test on your results and prints them nicely.
    # It's NOT the official tests, they are in tests.py as usual.
    # Add to these tests, give them arguments etc. to make sure that your
    # code is robust to the situations that you'll see in action.
    # NOTE: because some of these take user input you can't run them from
    

    print("\nloop_ranger", loop_ranger(1, 10, 2))
    print("\nlone_ranger", lone_ranger(1, 10, 3))
    print("\ntwo_step_ranger", two_step_ranger(1, 10))
    print("\nstubborn_asker")
    stubborn_asker(30, 45)
    print("\nnot_number_rejector")
    not_number_rejector("Give me a number: ")
    print("\nsuper_asker")
    super_asker(33, 42)