input_data = open('input.txt', 'r')
data = input_data.read ()

data = data.split()
k = int(data[0])
a = int(9)
b = int(a-k)

output_data = open ('output.txt', 'w')
output_data.write(str(k) + str(a) + str(b))

input_data.close()
output_data.close()