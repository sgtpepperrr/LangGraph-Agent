#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
sys.path.append('/Users/liaowang/Desktop/Fun AI/LangGraph_Agent')

from graph import fig_inter

# 测试fig_inter函数
test_code = '''
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(8,6))
plt.plot([1,2,3,4], [1,4,2,3])
plt.title("Test Chart")
plt.xlabel("X axis")
plt.ylabel("Y axis")
fig.tight_layout()
'''

print("开始测试fig_inter函数...")
result = fig_inter(test_code, 'fig')
print(f"测试结果: {result}")

# 检查images文件夹
images_dir = '/Users/liaowang/Desktop/Fun AI/LangGraph_Agent/images'
if os.path.exists(images_dir):
    print(f"\nimages文件夹存在: {images_dir}")
    files = os.listdir(images_dir)
    print(f"文件夹内容: {files}")
else:
    print(f"\nimages文件夹不存在: {images_dir}")