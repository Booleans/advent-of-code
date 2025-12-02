import re 

pattern = r'^(\d+)\1$'

invalid_ID = re.compile(pattern)

invalid_IDs = [] 

for num in range(199617, 254905):
    if invalid_ID.match(str(num)):
        invalid_IDs.append(num)
    
x = 5       