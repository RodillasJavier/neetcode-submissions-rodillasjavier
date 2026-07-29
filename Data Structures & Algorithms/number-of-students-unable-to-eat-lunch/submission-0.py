from collections import Counter

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        """
        in: 
            - array of students
                - students[j] : preference of the j-th student in the initial queue
            - stack of sandwiches
                - sandwiches[i] : type of sandwich the ith one is
        out:
            - return number of students unable to eat
        constraints:
            - iff student @ front of q prefers sandwich:
                - take it, leave q
                - else, back of q
            - until none of the students want the top sandwich
        """
        res = len(students)
        count = Counter(students)

        for sandwich in sandwiches:
            if count[sandwich] > 0:
                res -= 1
                count[sandwich] -= 1
            else:
                return res

        return res
