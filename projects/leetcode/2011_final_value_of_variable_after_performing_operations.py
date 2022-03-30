from typing import List


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        """
        ++X and X++ increments the value of the variable X by 1
        --X and X-- decrements the value of the variable X by 1.
        Given an array of strings operations containing a list of operations, return the 
        final value of X after performing all the operations.

        Args:
            operations: list of operations
        Returns:
            int: A list of length 2 containing the indices of numbers from nums that add up to target.
        """
        operation_count = {'Add': 0, 'Subtract': 0}

        for operation in operations:
            if operation in ['++X', 'X++']:
                operation_count['Add'] += 1
            elif operation in ['--X', 'X--']:
                operation_count['Subtract'] += 1
            else:
                pass

        return 0 - operation_count['Subtract'] + operation_count['Add']
