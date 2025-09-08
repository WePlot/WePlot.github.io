# DeepSeek API 博客生成器

基于DeepSeek API的自动博客生成脚本，可以根据指定主题和内容生成高质量的博客文章。

## 功能特性

- 🎯 根据主题和内容要点生成完整博客文章
- 📝 支持Markdown格式输出
- 🎨 可自定义写作风格
- 💾 自动保存到文件
- 🔧 完整的错误处理

## 安装依赖

```bash
pip install -r requirements.txt
```

## 配置

1. 复制配置文件：
```bash
cp config.example.py config.py
```

2. 在 `config.py` 中填入您的DeepSeek API密钥：
```python
DEEPSEEK_API_KEY = "your_actual_api_key_here"
```

或者设置环境变量：
```bash
export DEEPSEEK_API_KEY="your_actual_api_key_here"
```

## 使用方法

### 命令行方式

```bash
# 基本使用
python blog_generator.py --theme "Python异步编程" --content "asyncio基础,async/await语法,实际应用案例"

# 指定写作风格
python blog_generator.py --theme "机器学习入门" --content "监督学习,无监督学习,深度学习基础" --style "科普文章"

# 指定输出文件名
python blog_generator.py --theme "Docker容器化" --content "Docker基础,镜像构建,容器部署" --output "docker_intro.md"

# 直接提供API密钥
python blog_generator.py --theme "Web开发" --content "前端框架,后端技术,数据库" --api-key "your_api_key"
```

### Python代码方式

```python
from blog_generator import DeepSeekBlogGenerator

# 初始化生成器
generator = DeepSeekBlogGenerator(api_key="your_api_key")

# 生成博客文章
blog_content = generator.generate_blog_post(
    theme="人工智能发展",
    content="机器学习历史,深度学习突破,未来趋势",
    style="技术综述"
)

# 保存到文件
filepath = generator.save_to_file(blog_content, "ai_development.md")
print(f"文章已保存到: {filepath}")
```

## 参数说明

- `--theme`: 博客主题（必需）
- `--content`: 内容要点（必需）
- `--style`: 写作风格，默认为"专业技术博客"
- `--api-key`: DeepSeek API密钥
- `--output`: 输出文件名

## 输出格式

生成的博客文章包含：
- YAML front matter（标题、日期、作者等信息）
- Markdown格式的内容
- 适当的标题层级结构
- 技术细节和示例（如果适用）

## 注意事项

1. 确保您有有效的DeepSeek API访问权限
2. API调用可能需要付费，请关注使用量
3. 生成的文本可能需要人工审核和调整
4. 建议在正式发布前检查内容的准确性和适当性

## 错误处理

脚本包含完整的错误处理机制，会捕获以下错误：
- API请求失败
- 认证错误
- 响应解析错误
- 文件写入错误