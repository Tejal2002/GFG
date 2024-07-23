#User function Template for python3

class Solution:
        
    def sumOfSeries(self,n):
        #code here
    
        # if n == 1:
        #     return 1
        
        # return n**3 + self.sumOfSeries(n-1)

        #Python has a default recursion depth limit (usually 1000), 
        #and your input value 18468 exceeds this limit.
        
        # Iterative approach 
        # total_sum = 0
        # for i in range(1, n + 1):
        #     total_sum += i ** 3
        # return total_sum
        
        #Using formula 
        
        # Calculate the sum of the first n natural numbers
        sum_n = n * (n + 1) // 2
        # Return the square of the sum
        return sum_n ** 2
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        ob=Solution()
        print(ob.sumOfSeries(N)) 
# } Driver Code Ends