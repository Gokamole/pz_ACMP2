input_data = open('input.txt', 'r')
data = input_data.read ()

data = data.split()
a = int(data[0])
b = int(9)
c = int(b-a)
d = str(a*100 + b*10 + c)

output_data = open ('output.txt', 'w')
output_data.write(d)

input_data.close()
output_data.close()