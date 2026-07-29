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
        count = Counter(students)

        for index, sandwich in enumerate(sandwiches):
            if count[sandwich] <= 0:
                return len(sandwiches) - index
            
            count[sandwich] -= 1
                

        return 0

# time complexity: O(n)
# space complexity: O(1)