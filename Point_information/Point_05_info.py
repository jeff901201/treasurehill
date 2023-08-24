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
        "Original_Content_Url": "https://i.imgur.com/RYrqi6D.png",
        "Preview_Image_Url": "https://i.imgur.com/RYrqi6D.png",
    },
    "區域位置圖": {
        "Original_Content_Url": "https://i.imgur.com/KkA22Uj.png",
        "Preview_Image_Url": "https://i.imgur.com/GEuTlUe.png",
    },
}

# ====================================================================
# ImageMap message Information
# Define the URLs, text, and area for each action in the ImageMap
image_map_data = {
    "導覽資訊": {
        "baseUrl": "https://i.imgur.com/LUOj91z.png",
        "altText": "歷史遺址（Point_05）資訊圖",
        "baseSize": BaseSize(height=2670, width=1040),
        "actions": [
            {
                "text": "請給我歷史遺址（Point_05）的細部放大圖",
                "area": ImagemapArea(x=86, y=213, width=453, height=273),
            },
            {
                "text": "請給我歷史遺址（Point_05）的區域位置圖",
                "area": ImagemapArea(x=596, y=213, width=365, height=185),
            },
            {
                "text": "請給我歷史遺址（Point_05）的實景圖",
                "area": ImagemapArea(x=86, y=579, width=453, height=284),
            },
            {
                "text": "請給我歷史遺址（Point_05）的景點介紹",
                "area": ImagemapArea(x=71, y=1060, width=900, height=406),
            },
            {
                "text": "請給我歷史遺址（Point_05）往信箱牆（Point_04）的路線",
                "area": ImagemapArea(x=459, y=1699, width=508, height=234),
            },
            {
                "text": "請給我歷史遺址（Point_05）往沿路出現的卵石砌（Point_06）的路線",
                "area": ImagemapArea(x=458, y=1981, width=508, height=234),
            },
            {
                "text": "請給我歷史遺址（Point_05）往上校的家（Point_20）的路線",
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
            "image_url": "https://i.imgur.com/5BxYry1.jpg",
            "label": "實景圖 1",
            "data": "1",
        },
        "2": {
            "image_url": "https://i.imgur.com/E1uDWI7.jpg",
            "label": "實景圖 2",
            "data": "2",
        },
        "3": {
            "image_url": "https://i.imgur.com/A3vMvxI.jpg",
            "label": "實景圖 3",
            "data": "3",
        },
        "4": {
            "image_url": "https://i.imgur.com/X4Z56iz.jpg",
            "label": "實景圖 4",
            "data": "4",
        },
        "5": {
            "image_url": "https://i.imgur.com/j8hhtzE.jpg",
            "label": "實景圖 5",
            "data": "5",
        },
    },
    "前往_Point_04": {
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
    "前往_Point_06": {
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
    "前往_Point_20": {
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
        TextSendMessage("Point_05，第1段"),
        TextSendMessage("Point_05，第2段"),
        ImageSendMessage(
            original_content_url="https://i.imgur.com/5BxYry1.jpg",
            preview_image_url="https://i.imgur.com/5BxYry1.jpg",
        ),
        TextSendMessage("Point_05，第3段"),
        TextSendMessage("Point_05，第4段"),
    ],
    "導航": [
        TextSendMessage("https://www.google.com/maps"),
    ],
}

# ====================================================================
# Confirm Template information
confirm_template_data = {
    "確認是否抵達_Point_04": {
        "alt_text": "是否抵達信箱牆（Point_04）?",
        "text": "是否抵達信箱牆（Point_04）?",
        "actions": {
            "message": {
                "label": "抵達",
                "text": "順利抵達，請給我信箱牆（Point_04）的導覽資訊",
            },
            "url": {
                "label": "導航",
                "url": "https://www.google.com/maps",
            },
        },
    },
    "確認是否抵達_Point_06": {
        "alt_text": "是否抵達沿路出現的卵石砌（Point_06）?",
        "text": "是否抵達沿路出現的卵石砌（Point_06）?",
        "actions": {
            "message": {
                "label": "抵達",
                "text": "順利抵達，請給我沿路出現的卵石砌（Point_06）的導覽資訊",
            },
            "url": {
                "label": "導航",
                "url": "https://www.google.com/maps",
            },
        },
    },
    "確認是否抵達_Point_20": {
        "alt_text": "是否抵達上校的家（Point_20）?",
        "text": "是否抵達上校的家（Point_20）?",
        "actions": {
            "message": {
                "label": "抵達",
                "text": "順利抵達，請給我上校的家（Point_20）的導覽資訊",
            },
            "url": {
                "label": "導航",
                "url": "https://www.google.com/maps",
            },
        },
    },
}
