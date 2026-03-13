#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
高德地图API工具测试脚本
测试各种地图功能是否正常工作
"""

import os
import sys
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

try:
    from amap_tools import (
        amap_geocode, 
        amap_regeocode, 
        amap_poi_search,
        amap_weather,
        amap_driving_route,
        amap_walking_route,
        amap_coord_convert,
        amap_ip_location,
        amap_district_search
    )
    print("✅ 高德地图工具导入成功!")
except ImportError as e:
    print(f"❌ 导入失败: {e}")
    sys.exit(1)

def test_amap_tools():
    """测试高德地图API各项功能"""
    print("\n🗺️ 开始测试高德地图API工具...")
    print("=" * 60)
    
    # 1. 测试地理编码
    print("\n📍 测试1: 地理编码 - 地址转坐标")
    try:
        result = amap_geocode.invoke({"address": "北京市朝阳区阜通东大街6号"})
        print(result)
    except Exception as e:
        print(f"❌ 地理编码测试失败: {e}")
    
    # 2. 测试逆地理编码
    print("\n📍 测试2: 逆地理编码 - 坐标转地址")
    try:
        result = amap_regeocode.invoke({"location": "116.480881,39.989410", "extensions": "all"})
        print(result)
    except Exception as e:
        print(f"❌ 逆地理编码测试失败: {e}")
    
    # 3. 测试POI搜索
    print("\n🔍 测试3: POI搜索 - 查找麦当劳")
    try:
        result = amap_poi_search.invoke({"keywords": "麦当劳", "city": "北京"})
        print(result)
    except Exception as e:
        print(f"❌ POI搜索测试失败: {e}")
    
    # 4. 测试天气查询
    print("\n🌤️ 测试4: 天气查询 - 北京实时天气")
    try:
        result = amap_weather.invoke({"city": "110101", "extensions": "base"})
        print(result)
    except Exception as e:
        print(f"❌ 天气查询测试失败: {e}")
    
    # 5. 测试天气预报
    print("\n🌤️ 测试5: 天气预报 - 北京未来天气")
    try:
        result = amap_weather.invoke({"city": "110101", "extensions": "all"})
        print(result)
    except Exception as e:
        print(f"❌ 天气预报测试失败: {e}")
    
    # 6. 测试驾车路径规划
    print("\n🚗 测试6: 驾车路径规划 - 天安门到故宫")
    try:
        result = amap_driving_route.invoke({"origin": "116.397499,39.908722", "destination": "116.403963,39.924347"})
        print(result)
    except Exception as e:
        print(f"❌ 驾车路径规划测试失败: {e}")
    
    # 7. 测试步行路径规划
    print("\n🚶 测试7: 步行路径规划 - 天安门到故宫")
    try:
        result = amap_walking_route.invoke({"origin": "116.397499,39.908722", "destination": "116.403963,39.924347"})
        print(result)
    except Exception as e:
        print(f"❌ 步行路径规划测试失败: {e}")
    
    # 8. 测试坐标转换
    print("\n🧭 测试8: 坐标转换 - GPS转高德")
    try:
        result = amap_coord_convert.invoke({"locations": "116.481499,39.990475", "coordsys": "gps"})
        print(result)
    except Exception as e:
        print(f"❌ 坐标转换测试失败: {e}")
    
    # 9. 测试IP定位
    print("\n🌐 测试9: IP定位")
    try:
        result = amap_ip_location.invoke({"ip": ""})
        print(result)
    except Exception as e:
        print(f"❌ IP定位测试失败: {e}")
    
    # 10. 测试行政区域查询
    print("\n🏛️ 测试10: 行政区域查询 - 北京市")
    try:
        result = amap_district_search.invoke({"keywords": "北京", "subdistrict": 2})
        print(result)
    except Exception as e:
        print(f"❌ 行政区域查询测试失败: {e}")
    
    print("\n" + "=" * 60)
    print("🎉 高德地图API工具测试完成!")

if __name__ == "__main__":
    # 检查API Key
    amap_key = os.getenv('AMAP_API_KEY')
    if not amap_key:
        print("❌ 未找到AMAP_API_KEY环境变量!")
        print("请在.env文件中设置: AMAP_API_KEY=你的高德地图API密钥")
        sys.exit(1)
    
    print(f"✅ API Key已设置: {amap_key[:8]}...")
    test_amap_tools() 