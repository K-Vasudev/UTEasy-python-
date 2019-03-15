# Code used to read in ultrasonic file
# The file must be of the form created by ALGTe1.0
#

def getParameters(data):
    axis_length = data[1]
    AxisLength = StripLine(axis_length)
    domain = data[3]
    Domain = StripLine(domain)
    return AxisLength, Domain

def StripLine(str):
    newStr = str.rstrip('\n')
    return newStr

# Main body
data = []				# 'data' will be used as list to read in file

# Open file with ultrasonic data
with open('TCPL_s3_c3_long_1.txt','r') as file:			# open UT signal file for reading
    for f in file:
	    data.append(f)
		
AxisLength, Domain = getParameters(data)
print(Domain)
print(AxisLength)

a,b,c = Domain.split()
print(a)


	