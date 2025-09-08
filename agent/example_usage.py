#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
DeepSeek博客生成器使用示例
"""

import os
import sys
from blog_generator import DeepSeekBlogGenerator

def main():
    """使用示例"""
    
    # 方法1: 通过环境变量设置API密钥
    os.environ['DEEPSEEK_API_KEY'] = 'your_api_key_here'  # 替换为您的实际API密钥
    
    try:
        # 初始化生成器
        generator = DeepSeekBlogGenerator()
        
        # 示例1: 生成技术博客
        print("正在生成技术博客文章...")
        tech_blog = generator.generate_blog_post(
            theme="Python异步编程实战",
            content="asyncio库基础,async/await语法详解,实际项目中的应用案例,性能优化技巧",
            style="专业技术博客"
        )
        
        # 保存到文件
        tech_file = generator.save_to_file(tech_blog, "python_async_programming.md")
        print(f"技术博客已保存: {tech_file}")
        
        # 示例2: 生成科普文章
        print("\n正在生成科普文章...")
        science_blog = generator.generate_blog_post(
            theme="人工智能的现状与未来",
            content="机器学习发展历程,深度学习突破性进展,当前技术瓶颈,未来发展趋势预测",
            style="科普文章"
        )
        
        # 保存到文件
        science_file = generator.save_to_file(science_blog, "ai_present_future.md")
        print(f"科普文章已保存: {science_file}")
        
        # 示例3: 生成教程类文章
        print("\n正在生成教程文章...")
        tutorial_blog = generator.generate_blog_post(
            theme="Docker容器化入门指南",
            content="Docker基本概念,镜像构建方法,容器部署实践,常见问题解决方案",
            style="教程指南"
        )
        
        # 保存到文件
        tutorial_file = generator.save_to_file(tutorial_blog, "docker_tutorial.md")
        print(f"教程文章已保存: {tutorial_file}")
        
        print("\n所有文章生成完成！")
        print("请检查生成的文件并根据需要进行修改。")
        
    except ValueError as e:
        print(f"配置错误: {e}")
        print("请设置DEEPSEEK_API_KEY环境变量或通过参数传入API密钥")
        return 1
    except Exception as e:
        print(f"生成过程中出现错误: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    # 检查是否设置了API密钥
    if 'DEEPSEEK_API_KEY' not in os.environ or os.environ['DEEPSEEK_API_KEY'] == 'your_api_key_here':
        print("警告: 请先设置有效的DeepSeek API密钥")
        print("方法1: 设置环境变量 DEEPSEEK_API_KEY")
        print("方法2: 修改示例代码中的API密钥")
        sys.exit(1)
    
    sys.exit(main())