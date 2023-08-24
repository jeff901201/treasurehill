# Import necessary modules containing image message data
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
    RichMenue_info,
)


# Function to select image message URLs based on point_number and keyword
def select_image_message_info(point_number, keyword):
    # Use the match statement to determine the point_number and retrieve the URLs accordingly
    match point_number:
        # If the point_number is RichMenue_info
        case "RichMenue":
            # Retrieve the URLs from the RichMenue_info module
            image_message_info = RichMenue_info.image_message_info[keyword]
        # If the point_number is Point_01_info
        case "Point_01":
            # Retrieve the URLs from the Point_01_info module
            image_message_info = Point_01_info.image_message_info[keyword]
        # If the point_number is Point_04_info
        case "Point_04":
            # Retrieve the URLs from the Point_04_info module
            image_message_info = Point_04_info.image_message_info[keyword]
        # If the point_number is Point_05_info
        case "Point_05":
            # Retrieve the URLs from the Point_05_info module
            image_message_info = Point_05_info.image_message_info[keyword]
        # If the point_number is Point_06_info
        case "Point_06":
            # Retrieve the URLs from the Point_06_info module
            image_message_info = Point_06_info.image_message_info[keyword]
        # If the point_number is Point_07_info
        case "Point_07":
            # Retrieve the URLs from the Point_07_info module
            image_message_info = Point_07_info.image_message_info[keyword]
        # If the point_number is Point_11_info
        case "Point_11":
            # Retrieve the URLs from the Point_11_info module
            image_message_info = Point_11_info.image_message_info[keyword]
        # If the point_number is Point_13_info
        case "Point_13":
            # Retrieve the URLs from the Point_13_info module
            image_message_info = Point_13_info.image_message_info[keyword]
        # If the point_number is Point_14_info
        case "Point_14":
            # Retrieve the URLs from the Point_14_info module
            image_message_info = Point_14_info.image_message_info[keyword]
        # If the point_number is Point_16_info
        case "Point_16":
            # Retrieve the URLs from the Point_16_info module
            image_message_info = Point_16_info.image_message_info[keyword]
        # If the point_number is Point_18_info
        case "Point_18":
            # Retrieve the URLs from the Point_18_info module
            image_message_info = Point_18_info.image_message_info[keyword]
        # If the point_number is Point_20_info
        case "Point_20":
            # Retrieve the URLs from the Point_20_info module
            image_message_info = Point_20_info.image_message_info[keyword]
        # If the point_number is Point_21_info
        case "Point_21":
            # Retrieve the URLs from the Point_21_info module
            image_message_info = Point_21_info.image_message_info[keyword]
        # If the point_number is Point_22_info
        case "Point_22":
            # Retrieve the URLs from the Point_22_info module
            image_message_info = Point_22_info.image_message_info[keyword]
        # If the point_number is Point_24_info
        case "Point_24":
            # Retrieve the URLs from the Point_24_info module
            image_message_info = Point_24_info.image_message_info[keyword]
        # If the point_number is Point_25_info
        case "Point_25":
            # Retrieve the URLs from the Point_25_info module
            image_message_info = Point_25_info.image_message_info[keyword]

    return image_message_info  # Return the dictionary containing the image message URLs
