'''
Xiaochi Ma
2018-11-12
'''

def readFile(fileName):
    
    count = {}
    fileConn = open(fileName)
    
    for line in fileConn:
        keys = line.split(" ")
        count[keys[0]] = count.get(keys[0], 0) + 1
        
    fileConn.close()

    return count
    
    
    

if __name__ == '__main__':
    
    fileName = "hosts_access_log_00.txt"
    
    counts = {}
    fileConn = open(fileName)
    
    for line in fileConn:
        keys = line.split(" ")
        counts[keys[0]] = counts.get(keys[0], 0) + 1
        
    fileConn.close()
    
    text_file = open("records_"+fileName, "w")
    for key, value in counts.items():
        text_file.write(key + ' ' + str(value) + '\n')
    text_file.close()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    