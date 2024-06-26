import streamlit as st
import requests
from datetime import datetime
from io import BytesIO
from PIL import Image, UnidentifiedImageError

# APOD API를 호출하여 이미지 데이터를 가져오는 함수
def get_apod_data():
    api_url = "https://api.nasa.gov/planetary/apod"
    params = {
        'api_key': 'DEMO_KEY',  # 여기에 당신의 NASA API 키를 입력하세요.
        'date': datetime.now().strftime('%Y-%m-%d')
    }
    response = requests.get(api_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        st.error("데이터를 가져오는데 실패했습니다.")
        return None

# Streamlit 인터페이스
st.title("오늘의 천문학 사진")

# APOD 데이터 가져오기
apod_data = get_apod_data()

if apod_data and 'url' in apod_data:
    image_url = apod_data['url']
    st.write(f"이미지 URL: {image_url}")
    
    try:
        image_response = requests.get(image_url)
        image = Image.open(BytesIO(image_response.content))
        st.image(image, caption=f"{apod_data.get('title', '천문학 사진')}")
    except UnidentifiedImageError:
        st.error("이미지를 불러오는 중 오류가 발생했습니다. 이미지 파일이 아닙니다.")
    except Exception as e:
        st.error(f"이미지를 불러오는 중 오류가 발생했습니다: {e}")
else:
    st.error("데이터를 가져올 수 없습니다.")
