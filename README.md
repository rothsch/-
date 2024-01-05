# 不同亮度图像下yolo框架的测试
我们通过classifier文件来分别出白天场景下的猫和黑夜场景下的猫
```python
python tools/test.py yolov5/yolov5_s-v61_fast_1xb12-40e_cat.py \
                     best.pth \
                     --show-dir show_results
```
来分别进行测试
