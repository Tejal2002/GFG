#User function Template for python3
class Solution:
    def print2largest(self, arr):
        
        # Code Here
        
    # METHOD 1
        # small = float('inf')
        # second_small = float('inf')
        # large = float('-inf')
        # second_large = float('-inf')
        
        # for i in range(len(arr)):
        #     if small > arr[i]:
        #         small = arr[i]
        #     if large < arr[i]:
        #         large = arr[i]
            
        # for i in range(len(arr)):
        #     if arr[i] < second_small and arr[i] != small :
        #         second_small = arr[i]
        #     if arr[i] > second_large and arr[i] != large : 
        #         second_large = arr[i]
                
        # if len(arr)==0 or len(arr)==1:
        #     return -1
        # elif second_large == large :
        #     return -1
        # else:
        #     return second_large
            
    #METHOS 2
        large = float('-inf')
        second_large = float('-inf')
        
        for i in range(len(arr)):
            if arr[i] > large:
                second_large = large
                large = arr[i]
            elif arr[i] > second_large and arr[i] != large:
                second_large = arr[i]
        
        if len(arr) < 2 :
            return -1
        elif second_large == large :
            return -1
        else:
            return second_large
        
        
        
        
        


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.print2largest(arr)
        print(ans)

# } Driver Code Ends