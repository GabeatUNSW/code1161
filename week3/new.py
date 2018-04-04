def stubborn_asker(low, high):
  message = "Give me a number between {low}, and {high}: ".format(low=low, high=high)
  
  while True:
    input_num = int(input(message))
    if low < input_num < high:
      print ("Thanks! {} looks good.".format(input_num))
    else:
      print ("{input} isn't between {low}, and {high}" .format(input=input_num, low=low, high=high))
  return