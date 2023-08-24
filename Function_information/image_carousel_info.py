# Import necessary modules containing image carousel data
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


# Function to select image carousel data based on point_number and keyword
def select_image_carousel_info(point_number, keyword):
    # Use the match statement to determine the point_number and retrieve the data accordingly
    match point_number:
        # If the point_number is "Point_01"
        case "Point_01":
            # Retrieve the image carousel data from the Point_01_info module
            image_carousel_data = Point_01_info.image_carousel_data[keyword]
        # If the point_number is "Point_04"
        case "Point_04":
            # Retrieve the image carousel data from the Point_04_info module
            image_carousel_data = Point_04_info.image_carousel_data[keyword]
        # If the point_number is "Point_05"
        case "Point_05":
            # Retrieve the image carousel data from the Point_05_info module
            image_carousel_data = Point_05_info.image_carousel_data[keyword]
        # If the point_number is "Point_06"
        case "Point_06":
            # Retrieve the image carousel data from the Point_06_info module
            image_carousel_data = Point_06_info.image_carousel_data[keyword]
        # If the point_number is "Point_07"
        case "Point_07":
            # Retrieve the image carousel data from the Point_07_info module
            image_carousel_data = Point_07_info.image_carousel_data[keyword]
        # If the point_number is "Point_11"
        case "Point_11":
            # Retrieve the image carousel data from the Point_11_info module
            image_carousel_data = Point_11_info.image_carousel_data[keyword]
        # If the point_number is "Point_13"
        case "Point_13":
            # Retrieve the image carousel data from the Point_13_info module
            image_carousel_data = Point_13_info.image_carousel_data[keyword]
        # If the point_number is "Point_14"
        case "Point_14":
            # Retrieve the image carousel data from the Point_14_info module
            image_carousel_data = Point_14_info.image_carousel_data[keyword]
        # If the point_number is "Point_16"
        case "Point_16":
            # Retrieve the image carousel data from the Point_16_info module
            image_carousel_data = Point_16_info.image_carousel_data[keyword]
        # If the point_number is "Point_18"
        case "Point_18":
            # Retrieve the image carousel data from the Point_18_info module
            image_carousel_data = Point_18_info.image_carousel_data[keyword]
        # If the point_number is "Point_20"
        case "Point_20":
            # Retrieve the image carousel data from the Point_20_info module
            image_carousel_data = Point_20_info.image_carousel_data[keyword]
        # If the point_number is "Point_21"
        case "Point_21":
            # Retrieve the image carousel data from the Point_21_info module
            image_carousel_data = Point_21_info.image_carousel_data[keyword]
        # If the point_number is "Point_22"
        case "Point_22":
            # Retrieve the image carousel data from the Point_22_info module
            image_carousel_data = Point_22_info.image_carousel_data[keyword]
        # If the point_number is "Point_24"
        case "Point_24":
            # Retrieve the image carousel data from the Point_24_info module
            image_carousel_data = Point_24_info.image_carousel_data[keyword]
        # If the point_number is "Point_25"
        case "Point_25":
            # Retrieve the image carousel data from the Point_25_info module
            image_carousel_data = Point_25_info.image_carousel_data[keyword]

    # Return the retrieved image carousel data
    return image_carousel_data
