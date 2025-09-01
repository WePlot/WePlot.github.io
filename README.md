# 技术博客

基于Hexo构建的个人技术博客，专注于前端开发、后端技术和DevOps实践分享。

## 🚀 快速开始

### 环境要求
- Node.js >= 14.0.0
- npm 或 yarn

### 安装依赖
```bash
npm install
```

### 本地开发
```bash
npm run server
# 或者包含草稿
npm run dev
```

访问 http://localhost:4000 查看博客

### 构建部署
```bash
npm run build
```

## 📝 内容管理

### 创建新文章
```bash
npm run new "文章标题"
# 或者
npx hexo new post "文章标题"
```

### 创建新页面
```bash
npx hexo new page "页面名称"
```

### 文章模板
```markdown
---
title: 文章标题
date: YYYY-MM-DD HH:mm:ss
categories: [主分类, 子分类]
tags: [标签1, 标签2, 标签3]
description: 文章摘要描述
cover: 封面图片URL
top: false
---

文章内容...
```

## 🎨 主题配置

当前使用 NexT 主题，配置文件位于：
- 站点配置：`_config.yml`
- 主题配置：`_config.next.yml`

## 📦 插件列表

- `hexo-generator-search` - 搜索功能
- `hexo-generator-searchdb` - 搜索数据库
- `hexo-generator-sitemap` - 站点地图
- `hexo-generator-robotstxt` - robots.txt
- `hexo-prism-plugin` - 代码高亮
- `hexo-renderer-marked` - Markdown渲染
- `hexo-deployer-git` - Git部署

## 🚀 部署

### GitHub Pages
1. 在GitHub创建仓库
2. 配置 `_config.yml` 中的部署设置
3. 推送代码到main分支，GitHub Actions会自动部署

### 手动部署
```bash
npm run publish
```

## 📊 项目结构

```
hexo-blog/
├── .github/workflows/    # GitHub Actions工作流
├── scaffolds/           # 文章模板
├── source/             # 源文件
│   ├── _posts/         # 文章
│   ├── about/          # 关于页面
│   ├── categories/     # 分类页面
│   └── tags/           # 标签页面
├── themes/             # 主题文件
├── _config.yml         # 站点配置
└── package.json        # 项目配置
```

## 🔧 开发指南

### 本地预览
```bash
npm run server
```

### 清理缓存
```bash
npm run clean
```

### 生成静态文件
```bash
npm run build
```

## 📈 SEO优化

- 自动生成sitemap.xml
- robots.txt配置
- 结构化数据标记
- 响应式设计
- 代码高亮和语法着色

## 🤝 贡献

欢迎提交Issue和Pull Request来改进这个博客项目。

## 📄 许可证

MIT License