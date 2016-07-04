import time 

class dinamic_algorithm:

    def positive_negative_sums(self,seq):
        P, N = 0, 0
        for c in seq:
            if c >= 0:
                P += c
            else:
                N += c

        return P, N

    def find_set(self,list_set,suma,seq):
        answer = []
        count = len(list_set)
        current = 0
        for i in reversed(list_set):
            
            for j in i:

                if(count == len(list_set)):

                    if (j[0]==True and j[3]==False and j[2]==suma):
                        answer.append(j[1])
                        
                        current = j[2]-j[1]
                    elif(j[0]==True and j[3]==True and j[2]==suma):
                        current = j[2]
                        break

                else:
                    if (j[0]==True and j[3]==False and j[2]==current):
                        answer.append(j[1])
                        
                        current = j[2]-j[1]
                        if (count==1 and j[4]==True):
                            answer.append(seq[0])
                        break
                    elif(j[0]==True and j[3]==True and j[2]==current):
                        current = j[2]
                        
                        if count==1:
                            answer.append(seq[0])
                        break

            count -= 1 

        return (answer)
            # print ('\n',i)

    def subset_sum(self,seq, s):
        start_time = time.time()
        P, N = self.positive_negative_sums(seq)

        if not seq or s < N or s > P:
            finish_time = time.time()
            a = ('Running time of algorithm : %.5f' %(finish_time - start_time))
            b = ("Such Subsets do not exists.")
            return b,a

        n, m = len(seq), P - N + 1

        table = [[False] * m for x in range(n)]
        table[0][seq[0]] = True
        list_set =[]
        for i in range(1, n):

            b_table = []
            for j in range(N, P+1):

                table[i][j] = seq[i] == j or table[i-1][j] or table[i-1][j-seq[i]]

                a = (table[i][j], seq[i] , j , table[i-1][j] , table[i-1][j-seq[i]] )
                b_table.append(a)

            list_set.append(b_table)
        if table[n-1][s]==True:
            answ = self.find_set(list_set,s,seq)
            finish_time = time.time()
            a = ('Running time of algorithm : %.5f' %(finish_time - start_time))
            return answ,a
        else:
            finish_time = time.time()
            a = ('Running time of algorithm : %.5f' %(finish_time - start_time) )
            b = ("Such Subsets do not exists.")
            return b,a

if __name__ == "__main__":
    start_time = time.time()
    start_set = [3,-1,2,2,2,2,2,2,2,21,12,-4,-4,-123,2,3,3,444,3,3,11,1,2,124,345,2,35,12,3,2,32,23,523,53,3,22,3,32,35,12,12,12,1212,12,23,4,4,2,2,3,3,2,23,2,2,21,2,2,2,2,21,12,-4,-4,-123,2,3,3,444,3,3,11,1,2,124,345,2,35,12,3,2,32,23,523,53,3,22,3,32,35,12,12,12,1212,12,23,4,4,2,2,3,3,2,23,2,12,-4,-4,-123,2,3,3,444,3,3,11,1,2,124,345,2,35,12,3,2,32,23,523,53,3,22,3,32,35,12,12,12,1212,12,23,4,4,2,2,3,3,2,23,2,23,2,2,2,3,2,3,2,3,2,43,2,4,5,7] 
    n = 555
    a = dinamic_algorithm().subset_sum(start_set,n)
    finish_time = time.time()
    print ('Running time of program : %.5f' %(finish_time - start_time))
    print (a)