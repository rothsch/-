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

