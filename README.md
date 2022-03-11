# laboratory
Data analysis and processing

## First approach

The first approach was to extract the images -> 01_image_extraction.ipynb

With these images in the CSV, we used 02_age_and_gender_v1.ipynb but the val_loss and val_accuracy were too low.

## Second approach

Using:

1. 03_age_v2.ipynb

2. 04_gender_v2.ipynb

# Metrics

You have to see what % is wrong in each age range. Do you make more mistakes with young or old people? with men or women?


# References
- https://www.tensorflow.org/api_docs/python/tf/keras/losses
- https://www.tensorflow.org/api_docs/python/tf/keras/applications/efficientnet/EfficientNetB7
- https://machinelearningmastery.com/how-to-reduce-overfitting-in-deep-learning-with-weight-regularization/

resnet152 -> gender
densenet201 -> edad