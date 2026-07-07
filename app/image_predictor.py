"""
=========================================
Image Predictor
AI Diet Recommendation System
=========================================
"""

import numpy as np

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.efficientnet import preprocess_input


class ImagePredictor:

    def __init__(self, model_path, class_names):
        """
        Load trained AI model
        """

        self.model = load_model(model_path)
        self.class_names = class_names

        print("✅ Food Classification Model Loaded Successfully!")

    def predict(self, image_path):
        """
        Predict food from image
        """

        # Load image
        img = image.load_img(
            image_path,
            target_size=(224, 224)
        )

        # Convert to array
        img_array = image.img_to_array(img)

        # Add batch dimension
        img_array = np.expand_dims(img_array, axis=0)

        # EfficientNet preprocessing
        img_array = preprocess_input(img_array)

        # Predict
        prediction = self.model.predict(
            img_array,
            verbose=0
        )[0]

        # Best prediction
        predicted_index = np.argmax(prediction)

        predicted_food = self.class_names[predicted_index]

        confidence = float(prediction[predicted_index])

        return {

            "food": predicted_food,

            "confidence": confidence

        }