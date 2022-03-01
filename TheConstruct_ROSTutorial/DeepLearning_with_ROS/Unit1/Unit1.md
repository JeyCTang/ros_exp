# Unit1 - Create your own ROS Package that Recognises Images with TensorFlow

## Moduels/Libraries
- Libraries/Modules:
  - ~~cv2~~
    - ~~cv2.cvtColor()~~
    - ~~cv2.imwrite()~~
  - ~~cv_bridge~~
    - ~~cv_bridge.CvBridge~~
  - utils
    - utils.draw_outputs
  - tensorflow
    - ~~tf.function~~
    - ~~tf.expand_dims()~~
    - ~~tf.broadcast_to()~~
    - tf.broadcast_dynamic_shape()
  - dataset
  - models


## Structure of Program

- search_for_mira_robot.py (main program)
  - TensorflowImageRecognition
    - detect_objects_from_image()
  - RosTensorFlow
    - check_image_topic_ready()
    - publish_result_objects_list()
    - callback()
    - main()
  - main_action()
- dataset.py
  - transform_targets_for_output()
  - transform_targets()
  - transform_images()
  - parse_tfrecord()
  - load_tfrecord_dataset()
  - load_fake_dataset()
- utils.py
  - load_darknet_weights()
  - braodcast_iou()
  - draw_outputs()
  - draw_labels()
  - freeze_all()
- covert.py
  - main()
- models.py
  - DarknetConv()
  - DarknetResidual()
  - DarknetBlock()
  - Darknet()
  - DarknetTiny()
  - YoloConv()
  - YoloConvTiny()
  - YoloOutput()
  - yolo_boxes()
  - yolo_nms()
  - YoloV3()
  - YoloV3Tiny()
  - YoloLoss()
- batch_norm.py
- detect.py

## Note
### cv2
#### cv2.cvtColor(src, code[, dst[, dstCn]])
cv2.cvtColor() method is used to convert an image from one color space to another. There are more than 150 color-space
conversion methods available in OpenCV
Parameters:
- src: It is the image whose color space is to be changed.
- code: It is the color space conversion code.
- dst: It is the output image of the same size and depth as src image. It is an optional parameter.
- dstCn: It is the number of channels in the destination image. If the parameter is 0 then the number of the channels is derived automatically from src and code. It is an optional parameter.

- **Return Value**: It returns an image.
- Example, see demo01_cv2_cvtColor.py

#### cv2.imwrite(filename, image)
 cv2.imwrite() method is used to save an image to any storage device. This will save the image according to the specified 
 format in current working directory.
- filename: A string representing the file name. The filename must include image format like .jpg, .png, etc.
- image: It is the image that is to be saved.
- Return Value: It returns true if image is saved successfully.

### cv_bridge
This contains CvBridge, which converts between ROS Image messages and OpenCV images. See details [here](http://wiki.ros.org/cv_bridge).

### tensorflow
#### `tf.function`
Compiles a function into a callable TensorFlow graph, details [here](https://www.tensorflow.org/api_docs/python/tf/function)

Example code:
```python
>>> @tf.function
... def f(x, y):
...   return x ** 2 + y
>>> x = tf.constant([2, 3])
>>> y = tf.constant([3, -2])
>>> f(x, y)
<tf.Tensor:... numpy=array([7,7], ...)>
```
#### `tf.expand_dim()`
Returns a tensor with a length 1 axis inserted at index `axis`. [Documentation](https://www.tensorflow.org/api_docs/python/tf/expand_dims)
```python
tf.expand_dims(
    input, axis, name=None
)
```
Given a tensor input, this operation inserts a dimension of length 1 at the dimension index axis of input's shape. 
The dimension index follows Python indexing rules: It's zero-based, a negative index it is counted backward from the end.

This operation is useful to:
- Add an outer "batch" dimension to a single element.
- Align axes for broadcasting.
- To add an inner vector length axis to a tensor of scalars.
```python
>>> x = tf.constant([1, 2, 3])
>>> y = tf.broadcast_to(x, [3, 3])
>>> print(y)

tf.Tensor(
  [[1 2 3]
   [1 2 3]
   [1 2 3]], shape=(3, 3), dtype=int32)
)
```

#### `tf.broadcast_dynamic_shape()`

### dataset

This module from the written python file `dataset.py`, in this module, most of the functions are aiming at process the data
and finally return a tensorflow.Dataset class.

### util
This module from the written python file `util.py`