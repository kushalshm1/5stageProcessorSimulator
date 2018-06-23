def dec_to_bin(x):
    return int(bin(x)[2:])

'''Memory Class
It contains Three Lists which are created by default whenever an Object of Memory is created

Three Lists are 
ICache
DCache
Registers

ICache will contain Instructions
DCache will contain ArrayData Values or any other Data
Registers are Fastest Memory areas and they are only four they will contain values of Variables.

This class also contains three Member Functions
1. AppendICache,
This Appends Instruction to ICache and can be used in the start when we will give instructions to our processor
2. AppendDCache
This Appends to DCache list taking Value(What to append) and Address(Where to append) as Arguments
3. AppendRegister
Appends to Registers taking Value(What to Append) and Register number(Which register to append out of Four)'''
class Memory:
	def __init__(self):
		self.ICache = [[0]*16]*128
		self.DCache = [[0]*8]*256
		self.Registers = [0]*4

	def AppendICache(self,value,address):
		self.ICache[address] = value
	def AppendDCache(self,value,address):
		self.DCache[address] = value
	def AppendRegister(self,value,registerNumber):
		self.Registers[RegisterNumber] = value


class ControlUnit(Memory):
	def __init__(self,ins):
		self.Instruction = ins
		self.OpCode = ins[0]
		Memory.__init__(Memory)

	def Go(self):
		# while(Memory.ICache[i]!=0):
		if(self.OpCode == 'LOADIMM'):
			# Memory.AppendRegister(self.Instruction[1],self.Instruction[2])
			Memory.Registers[self.Instruction[2]] = self.Instruction[1]
		elif(self.OpCode == 'LOAD'):
			Memory.AppendRegister(DCache[self.Instruction[2]],self.Instruction[1])
		elif(self.OpCode == 'STORE'):	
			Memory.AppendDCache(self.Instruction[1],DCache[self.Instruction[2]])






class ALU(Memory):
	def __init__(self,ins):
		self.Inputs = [0]*2
		self.Flags = 0
		Memory.__init__()


	def changeFlag(self,state):
		self.Flag = state

	def DoOperation(self,OpCode):
		if(OpCode[0]=='NOP'):
			pass
		elif(OpCode[0]=='ADD'):
			self.Inputs[0] = Memory.Registers[self.Instruction[1]]
			self.Inputs[1] = Memory.Registers[self.Instruction[2]]
			self.x = (self.Inputs[0]+self.Inputs[1])	
			if(self.x==0):
				self.Flag = 0
			else:
				self.Flag = 1
			return self.x
		elif(OpCode[0]=='SUB'):
			self.Inputs[0] = Memory.Registers[self.Instruction[1]]
			self.Inputs[1] = Memory.Registers[self.Instruction[2]]
			self.x = (self.Inputs[0]-self.Inputs[1])	
			if(self.x==0):
				self.Flag = 0
			else:
				self.Flag = 1
			return self.x
		elif(OpCode[0]=='NAND'):
			self.Inputs[0] = self.Instruction[1]
			self.Inputs[1] = self.Instruction[2]
			self.x = (Inputs[0]*Inputs[1])
			if(self.x==0):
				self.Flag = 0
			else:
				self.Flag = 1
			return self.x
		elif(OpCode[0]=='MOV'):
			self.Inputs[0] = Memory.Registers[self.Instruction[1]]
			self.Inputs[1] = Memory.Registers[self.Instruction[2]]
			self.temp = 0
			self.temp = Memory.Registers[self.Instruction[4:6]]
			Memory.Registers[self.Instruction[4:6]] = Memory.Registers[self.Instruction[6:4]]
			Memory.Registers[self.Instruction[6:4]] = Memory.Registers[self.Instruction[4:6]]

		elif(OpCode[0]=='NOR'):
			self.Inputs[0] = Memory.Registers[self.Instruction[4:6]]
			self.Inputs[1] = Memory.Registers[self.Instruction[6:8]]
			self.x = (Inputs[0]*Inputs[1])
			if(self.x==0):
				self.Flag = 0
			else:
				self.Flag = 1
			return self.x
		elif(OpCode[0]=='AND'):
			self.Inputs[0] = Memory.Registers[self.Instruction[4:6]]
			self.Inputs[1] = Memory.Registers[self.Instruction[6:8]]
			self.x = (Inputs[0]*Inputs[1])
			if(self.x==0):
				self.Flag = 0
			else:
				self.Flag = 1
			return self.x





		




mem = Memory()
mem.AppendICache(["LOADIMM",100,0],0)
mem.AppendICache(["LOADIMM",10,2],0)


cu = ControlUnit(mem.ICache[0])
cu.Go()
print(mem.Registers)
# print(mem.ICache)
# cu = ControlUnit()
