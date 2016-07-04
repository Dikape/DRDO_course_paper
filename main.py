import os
import time
from brut_force import brut_force_algorithm
from dinamic_programming import dinamic_algorithm

if __name__ == "__main__":

    choice = input("Do you want read from file? y/n ")
    if choice.lower() == 'y':
        name_file = input("Please input name of file: ")
        file = open (name_file, 'r')
        # for i in file:
        #     start_set.append(int(i))
        start_set = [int(i) for i in file]
        file.close()
    else:
        start_set = []
        numb = input("Please enter number of array: ")
        for i in range(int(numb)):
            el = int(input ("Enter elements :"))
            start_set.append(el)

    n = int (input ("Please input sum , which you searching : "))
    while True: 
        print ("-"*50)

        selection = input("""What do you want? 
  1.Solve this problem by 'brut force' algorithm. 
  2.Solve this problem by dinamic programing.
  3. Exit.

  Choose some number : """) 
        print ("-"*50)

        if selection =='1': 

            start_time = time.time()

            a = brut_force_algorithm().find_answer(n, start_set)
            f = open ('brut_force_result.txt', 'w')

            finish_time = time.time()

            f.write('Needed Sum : ' + str(n) + '\n')
            f.write('Running time of the program : %.5f' %(finish_time - start_time) + '\n')
            f.write (a[1]+'\n')
            for i in a[0]:
                f.write (str(i) + '\n')
            if not a[0]:
                f.write ('Such Subsets do not exists.')

            print ('You can see result in file "brut_force_result.txt"')
            f.close()
            os.system("start "+"brut_force_result.txt")

        elif selection == '2':
            start_time = time.time()
            a = dinamic_algorithm().subset_sum(start_set,n)

            f = open ("dinamic_programming_result.txt", 'w')

            finish_time = time.time()
            f.write('Needed Sum : ' + str(n) + '\n')
            f.write ('Running time of program : %.5f' %(finish_time - start_time) + '\n')

            f.write(a[1]+'\n')
            f.write(str(a[0])+'\n')

            if not a[1]:
                f.write ('Such Subsets do not exists.')

            f.close()
            print ('You can see result in file "dinamic_programming_result.txt"')
            os.system("start "+"dinamic_programming_result.txt")


        elif selection == '3': 
          break

        else: 
          print ("Unknown Option Selected!")

