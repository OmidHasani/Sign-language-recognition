This project is an intelligent system based on machine learning that can recognize and display various words from sign language using camera images, even in real-time. By leveraging advanced machine learning and computer vision techniques, the system analyzes hand and finger movements and translates them into corresponding words in sign language. The process happens instantaneously, allowing users to see the translation of their gestures displayed on the screen in real-time.

A key feature of this project is the unique dataset, which has been manually and exclusively collected for this purpose. Unlike public datasets that may contain inconsistent or inaccurate samples, this dataset has been carefully selected and created to ensure the highest level of accuracy and efficiency in recognizing sign language gestures. The manual collection means that all gestures were captured with a focus on image quality, viewing angles, and diversity in user movements.

Moreover, the normalization of data has been a crucial part of the system's development. Advanced normalization techniques were applied to standardize the data, enabling the algorithm to more effectively and accurately analyze the differences in hand movements. This step has ensured that the system performs well even under different lighting conditions and angles, reducing recognition errors to a minimum.

Overall, this project stands out due to the integration of advanced machine learning, a custom-built dataset, and cutting-edge normalization methods, making it a powerful tool for assisting the deaf and improving human interactions through sign language. In the future, this system could serve as a platform for the development of other technologies aimed at enhancing human communication and intelligent assistance.

--------------------------------------------------------------------------------------------------------------------------

1.  Using the hand detector library, we processed the hand in real-time by detecting key landmarks on the hand. The system identifies the position of fingers and the palm, allowing us to track hand movements and gestures. We applied image pre-processing techniques, such as resizing and normalization, to enhance the detection accuracy. Additionally, the model outputs precise coordinates of each detected hand landmark, which can then be used for further analysis, such as gesture recognition or interaction with virtual environments.

![Screenshot 2024-10-04 230118](https://github.com/user-attachments/assets/d70401c8-50a8-42d5-a313-b0c9bda1bbd2)

2.  Word recognition is performed using the points received from the hand and the amount of coordinate changes between the points.

![Screenshot 2024-10-04 230145](https://github.com/user-attachments/assets/4565e099-7131-4ac9-be4e-402e2dac6fad)
