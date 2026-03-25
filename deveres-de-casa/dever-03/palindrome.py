

def is_palindrome(arr):

    arr_len = len(arr)

    if arr_len <= 1:
        return True
    else:
        
        if arr[0] == arr[-1]:
            return is_palindrome(arr[1:-1])
        else:
            return False
        
def main():
    
    arr = ['a', 'c','b', 'a']
    
    output = is_palindrome(arr)

    if output == True:
        print(f'O Array {arr} é um palindromo')
    elif output == False:
        print(f'O Array {arr} não é um palindromo')




if __name__ == '__main__':
    main()


