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
        "Original_Content_Url": "https://i.imgur.com/29gFDrl.png",
        "Preview_Image_Url": "https://i.imgur.com/29gFDrl.png",
    },
    "區域位置圖": {
        "Original_Content_Url": "https://i.imgur.com/zxU3njz.png",
        "Preview_Image_Url": "https://i.imgur.com/iGBjoRz.png",
    },
}

# ====================================================================
# ImageMap message Information
# Define the URLs, text, and area for each action in the ImageMap
image_map_data = {
    "導覽資訊": {
        "baseUrl": "https://i.imgur.com/FpGVvwW.png",
        "altText": "波羅蜜大樹（Point_18）資訊圖",
        "baseSize": BaseSize(height=2670, width=1040),
        "actions": [
            {
                "text": "請給我波羅蜜大樹（Point_18）的細部放大圖",
                "area": ImagemapArea(x=86, y=213, width=453, height=273),
            },
            {
                "text": "請給我波羅蜜大樹（Point_18）的區域位置圖",
                "area": ImagemapArea(x=596, y=213, width=365, height=185),
            },
            {
                "text": "請給我波羅蜜大樹（Point_18）的實景圖",
                "area": ImagemapArea(x=86, y=579, width=453, height=284),
            },
            {
                "text": "請給我波羅蜜大樹（Point_18）的景點介紹",
                "area": ImagemapArea(x=71, y=1060, width=900, height=406),
            },
            {
                "text": "請給我波羅蜜大樹（Point_18）往擁擠的住所（Point_07）的路線",
                "area": ImagemapArea(x=459, y=1699, width=508, height=234),
            },
            {
                "text": "請給我波羅蜜大樹（Point_18）往天生的建築師（Point_11）的路線",
                "area": ImagemapArea(x=458, y=1981, width=508, height=234),
            },
            {
                "text": "請給我波羅蜜大樹（Point_18）往大時代，小人物（Point_16）的路線",
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
            "image_url": "https://i.imgur.com/A8I9vhT.jpg",
            "label": "實景圖 1",
            "data": "1",
        },
        "2": {
            "image_url": "https://i.imgur.com/lTJ8dxy.jpg",
            "label": "實景圖 2",
            "data": "2",
        },
        "3": {
            "image_url": "https://i.imgur.com/2yXijAV.jpg",
            "label": "實景圖 3",
            "data": "3",
        },
        "4": {
            "image_url": "https://i.imgur.com/bzYs7TE.jpg",
            "label": "實景圖 4",
            "data": "4",
        },
        "5": {
            "image_url": "https://i.imgur.com/UhZNZdt.png",
            "label": "實景圖 5",
            "data": "5",
        },
    },
    "前往_Point_07": {
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
    "前往_Point_11": {
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
    "前往_Point_16": {
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
        TextSendMessage("Point_18，第1段"),
        TextSendMessage("Point_18，第2段"),
        ImageSendMessage(
            original_content_url="https://i.imgur.com/A8I9vhT.jpg",
            preview_image_url="https://i.imgur.com/A8I9vhT.jpg",
        ),
        TextSendMessage("Point_18，第3段"),
        TextSendMessage("Point_18，第4段"),
    ],
    "導航": [
        TextSendMessage("https://www.google.com/maps"),
    ],
}

# ====================================================================
# Confirm Template information
confirm_template_data = {
    "確認是否抵達_Point_07": {
        "alt_text": "是否抵達擁擠的住所（Point_07）?",
        "text": "是否抵達擁擠的住所（Point_07）?",
        "actions": {
            "message": {
                "label": "抵達",
                "text": "順利抵達，請給我擁擠的住所（Point_07）的導覽資訊",
            },
            "url": {
                "label": "導航",
                "url": "https://www.google.com/maps",
            },
        },
    },
    "確認是否抵達_Point_11": {
        "alt_text": "是否抵達天生的建築師（Point_11）?",
        "text": "是否抵達天生的建築師（Point_11）?",
        "actions": {
            "message": {
                "label": "抵達",
                "text": "順利抵達，請給我天生的建築師（Point_11）的導覽資訊",
            },
            "url": {
                "label": "導航",
                "url": "https://www.google.com/maps",
            },
        },
    },
    "確認是否抵達_Point_16": {
        "alt_text": "是否抵達大時代，小人物（Point_16）?",
        "text": "是否抵達大時代，小人物（Point_16）?",
        "actions": {
            "message": {
                "label": "抵達",
                "text": "順利抵達，請給我大時代，小人物（Point_16）的導覽資訊",
            },
            "url": {
                "label": "導航",
                "url": "https://www.google.com/maps",
            },
        },
    },
}
