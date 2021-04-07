from sys import argv
def parase(payload): 
    mode=payload[0]
    payload=payload[1:]
    startdata,enddata,beg,en=modifiers[mode]
    a=[]
    a.extend(startdata)
    a.extend([beg+i+en for i in payload.split(',')])
    a.extend(enddata)
    return a

modifiers={'H':[['friststartcall','secondstartcall'],['fristendcall','end'],'beg','end']}




crc0='0000000000000000'
eop='001'
sync='01010100'
pid='11010010'

begin=crc0+eop
end=sync+pid


file=begin+(end+begin).join(parase(open(argv[1],'r').read()))+end
print(file)
with open(argv[2],'w') as f:
    f.write(file)
