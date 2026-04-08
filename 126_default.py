#create function that return total Bytes of given GB, MB and KB. in this example MB and KB optional. 
def get_total_bytes(gb, mb=0, kb=0):
    bytes_total = (gb * 1024 * 1024 * 1024) + (mb * 1024 * 1024) + (kb * 1024)
    return bytes_total
gb = int(input('enter gb'))
mb = int(input('enter mb'))
kb = int(input('enter kb'))

# Example usage
result = get_total_bytes(gb,mb,kb)
print("result into seconds using 3 arguments",result)

result = get_total_bytes(gb,mb)
print("result into seconds using 2 arguments",result)

result = get_total_bytes(gb)
print("result into seconds using 1 arguments",result)
