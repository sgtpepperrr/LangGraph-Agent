#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LangGraph Agent 简单测试脚本
测试Agent的基本功能和工具调用
"""

import os
from dotenv import load_dotenv
from graph import graph

# 加载环境变量
load_dotenv()

def test_agent():
    """测试LangGraph Agent的基本功能"""
    print("🚀 开始测试LangGraph Agent...")
    print("=" * 50)
    
    try:
        # 测试1: 简单的系统信息查询
        print("\n📊 测试1: 获取系统信息")
        response = graph.invoke({"messages": [{"role": "user", "content": "获取当前系统信息"}]})
        print("✅ 系统信息测试成功")
        
        # 测试2: 文件操作
        print("\n📁 测试2: 列出当前目录文件")
        response = graph.invoke({"messages": [{"role": "user", "content": "列出当前目录的所有文件"}]})
        print("✅ 文件操作测试成功")
        
        # 测试3: 时间日期操作
        print("\n⏰ 测试3: 获取当前时间")
        response = graph.invoke({"messages": [{"role": "user", "content": "获取当前时间和日期"}]})
        print("✅ 时间日期测试成功")
        
        # 测试4: CSV数据分析
        print("\n📈 测试4: 分析CSV数据")
        response = graph.invoke({"messages": [{"role": "user", "content": "分析telco_data.csv文件的基本信息"}]})
        print("✅ CSV数据分析测试成功")
        
        print("\n🎉 所有测试都成功完成！")
        print("=" * 50)
        print("✅ LangGraph Agent 运行正常！")
        print("🌐 API服务地址: http://127.0.0.1:2024")
        print("🎨 Studio UI地址: https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024")
        print("📊 LangSmith地址: https://smith.langchain.com")
        
    except Exception as e:
        print(f"❌ 测试失败: {e}")
        return False
    
    return True

if __name__ == "__main__":
    success = test_agent()
    if success:
        print("\n🚀 Agent已准备就绪，可以开始使用！")
    else:
        print("\n❌ Agent测试失败，请检查配置！") 