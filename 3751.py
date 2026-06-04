class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        
        def solve(num_str: str) -> int:
            n = len(num_str)
            if n < 3:
                return 0
            
            # memo dict: (index, prev_digit, prev_prev_digit, is_less, is_started)
            memo = {}
            
            def dp(i, prev, pprev, is_less, is_started):
                # Base case: completed the number
                if i == n:
                    return 0
                
                state = (i, prev, pprev, is_less, is_started)
                if state in memo:
                    return memo[state]
                
                limit = 9 if is_less else int(num_str[i])
                total_waviness = 0
                
                for d in range(limit + 1):
                    next_less = is_less or (d < limit)
                    
                    if not is_started:
                        if d == 0:
                            # Still leading zeros
                            total_waviness += dp(i + 1, -1, -1, next_less, False)
                        else:
                            # First non-zero digit placed
                            total_waviness += dp(i + 1, d, -1, next_less, True)
                    else:
                        # We have started building the number
                        next_waviness = 0
                        
                        # Check if 'prev' forms a peak or valley
                        # It needs a valid 'pprev' behind it and a 'd' ahead of it
                        if pprev != -1:
                            is_peak = (prev > pprev) and (prev > d)
                            is_valley = (prev < pprev) and (prev < d)
                            if is_peak or is_valley:
                                next_waviness = 1
                        
                        # Count waviness contributed by the current arrangement + future states
                        # To find the total waviness across all valid suffixes, we must multiply 
                        # this point's waviness by the total number of valid ways to complete the remaining digits.
                        total_waviness += next_waviness * count_ways(i + 1, d, prev, next_less) + \
                                          dp(i + 1, d, prev, next_less, True)
                
                memo[state] = total_waviness
                return total_waviness

            # Helper function to count how many valid suffix paths exist
            count_memo = {}
            def count_ways(i, prev, pprev, is_less):
                if i == n:
                    return 1
                state = (i, prev, pprev, is_less)
                if state in count_memo:
                    return count_memo[state]
                
                limit = 9 if is_less else int(num_str[i])
                ways = 0
                for d in range(limit + 1):
                    ways += count_ways(i + 1, d, prev, is_less or (d < limit))
                
                count_memo[state] = ways
                return ways

            return dp(0, -1, -1, False, False)

        return solve(str(num2)) - solve(str(num1 - 1))