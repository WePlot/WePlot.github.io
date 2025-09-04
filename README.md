# WePlot 博客

基于Hexo框架和GitHub Pages搭建的个人博客系统。

## 项目概述

WePlot是一个基于Hexo框架的个人博客系统，通过GitHub Pages进行托管，实现高效的内容创作、发布和管理。

## 技术栈

- Hexo 7.3.0+
- Node.js 16.x+
- NexT 主题 8.x
- GitHub Pages

## 功能特点

- Markdown格式支持
- 多级分类系统
- 标签云展示
- 全站内容搜索
- Gitalk评论系统
- 社交媒体分享
- 访问统计与分析

## 快速开始

### 安装依赖

```bash
npm install
```

### 本地开发

```bash
npm run server
```

### 构建静态文件

```bash
npm run build
```

### 部署到GitHub Pages

```bash
npm run deploy
```

## 目录结构

```
WePlot/
├── _config.yml          # 站点配置文件
├── _config.next.yml     # 主题配置文件
├── package.json         # 项目依赖
├── scaffolds/           # 模板文件夹
├── source/              # 资源文件夹
│   ├── _posts/          # 文章
│   ├── about/           # 关于页面
│   ├── categories/      # 分类页面
│   ├── tags/            # 标签页面
│   └── images/          # 图片资源
└── themes/              # 主题文件夹
    └── next/            # NexT主题
```

## 自动部署

本项目使用GitHub Actions进行自动部署，每当推送到main分支时，会自动构建并部署到GitHub Pages。

## 许可证

MIT