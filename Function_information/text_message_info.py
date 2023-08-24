# Import necessary modules containing text message data
from Point_information import (
    Point_01_info,
    Point_04_info,
    Point_05_info,
    Point_06_info,
    Point_07_info,
    Point_11_info,
    Point_13_info,
    Point_14_info,
    Point_16_info,
    Point_18_info,
    Point_20_info,
    Point_21_info,
    Point_22_info,
    Point_24_info,
    Point_25_info,
)


# Function to select text message data based on point_number and keyword
def select_text_message_info(point_number, keyword):
    # Use the match statement to determine the point_number and retrieve the data accordingly
    match point_number:
        # If the point_number is Point_01_info
        case "Point_01":
            text_message = Point_01_info.text_data[keyword]
        # If the point_number is Point_04_info
        case "Point_04":
            text_message = Point_04_info.text_data[keyword]
        # If the point_number is Point_05_info
        case "Point_05":
            text_message = Point_05_info.text_data[keyword]
        # If the point_number is Point_06_info
        case "Point_06":
            text_message = Point_06_info.text_data[keyword]
        # If the point_number is Point_07_info
        case "Point_07":
            text_message = Point_07_info.text_data[keyword]
        # If the point_number is Point_11_info
        case "Point_11":
            text_message = Point_11_info.text_data[keyword]
        # If the point_number is Point_13_info
        case "Point_13":
            text_message = Point_13_info.text_data[keyword]
        # If the point_number is Point_14_info
        case "Point_14":
            text_message = Point_14_info.text_data[keyword]
        # If the point_number is Point_16_info
        case "Point_16":
            text_message = Point_16_info.text_data[keyword]
        # If the point_number is Point_18_info
        case "Point_18":
            text_message = Point_18_info.text_data[keyword]
        # If the point_number is Point_20_info
        case "Point_20":
            text_message = Point_20_info.text_data[keyword]
        # If the point_number is Point_21_info
        case "Point_21":
            text_message = Point_21_info.text_data[keyword]
        # If the point_number is Point_22_info
        case "Point_22":
            text_message = Point_22_info.text_data[keyword]
        # If the point_number is Point_24_info
        case "Point_24":
            text_message = Point_24_info.text_data[keyword]
        # If the point_number is Point_25_info
        case "Point_25":
            text_message = Point_25_info.text_data[keyword]

    # Return the retrieved text message
    return text_message  # Return the retrieved text message based on the point_number and keyword
