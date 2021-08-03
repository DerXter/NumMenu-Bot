# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, FollowupAction
from rasa_sdk.executor import CollectingDispatcher

class ActionHandleOptions(Action):

    def name(self) -> Text:
        return "action_handle_options"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        option2action_name =   {1: "action_handle_pytorch",
                                2: "action_handle_tensorflow",
                                3: "action_handle_deeplearning4j",
                                4: "action_handle_cntk",
                                5: "action_handle_keras",
                                6: "action_handle_onnx",
                                7: "action_handle_mxnet",
                                8: "action_handle_caffe"}
        try:
            option = int(tracker.get_slot("option"))
        except ValueError:
            dispatcher.utter_message(text=f"Please enter a number!")
            return [SlotSet('option', None)]
        try:
            next_action = option2action_name[option]
        except KeyError:
            dispatcher.utter_message(text=f"This option is not available!")
            return [SlotSet('option', None)]

        dispatcher.utter_message(text=f"You've choosen option {option} !")

        return [SlotSet('option', None),
                FollowupAction(name=next_action)]

# source of framework descriptions: https://marutitech.com/top-8-deep-learning-frameworks/
class ActionHandlePyTorch(Action):

    def name(self) -> Text:
        return "action_handle_pytorch"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        message = """Torch is a scientific computing framework that offers broad support for machine learning\n
algorithms. It is a Lua based deep learning framework and is used widely amongst industry giants\n
such as Facebook, Twitter, and Google."""
        dispatcher.utter_message(text=message)

        return []

class ActionHandleTensorflow(Action):

    def name(self) -> Text:
        return "action_handle_tensorflow"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        message = """TensorFlow is inarguably one of the most popular deep learning frameworks.\n
Developed by the Google Brain team, TensorFlow supports languages such as Python,\n
C++, and R to create deep learning models along with wrapper libraries.\n
It is available on both desktop and mobile."""
        dispatcher.utter_message(text=message)

        return []

class ActionHandleDeepLearning4J(Action):

    def name(self) -> Text:
        return "action_handle_deeplearning4j"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        message = """The j in Deeplearning4j stands for Java ☕️ Needless to say, it is a deep learning library \n
for the Java Virtual Machine (JVM). It is developed in Java and supports other JVM languages \n
like Scala, Clojure, and Kotlin."""
        dispatcher.utter_message(text=message)

        return []

class ActionHandleCNTK(Action):

    def name(self) -> Text:
        return "action_handle_cntk"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        message = """Popularly known for easy training and a combination of popular model types across servers,\n
the Microsoft Cognitive Toolkit (earlier known as CNTK) is an open-source deep learning\n
framework to train deep learning models. \n
It performs efficient Convolution Neural Networks and training for image, speech, and text-based data."""
        dispatcher.utter_message(text=message)

        return []

class ActionHandleKeras(Action):

    def name(self) -> Text:
        return "action_handle_keras"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        message = """Keras library was developed, keeping quick experimentation as its USP. \n
Written in Python, the Keras neural networks library supports both convolutional and \n
recurrent networks that are capable of running on either TensorFlow or Theano."""
        dispatcher.utter_message(text=message)

        return []

class ActionHandleONNX(Action):

    def name(self) -> Text:
        return "action_handle_onnx"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        message = """ONNX or the Open Neural Network Exchange was developed as an open-source deep learning\n
ecosystem. Developed by Microsoft and Facebook, ONNX proves to be a deep learning framework \n
that enables developers to switch easily between platforms."""
        dispatcher.utter_message(text=message)

        return []

class ActionHandleMXNET(Action):

    def name(self) -> Text:
        return "action_handle_mxnet"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        message = """Designed specifically for high efficiency, productivity, and flexibility, \n
MXNet (pronounced as mix-net) is a deep learning framework that is supported by Python,\n
R, C++, and Julia."""
        dispatcher.utter_message(text=message)

        return []

class ActionHandleCaffe(Action):

    def name(self) -> Text:
        return "action_handle_caffe"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        message = """Well known for its laser-like speed, Caffe is a deep learning framework that is supported\n
with interfaces like C, C++, Python, MATLAB, and Command Line.\n
Its applicability in modeling Convolution Neural Networks (CNN) and its speed has made it popular \n
in recent years."""
        dispatcher.utter_message(text=message)

        return []