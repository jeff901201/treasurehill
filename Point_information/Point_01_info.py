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
        "Original_Content_Url": "https://i.imgur.com/3Jv45rY.png",
        "Preview_Image_Url": "https://i.imgur.com/3Jv45rY.png",
    },
    "區域位置圖": {
        "Original_Content_Url": "https://i.imgur.com/gDIZtT1.png",
        "Preview_Image_Url": "https://i.imgur.com/y9OkW7f.png",
    },
}

# ====================================================================
# ImageMap message Information
# Define the URLs, text, and area for each action in the ImageMap
image_map_data = {
    "導覽資訊": {
        "baseUrl": "https://i.imgur.com/iFDwNMz.png",
        "altText": "寶藏巖寺（Point_01）導覽資訊",
        "baseSize": BaseSize(height=2055, width=1040),
        "actions": [
            {
                "text": "請給我寶藏巖寺（Point_01）的細部放大圖",
                "area": ImagemapArea(x=86, y=213, width=453, height=273),
            },
            {
                "text": "請給我寶藏巖寺（Point_01）的區域位置圖",
                "area": ImagemapArea(x=596, y=213, width=365, height=185),
            },
            {
                "text": "請給我寶藏巖寺（Point_01）的實景圖",
                "area": ImagemapArea(x=86, y=579, width=453, height=284),
            },
            {
                "text": "請給我寶藏巖寺（Point_01）的景點介紹",
                "area": ImagemapArea(x=71, y=1060, width=900, height=406),
            },
            {
                "text": "請給我寶藏巖寺（Point_01）往信箱牆（Point_04）的路線",
                "area": ImagemapArea(x=459, y=1673, width=508, height=234),
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
            "image_url": "https://i.imgur.com/yaMGjdJ.jpg",
            "label": "實景圖 1",
            "data": "1",
        },
        "2": {
            "image_url": "https://i.imgur.com/cPry8n8.jpg",
            "label": "實景圖 2",
            "data": "2",
        },
        "3": {
            "image_url": "https://i.imgur.com/CRJNciN.jpg",
            "label": "實景圖 3",
            "data": "3",
        },
        "4": {
            "image_url": "https://i.imgur.com/Ip7kSx6.jpg",
            "label": "實景圖 4",
            "data": "4",
        },
        "5": {
            "image_url": "https://i.imgur.com/2AJ4c9q.jpg",
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
}

# ====================================================================
# Reply Message Information
text_data = {
    "景點介紹": [
        TextSendMessage(
            "寶藏巖位於台灣台北市中正區，是一座古老的佛教山寺，也是台北市定古蹟。除了有著著名的寶藏巖寺外，附近的違章建築形成了一個名為寶藏巖歷史聚落的古老社區，同樣被列為台北市定歷史建築。該地區擁有傍水山坡、漳泉廟宇和眷村等特殊景觀，與周圍的交通設施相結合，形成古今交融的景象。"
        ),
        TextSendMessage(
            "自1997年後，寶藏巖受到台灣學者和民眾的關注，並經過整修和媒體報導後，被列為台北市最具特色的景點之一，與台北101大樓齊名。該地歷史可以追溯到17世紀末，當時移民者郭治亨及其子在這裡建造了寺廟。寶藏巖作為主祀觀音的山寺，也被稱為「觀音亭」，是泉州安溪人的信仰中心。"
        ),
        ImageSendMessage(
            original_content_url="https://i.imgur.com/2AJ4c9q.jpg",
            preview_image_url="https://i.imgur.com/2AJ4c9q.jpg",
        ),
        TextSendMessage(
            "寶藏巖寺經歷多次整修後，仍保留著清朝特有的建築結構、石柱和石窗。1930年代中期，日軍增設了高炮部隊並興建了碉堡和兵舍。1945年後，台灣由國府統治，日治時期的軍事建築多被改建成機關辦公廳舍。1950年代，寶藏巖成為台北北區司令部的重要地點。從1960年代開始，居民在寶藏巖附近興建違建，人口逐漸增加，到1980年代已有約200多戶人家。"
        ),
        TextSendMessage("然而，1980年代時，台北市政府計劃拆除整個寶藏巖社區，引發居民的抗議。最終，寶藏巖被認定為歷史建築，並完成了所有遷村計劃，成為一個被保護的地方。"),
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
}
