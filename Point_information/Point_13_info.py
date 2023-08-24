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
        "Original_Content_Url": "https://i.imgur.com/oWCqMfQ.png",
        "Preview_Image_Url": "https://i.imgur.com/oWCqMfQ.png",
    },
    "區域位置圖": {
        "Original_Content_Url": "https://i.imgur.com/12bY01b.png",
        "Preview_Image_Url": "https://i.imgur.com/l8VRMdm.png",
    },
}

# ====================================================================
# ImageMap message Information
# Define the URLs, text, and area for each action in the ImageMap
image_map_data = {
    "導覽資訊": {
        "baseUrl": "https://i.imgur.com/qVg31BV.png",
        "altText": "請給我住戶組成複雜（Point_13）資訊圖",
        "baseSize": BaseSize(height=2380, width=1040),
        "actions": [
            {
                "text": "請給我請給我住戶組成複雜（Point_13）的細部放大圖",
                "area": ImagemapArea(x=86, y=213, width=453, height=273),
            },
            {
                "text": "請給我請給我住戶組成複雜（Point_13）的區域位置圖",
                "area": ImagemapArea(x=596, y=213, width=365, height=185),
            },
            {
                "text": "請給我請給我住戶組成複雜（Point_13）的實景圖",
                "area": ImagemapArea(x=86, y=579, width=453, height=284),
            },
            {
                "text": "請給我請給我住戶組成複雜（Point_13）的景點介紹",
                "area": ImagemapArea(x=71, y=1060, width=900, height=406),
            },
            {
                "text": "請給我住戶組成複雜（Point_13）往天生的建築師（Point_11）的路線",
                "area": ImagemapArea(x=459, y=1696, width=508, height=234),
            },
            {
                "text": "請給我住戶組成複雜（Point_13）往家庭代工（Point_14）的路線",
                "area": ImagemapArea(x=456, y=1976, width=508, height=234),
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
            "image_url": "https://i.imgur.com/y5IVnEm.jpg",
            "label": "實景圖 1",
            "data": "1",
        },
        "2": {
            "image_url": "https://i.imgur.com/m63botE.jpg",
            "label": "實景圖 2",
            "data": "2",
        },
        "3": {
            "image_url": "https://i.imgur.com/Y14gtRc.jpg",
            "label": "實景圖 3",
            "data": "3",
        },
        "4": {
            "image_url": "https://i.imgur.com/Q1sITui.jpg",
            "label": "實景圖 4",
            "data": "4",
        },
        "5": {
            "image_url": "https://i.imgur.com/2J8iR3s.jpg",
            "label": "實景圖 5",
            "data": "5",
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
    "前往_Point_14": {
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
        TextSendMessage("Point_13，第1段"),
        TextSendMessage("Point_13，第2段"),
        ImageSendMessage(
            original_content_url="https://i.imgur.com/Q1sITui.jpg",
            preview_image_url="https://i.imgur.com/Q1sITui.jpg",
        ),
        TextSendMessage("Point_13，第3段"),
        TextSendMessage("Point_13，第4段"),
    ],
    "導航": [
        TextSendMessage("https://www.google.com/maps"),
    ],
}

# ====================================================================
# Confirm Template information
confirm_template_data = {
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
    "確認是否抵達_Point_14": {
        "alt_text": "是否抵達家庭代工（Point_14）?",
        "text": "是否抵達家庭代工（Point_14）?",
        "actions": {
            "message": {
                "label": "抵達",
                "text": "順利抵達，請給我家庭代工（Point_14）的導覽資訊",
            },
            "url": {
                "label": "導航",
                "url": "https://www.google.com/maps",
            },
        },
    },
}
