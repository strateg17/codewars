def find_nb(m):
    n = 0
    current_volume = 0
    
    while current_volume < m:
        current_volume = current_volume + n ** 3
        n = n + 1
        
        if current_volume == m:
            return n - 1
        else:
            continue
            
    return -1
