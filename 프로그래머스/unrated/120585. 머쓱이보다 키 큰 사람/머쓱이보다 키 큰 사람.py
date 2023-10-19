def solution(array, height):
    
    count = 0
    array.sort(reverse = True)
    
    for i in array:
        if height < i:
             count += 1;

    return count