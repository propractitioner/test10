import streamlit as st
import requests
import matplotlib.pyplot as plt
from datetime import datetime
from io import BytesIO

# 별자리 API를 호출하여 별자리 데이터를 가져오는 함수
def get_constellation_data(lat, lon):
    api_url = "https://api.nasa.gov/planetary/star_chart"
    params = {
        'lat': lat,
        'lon': lon,
        'date': datetime.now().strftime('%Y-%m-%d'),
        'time': datetime.now().strftime('%H:%M:%S'),
        'api_key': 'DEMO_KEY'  # 여기에 당신의 NASA API 키를 입력하세요.
    }
    response = requests.get(api_url, params=params)
    if response.status_code == 200:
        return response.content
    else:
        st.error("별자리 데이터를 가져오는데 실패했습니다.")
        return None

# 도시와 좌표 정보
cities = {
    "서울": (37.5665, 126.9780),
    "부산": (35.1796, 129.0756),
    "도쿄": (35.6895, 139.6917),
    "오사카": (34.6937, 135.5023),
    "후쿠오카": (33.5904, 130.4017)
}

# Streamlit 인터페이스
st.title("오늘 밤의 별자리")
city = st.selectbox("도시를 선택하세요", list(cities.keys()))

if city:
    lat, lon = cities[city]
    st.write(f"선택된 도시: {city}, 위도: {lat}, 경도: {lon}")
    
    # 별자리 데이터 가져오기
    constellation_data = get_constellation_data(lat, lon)
    
    if constellation_data:
        try:
            st.image(BytesIO(constellation_data), caption=f"{city}의 밤하늘 별자리")
        except Exception as e:
            st.error(f"이미지를 불러오는 중 오류가 발생했습니다: {e}")
    else:
        st.error("별자리 데이터를 가져올 수 없습니다.")
