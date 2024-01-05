# 不同亮度图像下yolo框架的测试
```python
python tools/test.py configs/yolov5/yolov5_s-v61_fast_1xb12-40e_cat.py \
                     work_dirs/yolov5_s-v61_fast_1xb12-40e_cat/epoch_40.pth \
                     --show-dir show_results
