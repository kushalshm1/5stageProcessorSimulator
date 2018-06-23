i_cache = [00000000]*256
d_cache = [00000000]*256
registerFile = [0000000]*4


#This is a test comment


'''
All 16 Instruction of Our Processor
"NOP":0000,
"ADD":0001,     RX,RY
"SUB":0010,     RX,RY
"NAND":0011,    RX,RY
"MOV":0100,     RX,RY
"NOR":0101,     RX,RY
"NOT":0110,     RX
"AND":0111,     RX,RY
"BR":1000,      8-Bit Address of I-Cache
"BRZ":1001,     8-Bit Address of I-Cache
"RETURN":1010,
"BRSUB":1011,   8-Bit Address of I-Cache
"LOAD":1100,    RX, 8-Bit Address of D-Cache
"STORE":1101,   RX, 8-Bit Address of D-Cache 
(It is an Exception we are storing value in D-Cache
 but its address is coming after register value, 
 but it is still a destination)
"LOADIMM":1110, RX, 8-Bit Data
"OR":1111       RX,RY
'''

#1. Sample code to be converted into assembly
x = 10
y = 0
for i in range(0,21):
	y = y+x
	x = x-2
	if(x==0):
		break


#Assembly Code

'''
(00) LOADIMM R0,10
(02) LOADIMM R1,0
(04) LOADIMM R2,21
(06) ADD R1,R0
(08) LOADIMM R3,2
(10) SUB R0,R3
(12) BRZ 22
(14) LOADIMM R3,1
(16) SUB R2,R3
(18) BRZ 22
(20) BR 6
(22) END 

'''


#2. Sample code to be converted into assembly
arr = []
for i in range(0,10):
	arr.append(i)


#Assembly Code

'''
(00) LOADIMM R0,10
(02) LOADIMM R1,00
(04) LOADIMM R3,1
(06) STORE R0, R1
(08) ADD R1,R3
(10) SUB R0,R3
(12) BRZ 14
(14) BR 06
(16) END

'''

def dec_to_bin(x):
    return int(bin(x)[2:])


print(dec_to_bin(100))



DCache = [[0]*5]*10

print(DCache)