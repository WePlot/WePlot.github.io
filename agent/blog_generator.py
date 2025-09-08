#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
DeepSeek API 博客生成器
根据指定主题和内容生成博客文章的Python脚本
"""

import os
import json
import requests
from typing import Optional, Dict, Any
import argparse
from datetime import datetime

class DeepSeekBlogGenerator:
    """DeepSeek API 博客生成器类"""
    
    def __init__(self, api_key: Optional[str] = None):
        """
        初始化博客生成器
        
        Args:
            api_key: DeepSeek API密钥，如果为None则从环境变量读取
        """
        self.api_key = api_key or os.getenv('DEEPSEEK_API_KEY')
        if not self.api_key:
            raise ValueError("未找到DeepSeek API密钥，请设置环境变量DEEPSEEK_API_KEY或通过参数传入")
        
        self.api_url = "https://api.deepseek.com/v1/chat/completions"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
    
    def generate_blog_post(self, theme: str, content: str, style: str = "专业技术博客") -> str:
        """
        生成博客文章
        
        Args:
            theme: 博客主题
            content: 博客内容要点
            style: 写作风格，默认为"专业技术博客"
            
        Returns:
            生成的博客文章内容
        """
        prompt = self._build_prompt(theme, content, style)
        
        payload = {
            "model": "deepseek-chat",
            "messages": [
                {
                    "role": "system",
                    "content": "你是一位专业的博客作者，擅长撰写技术博客文章。请根据用户提供的主题和内容要点，生成一篇结构完整、内容丰富的博客文章。"
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "temperature": 0.7,
            "max_tokens": 2000
        }
        
        try:
            response = requests.post(self.api_url, headers=self.headers, json=payload, timeout=30)
            response.raise_for_status()
            
            result = response.json()
            blog_content = result['choices'][0]['message']['content']
            
            return self._format_blog_post(blog_content, theme)
            
        except requests.exceptions.RequestException as e:
            raise Exception(f"API请求失败: {e}")
        except (KeyError, IndexError) as e:
            raise Exception(f"API响应解析失败: {e}")
    
    def _build_prompt(self, theme: str, content: str, style: str) -> str:
        """构建提示词"""
        return f"""请根据以下信息生成一篇{style}风格的博客文章：

主题：{theme}
内容要点：{content}

要求：
1. 文章结构完整，包含引言、正文和结论
2. 使用Markdown格式，包含适当的标题层级
3. 语言流畅，逻辑清晰
4. 字数在800-1500字之间
5. 包含实际的技术细节和示例（如果适用）
6. 保持专业性和可读性

请直接输出完整的博客文章内容："""
    
    def _format_blog_post(self, content: str, theme: str) -> str:
        """格式化博客文章，添加元信息"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"""---
title: {theme}
date: {timestamp}
author: DeepSeek Blog Generator
categories: [技术, AI]
tags: [deepseek, 博客生成, AI写作]
---

{content}

---
*本文由DeepSeek API自动生成*
"""
    
    def save_to_file(self, content: str, filename: Optional[str] = None) -> str:
        """
        将博客内容保存到文件
        
        Args:
            content: 博客内容
            filename: 文件名，如果为None则自动生成
            
        Returns:
            保存的文件路径
        """
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"blog_post_{timestamp}.md"
        
        filepath = os.path.join("output", filename)
        os.makedirs("output", exist_ok=True)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return filepath

def main():
    """命令行入口函数"""
    parser = argparse.ArgumentParser(description="DeepSeek API 博客生成器")
    parser.add_argument("--theme", required=True, help="博客主题")
    parser.add_argument("--content", required=True, help="博客内容要点")
    parser.add_argument("--style", default="专业技术博客", help="写作风格")
    parser.add_argument("--api-key", help="DeepSeek API密钥")
    parser.add_argument("--output", help="输出文件名")
    
    args = parser.parse_args()
    
    try:
        # 初始化生成器
        generator = DeepSeekBlogGenerator(api_key=args.api_key)
        
        # 生成博客文章
        print("正在生成博客文章...")
        blog_content = generator.generate_blog_post(args.theme, args.content, args.style)
        
        # 保存到文件
        output_path = generator.save_to_file(blog_content, args.output)
        
        print(f"博客文章生成成功！")
        print(f"保存路径: {output_path}")
        print(f"\n文章预览:")
        print("-" * 50)
        print(blog_content[:500] + "..." if len(blog_content) > 500 else blog_content)
        
    except Exception as e:
        print(f"错误: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())