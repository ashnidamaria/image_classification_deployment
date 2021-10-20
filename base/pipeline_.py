"""
Pipeline script containing the abstract classes for pipeline
"""
from abc import ABC, abstractmethod


class PredictBase(ABC):
    """
    Python class for defining prediction pipeline
    """
    @abstractmethod
    def validate_image(self, json_dict):
        """
        Function to validate the URL
        :return: Image
        """
        pass

    @abstractmethod
    def download_image(self, json_dict):
        """
        Function to download the image from the URL
        :return: Image
        """
        pass

    @abstractmethod
    def preprocess(self, image):
        """
        Function to preprocess the image
        :return: nd array
        """
    @abstractmethod
    def predict(self, image, model):
        """
        Function to predict whether the image is cat or dog
        :return: string
        """

    @abstractmethod
    def run(self, json_dict, model):
        """
        Function to run the pipeline
        :dict json_dict: Input from API endpoint
        :return:
        """
        pass

