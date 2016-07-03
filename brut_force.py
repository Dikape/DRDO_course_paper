import time 

class brut_force_algorithm:

    def comb(self, s_array, r):
        s_array_tuple = tuple(s_array)
        n = len(s_array_tuple)
        if r > n:
            return
        indices = list(range(r))
        yield tuple(s_array_tuple[i] for i in indices)
        while True:
            for i in reversed(range(r)):
                if indices[i] != i + n - r:
                    break
            else:
                return
            indices[i] += 1
            for j in range(i+1, r):
                indices[j] = indices[j-1] + 1
            yield tuple(s_array_tuple[i] for i in indices)

    def find_answer(self,  s_sum, s_array ):
        start_time = time.time()
        answer_set = []
        new_answer_set = []
        s_array_len = int(len(s_array))
        for i in range(s_array_len):
            c = self.comb (s_array, i)
            for j in c:
                elements_sum = sum(j)

                if (elements_sum == s_sum):

                    qwerty = list(j)
                    qwerty.sort()
                    answer_set.append(qwerty)
                    continue

        for i in answer_set:
            if i not in new_answer_set:
                new_answer_set.append(i)
        finish_time = time.time()
        a = ('Running time of algorithm : %.5f' %(finish_time - start_time))
        return new_answer_set,a


if __name__ == "__main__":

    start_time = time.time()
    start_set = [3,-1,2,2,2,2,21,12,2,3,3,3,3,14,5,7] 
    n = 15
    b= brut_force_algorithm().find_answer(n, start_set)
    finish_time = time.time()
    print ('Running time of the program : %.5f' %(finish_time - start_time))
    print (b)



