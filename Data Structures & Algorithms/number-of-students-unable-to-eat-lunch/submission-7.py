from collections import deque

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
        students = deque(students)
        sandwiches = deque(sandwiches)

        rotations = 0
        while students and rotations < len(students):
            if students[0] == sandwiches[0]:
                students.popleft()
                sandwiches.popleft()
                rotations = 0   # somebody ate
            else:
                rotations += 1
                students.append(students.popleft())
        
        return len(students)

# time complexity: O(n^2)
# space complexity: O(n)