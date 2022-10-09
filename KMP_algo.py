def KMP(text, pattern):
    N = len(text); # Computing length of the text given 
    M = len(pattern); # Computing length of the pattern given

    # Creating an LPS array of size M and initializing all values as 0
    lps_arr = [0]*M 

    # A function to compute the LPS values and fill them in LPS array
    LPS_Table(pattern, M, lps_arr)
    i = 0 # initial index for iterating text
    j = 0 # initial index for iterating pattern
    while i < N:
      
        else:
            if j != 0:
                j = lps_arr[j-1]
            else:
                i += 1
        
        if j == M:
            print("Pattern found at index " + str(i-j))
            j = lps_arr[j-1]

def LPS_Table(pattern,M,lps_arr):
    l = 0 # Gives us the length of matching prefix & suffix
    i = 1 # used to iterate till the end of the pattern

    # As there is no prefix or suffix for first element yet
    lps_arr[0] = 0 
    while i < M:
        # If a match occours 
        # we increment the value of lps_arr[i] by l+1
        # and we also increment the value of l & i
        # to check the condition for next set of values
        if pattern[i] == pattern[l]:
            lps_arr[i] = l + 1
            l += 1
            i += 1
        
        # If a mismatch occours 
        else:
            if l != 0:
                # We change the value of l 
                # to the value at (l-1)th index of lps_arr
                l = lps_arr[l-1]

            else:
                # The value is set to 0 in case 
                # of no prefix or suffix 
                # and the value of i is incremented 
                # to compare l with the next value
                lps_arr[i] = 0
                i += 1  

    print("LPS Table found")
    print(lps_arr)
    print()

text = input("Enter Text String : ")
pattern = input("Enter the pattern : ")
print()
KMP(text, pattern)

