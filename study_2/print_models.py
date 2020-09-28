#-*- encoding=utf8 -*-
#Author:
#Time:  2020/7/2 17:03
#File:  print_models.py
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
# 模拟打印每一个元素，知道没有被打印的
# 打印的元素移到completed_models表格中
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print("Printing model: " + current_design)
    completed_models.append(current_design)
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)

def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model: " + current_design)
        completed_models.append(current_design)

def show_completed(completeds):
    print("\nThe following models have been printed: ")
    for completed in completeds:
        print(completed)
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
#调用print_models函数
# print_models(unprinted_designs, completed_models)
#不改变原列表function_name[:]     ------------------[:]在复制列表的时候有用过
print_models(unprinted_designs[:], completed_models)
#调用show_completed函数传completed_models
show_completed(completed_models)
print(unprinted_designs)



