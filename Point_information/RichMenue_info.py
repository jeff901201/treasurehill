from linebot.models import (
    BaseSize,
    ImagemapArea,
)

# ====================================================================
# Image message Information
# Define the URLs for the image content and preview for each keyword
image_message_info = {
    "全區地圖": {
        "Original_Content_Url": "https://i.imgur.com/zKFkHNV.jpg",
        "Preview_Image_Url": "https://i.imgur.com/zKFkHNV.jpg",
    },
}

# ====================================================================
# ImageMap message Information
# Define the URLs, text, and area for each action in the ImageMap
image_map_data = {
    "導覽開始": {
        "baseUrl": "https://i.imgur.com/oigXVdH.jpg",
        "altText": "導覽開始資訊圖",
        "baseSize": BaseSize(height=1700, width=1080),
        "actions": [
            {
                "text": "我要從歷史斷面（Point_25）開始，並開啟導覽資訊",
                "area": ImagemapArea(x=189, y=898, width=328, height=321),
            },
            {
                "text": "我要從信箱牆（Point_04）開始，並開啟導覽資訊",
                "area": ImagemapArea(x=590, y=909, width=330, height=309),
            },
            {
                "text": "我要從寶村柑仔店（Point_22）開始，並開啟導覽資訊",
                "area": ImagemapArea(x=184, y=1261, width=334, height=324),
            },
            {
                "text": "我要從寶藏巖寺（Point_01）開始，並開啟導覽資訊",
                "area": ImagemapArea(x=587, y=1274, width=394, height=312),
            },
        ],
    },
    # Add more key-value pairs for other ImageMap actions if needed
}
