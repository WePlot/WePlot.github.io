---
title: Windows Player Unity截屏报错：ReadPixels was called to read pixels from system frame buffer, while not inside drawing frame.
date: 2025-09-12 11:44:50
tags:
---



通常在Unity内截屏时，会使用 Texture2D 的 ReadPixels 接口，例如：

```c
// 先创建一个的空纹理，大小可根据实现需要来设置

Texture2D screenShot = new Texture2D((int)rect.width, (int)rect.height, TextureFormat.RGB24, false);

// 读取屏幕像素信息并存储为纹理数据，

screenShot.ReadPixels(rect, 0, 0);

screenShot.Apply();
```



当想要截取屏幕内容时，如果直接这样使用，就会报错 ReadPixels was called to read pixels from system frame buffer, while not inside drawing frame. 其底层原因是因为在调用 ReadPixels 接口的时候，并不能保证BackBuffer 是一个有效状态，BackBuffer 的有效是从 clearBuffer 之后到 swapbuffer 之前，在opengl标准中有说明，一旦 swapbuffer 执行后，backbuffer 内容将变成 invalid，此时读取backbuffer将产生未定义行为。因此在unity中将BeginRender 到 EndRender 定义为 drawing frame，读取屏幕缓冲区只能在这个阶段内才能生效。



为了保证这个时机，Unity 提供了两种方式

1. 协程

```c
        yield return new WaitForEndOfFrame();
        Rect rect = new Rect(0, 0, Screen.width, Screen.height);
        // 先创建一个的空纹理，大小可根据实现需要来设置
        Texture2D screenShot = new Texture2D((int)rect.width, (int)rect.height, TextureFormat.RGB24, false);

        // 读取屏幕像素信息并存储为纹理数据，
        screenShot.ReadPixels(rect, 0, 0);
        screenShot.Apply();

        // 然后将这些纹理数据，成一个png图片文件
        byte[] bytes = screenShot.EncodeToPNG();
```

2. OnPostRender

```c
   bool isScreenShot = false;
    private void OnPostRender()
    {
        if (isScreenShot)
        {
            Rect rect = new Rect(0, 0, Screen.width, Screen.height);
            // 先创建一个的空纹理，大小可根据实现需要来设置
            Texture2D screenShot = new Texture2D((int)rect.width, (int)rect.height, TextureFormat.RGB24, false);

            // 读取屏幕像素信息并存储为纹理数据，
            screenShot.ReadPixels(rect, 0, 0);
            screenShot.Apply();

            // 然后将这些纹理数据，成一个png图片文件
            byte[] bytes = screenShot.EncodeToPNG();
            print("isScreenShot "+ bytes.Length);
            isScreenShot = false;
        }
    }
```



这两处调用的时机都是在执行完所有的渲染命令，并且在交换背景缓冲区之前，保证了后续操作的正确性。



特殊情况说明：

实际项目过程会发生，即使按照上述正确的流程编写代码，依然遇到报错的情况，例如：

windows应用开发过程中，将 Unity 嵌入到其他应用中，如果使用了 win32 接口将 Unity 窗口隐藏，此时如果触发了截屏操作会报错，这是因为窗口隐藏时，触发了设别丢失 （Device Lost），导致整体渲染上下文都失效了。



解决这个问题可考虑以下思路：

1. 业务上不完全依赖截图返回的结果，一旦操作异常，就使用其他方案替换截图
2. 规避使用窗口隐藏接口，将窗口位置移动到屏幕外，实现同样的不可见效果