import streamlit as st


st.set_page_config('메인 페이지')

ultra_sonic_sensor_img = Image.open('images/ultraSonicSensor.jpg')
servo_motor_img = Image.open('images/servoMotor.jpg')




st.title('아두이노 레이더')


st.header('재료')


st.subheader('초음파 거리 센서')
st.image(ultra_sonic_sensor_img)
st.write('초음파 센서는 약 20kHz이상의 높은 주파수의 소리를 보낸후 반사되어 돌아오는 시간차를 측정해서 거리를 알 수 있는 센서이다.')


st.subheader('서보 모터')
st.image(servo_motor_img)
st.write('서보 모터는 일반 모터와는 다르게 회전이 정해져 있기 때문에 정확한 움직이 필요한 경우에 사용하는 모터이다. 서보 모터란 별도로 존재하는 모터가 아닌 서보라는 기술이 적용되어 사용자가 원하는 각도, 속도로 움직임이 가능한 것이다.')