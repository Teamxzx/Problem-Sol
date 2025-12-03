# calculator.py
import streamlit as st

def get_number_input(label):
    return st.number_input(label, value=0.0, step=0.1, format="%.2f")

def get_operator_input(label):
    valid_operators = ['+', '-', '*', '/', '%']
    return st.selectbox(label, valid_operators)

def calculate(num1, num2, operator):
    # ฟังก์ชันคำนวณหลัก
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            st.error("❗ ไม่สามารถหารด้วย 0 ได้")
            return None
        return num1 / num2
    elif operator == '%':
        if num2 == 0:
            st.error("❗ ไม่สามารถหารด้วย 0 ได้")
            return None
        return num1 % num2
    else:
        st.error(" ตัวดำเนินการไม่ถูกต้อง")
        return None


# ส่วนแสดงผล UI
st.title('My Calculator')

num1 = get_number_input("ป้อนตัวเลขแรก:")
num2 = get_number_input("ป้อนตัวเลขที่สอง:")
operator = get_operator_input("เลือกตัวดำเนินการ:")

if st.button('คำนวณ'):
    result = calculate(num1, num2, operator)
    if result is not None:
        st.success(f"ผลลัพธ์: {num1} {operator} {num2} = {result}")
