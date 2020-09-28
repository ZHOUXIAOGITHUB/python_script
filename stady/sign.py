#-*- encoding=utf8 -*-
#Author:
#Time:  2020/6/30 10:41
#File:  sign.py
#判断是否继续运行的标志
prompt = "\nEnter 'quit' end to the program. "
prompt += "\nTell me something, and I will repeat it back to you: "
active = True
while active:
    message = input(prompt)
    if message == "quit":
        # print(message)
        active = False
    else:
        print(message)


