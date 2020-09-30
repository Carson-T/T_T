import re 
pattern=re.compile(r"([a-z]{3})(\d{2})")  
match1=pattern.split("tjt12/tjt13") #如果正则表达式pattern 中有分组（圆括号），那么所有的组里的文字也会包含在列表里。
match2=pattern.findall("tjt12/tjt13") #有几对括号，findall函数就分几组，排列顺序遵循从左到右，由外到内，想要把整个字符串作为元组的一项，就给整个正则表达式套括号
match3=pattern.finditer("tjt12/tjt13")#返回match对象，不受分组影响
match4=pattern.sub(r"\1w","tjt12/tjt13")
for i in match3:
    print(i.group())
print(match1)
print(match2)
print(match4)