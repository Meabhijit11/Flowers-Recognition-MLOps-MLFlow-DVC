import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
# from keras.preprocessing import image
# from keras.models import load_model
import os

class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename

    def predict(self):
        # load model
        model = load_model(os.path.join("model", "model.h5"))

        imagename = self.filename
        test_image = image.load_img(imagename, target_size=(224, 224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        result = np.argmax(model.predict(test_image), axis=1)
        print(result)

        if result[0] == 1:
            prediction = 'daisy'
            return [{"image": prediction}]
        elif result[1] == 2:
            prediction = 'dandelion'
            return [{"image": prediction}]

        elif result[2] == 3:
            prediction = 'rose'
            return [{"image": prediction}]

        elif result[3] == 4:
            prediction = 'sunflower'
            return [{"image": prediction}]

        elif result[4] == 5:
            prediction = 'tulip'
            return [{"image": prediction}]
