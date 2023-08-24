from linebot.models import (
    BaseSize,
    ImagemapArea,
    ImageSendMessage,
    TextSendMessage,
)

# ====================================================================
# Image message Information
# Define the URLs for the image content and preview for each keyword
image_message_info = {
    "細部放大圖": {
        "Original_Content_Url": "https://i.imgur.com/Wim0N7S.png",
        "Preview_Image_Url": "https://i.imgur.com/Wim0N7S.png",
    },
    "區域位置圖": {
        "Original_Content_Url": "https://i.imgur.com/jE8qulW.png",
        "Preview_Image_Url": "https://i.imgur.com/bqwSJFC.png",
    },
}

# ====================================================================
# ImageMap message Information
# Define the URLs, text, and area for each action in the ImageMap
image_map_data = {
    "導覽資訊": {
        "baseUrl": "https://i.imgur.com/EZfvhq8.png",
        "altText": "歷史斷面（Point_25）資訊圖",
        "baseSize": BaseSize(height=2670, width=1040),
        "actions": [
            {
                "text": "請給我歷史斷面（Point_25）的細部放大圖",
                "area": ImagemapArea(x=86, y=213, width=453, height=273),
            },
            {
                "text": "請給我歷史斷面（Point_25）的區域位置圖",
                "area": ImagemapArea(x=596, y=213, width=365, height=185),
            },
            {
                "text": "請給我歷史斷面（Point_25）的實景圖",
                "area": ImagemapArea(x=86, y=579, width=453, height=284),
            },
            {
                "text": "請給我歷史斷面（Point_25）的景點介紹",
                "area": ImagemapArea(x=71, y=1060, width=900, height=406),
            },
            {
                "text": "請給我歷史斷面（Point_25）往寶藏巖寺（Point_01）的路線",
                "area": ImagemapArea(x=459, y=1699, width=508, height=234),
            },
            {
                "text": "請給我歷史斷面（Point_25）往寶村柑仔店（Point_22）的路線",
                "area": ImagemapArea(x=458, y=1981, width=508, height=234),
            },
            {
                "text": "請給我歷史斷面（Point_25）往菜園（Point_24）的路線",
                "area": ImagemapArea(x=458, y=2263, width=508, height=234),
            },
        ],
    },
    # Add more key-value pairs for other ImageMap actions if needed
}

# ====================================================================
# Image Carousel Template Information
# Define image information and actions for the Image Carousel
image_carousel_data = {
    "實景圖": {
        "1": {
            "image_url": "https://i.imgur.com/k4drBKq.jpg",
            "label": "實景圖 1",
            "data": "1",
        },
        "2": {
            "image_url": "https://i.imgur.com/SaHpTRx.jpg",
            "label": "實景圖 2",
            "data": "2",
        },
        "3": {
            "image_url": "https://i.imgur.com/8djsDes.jpg",
            "label": "實景圖 3",
            "data": "3",
        },
        "4": {
            "image_url": "https://i.imgur.com/Sxqt25r.jpg",
            "label": "實景圖 4",
            "data": "4",
        },
        "5": {
            "image_url": "https://i.imgur.com/IhZiby4.jpg",
            "label": "實景圖 5",
            "data": "5",
        },
    },
    "前往_Point_01": {
        "1": {
            "image_url": "https://i.imgur.com/42mnxvk.jpg",
            "label": "step1點擊看文字說明",
            "data": "往前直走",
        },
        "2": {
            "image_url": "https://i.imgur.com/nINeAma.jpg",
            "label": "step2點擊看文字說明",
            "data": "往左走進入寶藏巖入口",
        },
        "3": {
            "image_url": "https://i.imgur.com/wHYKyEi.jpg",
            "label": "step3點擊看文字說明",
            "data": "進入寶藏巖入口後左轉抵達信箱牆",
        },
    },
    "前往_Point_22": {
        "1": {
            "image_url": "https://i.imgur.com/42mnxvk.jpg",
            "label": "step1點擊看文字說明",
            "data": "往前直走",
        },
        "2": {
            "image_url": "https://i.imgur.com/nINeAma.jpg",
            "label": "step2點擊看文字說明",
            "data": "往左走進入寶藏巖入口",
        },
        "3": {
            "image_url": "https://i.imgur.com/wHYKyEi.jpg",
            "label": "step3點擊看文字說明",
            "data": "進入寶藏巖入口後左轉抵達信箱牆",
        },
    },
    "前往_Point_24": {
        "1": {
            "image_url": "https://i.imgur.com/42mnxvk.jpg",
            "label": "step1點擊看文字說明",
            "data": "往前直走",
        },
        "2": {
            "image_url": "https://i.imgur.com/nINeAma.jpg",
            "label": "step2點擊看文字說明",
            "data": "往左走進入寶藏巖入口",
        },
        "3": {
            "image_url": "https://i.imgur.com/wHYKyEi.jpg",
            "label": "step3點擊看文字說明",
            "data": "進入寶藏巖入口後左轉抵達信箱牆",
        },
    },
}

# ====================================================================
# Reply Message Information
text_data = {
    "景點介紹": [
        TextSendMessage("Point_25，第1段"),
        TextSendMessage("Point_25，第2段"),
        ImageSendMessage(
            original_content_url="https://i.imgur.com/Sxqt25r.jpg",
            preview_image_url="https://i.imgur.com/Sxqt25r.jpg",
        ),
        TextSendMessage("Point_25，第3段"),
        TextSendMessage("Point_25，第4段"),
    ],
    "導航": [
        TextSendMessage("https://www.google.com/maps"),
    ],
}

# ====================================================================
# Confirm Template information
confirm_template_data = {
    "確認是否抵達_Point_01": {
        "alt_text": "是否抵達寶藏巖寺（Point_01）?",
        "text": "是否抵達寶藏巖寺（Point_01）?",
        "actions": {
            "message": {
                "label": "抵達",
                "text": "順利抵達，請給我寶藏巖寺（Point_01）的導覽資訊",
            },
            "url": {
                "label": "導航",
                "url": "https://www.google.com/maps",
            },
        },
    },
    "確認是否抵達_Point_22": {
        "alt_text": "是否抵達寶村柑仔店（Point_22）?",
        "text": "是否抵達寶村柑仔店（Point_22）?",
        "actions": {
            "message": {
                "label": "抵達",
                "text": "順利抵達，請給我寶村柑仔店（Point_22）的導覽資訊",
            },
            "url": {
                "label": "導航",
                "url": "https://www.google.com/maps",
            },
        },
    },
    "確認是否抵達_Point_24": {
        "alt_text": "是否抵達菜園（Point_24）?",
        "text": "是否抵達菜園（Point_24）?",
        "actions": {
            "message": {
                "label": "抵達",
                "text": "順利抵達，請給我菜園（Point_24）的導覽資訊",
            },
            "url": {
                "label": "導航",
                "url": "https://www.google.com/maps",
            },
        },
    },
}
