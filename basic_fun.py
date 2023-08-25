from linebot.models import (
    ConfirmTemplate,
    ImageCarouselColumn,
    ImageCarouselTemplate,
    ImagemapArea,
    ImagemapSendMessage,
    ImageSendMessage,
    MessageAction,
    MessageImagemapAction,
    PostbackAction,
    TemplateSendMessage,
    URIAction,
)

from Function_information import (
    confirm_template_message_info,
    image_carousel_info,
    image_message_info,
    imagemap_info,
    text_message_info,
)

import re


# ====================================================================
# Function to create a list of captured content and keyword using the provided message
def create_point_and_keyword(message):
    # Define patterns with corresponding numbers of capture groups
    patterns = [
        (r"（(.*?)）.*?(區域位置圖|細部放大圖|景點介紹|導航|實景圖)", 2),
        (r"（(.*?)）.*?（(.*?)）.*?(路線)", 3),
        (r".*?（(.*?)）.*?(確認是否抵達)", 2),
        (r".*?（(.*?)）.*?(導覽資訊)", 2),
        (r".*?(寶藏巖).*?(全區地圖|商店資訊|拍照景點|功能介紹|導覽開始)", 2),
    ]

    point_and_keyword = []

    # Iterate through each pattern and corresponding number of groups
    for pattern, groups in patterns:
        match_result = re.search(pattern, message)

        if match_result:
            # Extract capture group values and append to point_and_keyword
            for i in range(1, groups + 1):
                point_and_keyword.append(match_result.group(i))

            # Adjust first value for special case
            if point_and_keyword[0] == "寶藏巖":
                point_and_keyword[0] = "RichMenue"

            function_type = match_result.group(groups)

            # Match function_type to categorize the message
            match function_type:
                case "區域位置圖" | "細部放大圖" | "全區地圖":
                    point_and_keyword.append("Image_Message")
                case "實景圖" | "路線":
                    point_and_keyword.append("Image_Carousel_Template")
                case "景點介紹" | "導航":
                    point_and_keyword.append("Text_Message")
                case "導覽資訊" | "導覽開始":
                    point_and_keyword.append("ImageMap_Message")

    # Check the number of items in point_and_keyword to determine the return format
    if len(point_and_keyword) == 4:
        return [
            point_and_keyword[0],
            "前往_" + point_and_keyword[1],
            "確認是否抵達_" + point_and_keyword[1],
            point_and_keyword[3],
        ]
    else:
        return point_and_keyword


# ====================================================================
# Function to create an ImageSendMessage using the provided point_number and keyword
def create_image_message(point_number, keyword):
    # Get the URLs for the image message from the select_image_message_info function
    image_message_data = image_message_info.select_image_message_info(
        point_number, keyword
    )

    # Create the ImageSendMessage object using the retrieved URLs
    image_message = ImageSendMessage(
        original_content_url=image_message_data["Original_Content_Url"],
        preview_image_url=image_message_data["Preview_Image_Url"],
    )

    return image_message


# ====================================================================
# Function to create an ImagemapSendMessage using the provided point_number and keyword
def create_imagemap_message(point_number, keyword):
    # Get the imagemap data using the select_imagemap_message_info function
    image_map_data = imagemap_info.select_imagemap_message_info(point_number, keyword)

    # Create a list of MessageImagemapAction objects using a list comprehension
    actions = [
        MessageImagemapAction(
            text=action["text"],  # Text shown on the Imagemap action
            area=ImagemapArea(
                x=action["area"].x,  # X-coordinate of the action area
                y=action["area"].y,  # Y-coordinate of the action area
                width=action["area"].width,  # Width of the action area
                height=action["area"].height,  # Height of the action area
            ),
        )
        for action in image_map_data[
            "actions"
        ]  # Iterate through all actions in the Imagemap
    ]

    # Create an ImagemapSendMessage object with the extracted information
    imagemap_message = ImagemapSendMessage(
        base_url=image_map_data["baseUrl"],  # Set the base URL for the Imagemap
        alt_text=image_map_data[
            "altText"
        ],  # Set the alternative text description for the Imagemap
        base_size=image_map_data["baseSize"],  # Set the base size of the Imagemap
        actions=actions,  # Set the list of actions for the Imagemap
    )

    return imagemap_message  # Return the created ImagemapSendMessage object


# ====================================================================
# Function to create an Image Carousel Template message using the provided point_number and keyword
def create_image_carousel_template(point_number, keyword):
    # Get the image carousel data using the select_image_carousel_info function
    image_carousel_data = image_carousel_info.select_image_carousel_info(
        point_number, keyword
    )

    # Create Image Carousel columns
    image_carousel_columns = [
        ImageCarouselColumn(
            image_url=image_carousel_data[key]["image_url"],  # URL of the image
            action=PostbackAction(
                label=image_carousel_data[key]["label"],  # Label displayed on the image
                data=image_carousel_data[key]["data"],  # Data sent when image is tapped
            ),
        )
        for key in image_carousel_data  # Iterate through all keys in the image_carousel_data
    ]

    # Create Image Carousel Template message
    image_carousel_template_message = TemplateSendMessage(
        alt_text=keyword,  # Alternative text for devices that don't support image carousels
        template=ImageCarouselTemplate(
            columns=image_carousel_columns
        ),  # Set the columns for the Image Carousel
    )

    return image_carousel_template_message  # Return the created Image Carousel Template message


# ====================================================================
# Function to create a text message using the provided point_number and keyword
def create_text_message(point_number, keyword):
    # Get the text message data using the select_text_message_info function
    text_message = text_message_info.select_text_message_info(point_number, keyword)

    # Return the text message
    return text_message  # Return the retrieved text message based on the point_number and keyword


# ====================================================================
# Function to create a Confirm Template message using the provided point_number and keyword
def create_confirm_template_message(point_number, keyword):
    # Get the data for Confirm Template message using the select_confirm_template_message_info function
    confirm_template_data = (
        confirm_template_message_info.select_confirm_template_message_info(
            point_number, keyword
        )
    )

    # Create a ConfirmTemplate object with the text and actions defined in the data
    confirm_template_object = ConfirmTemplate(
        text=confirm_template_data["text"],
        actions=[
            # Define a MessageAction with label and text for the action button
            MessageAction(
                label=confirm_template_data["actions"]["message"]["label"],
                text=confirm_template_data["actions"]["message"]["text"],
            ),
            # Define a URIAction with label and URI for the action button
            URIAction(
                label=confirm_template_data["actions"]["url"]["label"],
                uri=confirm_template_data["actions"]["url"]["url"],
            ),
        ],
    )

    # Create the TemplateSendMessage using the ConfirmTemplate and alt_text
    confirm_template_message = TemplateSendMessage(
        alt_text=confirm_template_data[
            "alt_text"
        ],  # Alt text for devices that can't display templates
        template=confirm_template_object,  # Set the created ConfirmTemplate as the content of the TemplateSendMessage
    )

    return confirm_template_message  # Return the created Confirm Template message
