# 不同亮度图像下yolo框架的测试
我们通过classifier.py文件来分别出白天场景下的猫和黑夜场景下的猫。
通过下面的命令
```python
python tools/test.py yolov5/yolov5_s-v61_fast_1xb12-40e_cat.py \
                     best.pth \
                     --show-dir show_results
```
来对区分好的图片进行测试

测试结果如下

![image](https://github.com/rothsch/Testing-of-YOLO-Framework-under-Different-Brightness-Images/assets/68881039/e62db4bb-af51-4353-80b9-34f44596c57f)

可以看出在黑夜和白天条件下，YOLO框架的准确率较高，特别是在白天条件下。
检测速度在白天条件下最快，这可能是因为光线充足，特征更加明显易于识别。
误检率在黑白混合的条件下最高，这可能是因为模型在处理不同类型图像时遇到了困难。
这个图表说明，在特定光照条件下进行分类测试（如黑夜和白天），相较于将黑白图像混合在一起测试，能更有效地评估模型在不同光照环境下的性能。
