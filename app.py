import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Tiêu đề ứng dụng
st.title("QUẢN LÝ ĐIỂM SINH VIÊN")

# Tạo dữ liệu mẫu 10 sinh viên
np.random.seed(42)
data = {
    'Họ và tên': ['An', 'Bình', 'Chi', 'Dũng', 'Hà', 'Lan', 'Minh', 'Nam', 'Phúc', 'Trang'],
    'Chuyên cần': [8, 9, 7, 9, 8, 7, 9, 8, 8, 9],
    'Giữa kỳ': [7, 8, 6, 9, 7, 6, 8, 7, 8, 9],
    'Cuối kỳ': [7.5, 8.5, 6.0, 9.0, 7.0, 5.5, 8.0, 7.0, 7.5, 9.0]
}
df = pd.DataFrame(data)

# Tính điểm tổng kết và xếp loại
df['Tong_ket'] = (0.2 * df['Chuyên cần'] + 0.3 * df['Giữa kỳ'] + 0.5 * df['Cuối kỳ']).round(2)

def xeploai(diem):
    if diem >= 8.5: return 'Giỏi'
    elif diem >= 7.0: return 'Khá'
    elif diem >= 5.0: return 'Trung bình'
    else: return 'Yếu'

df['Xep_loai'] = df['Tong_ket'].apply(xeploai)

# 1. Hiển thị bảng điểm
st.subheader("📋 Bảng điểm chi tiết của 10 sinh viên")
st.dataframe(df)

# 2. Thống kê
st.subheader("📊 Thống kê chung của lớp")
diem_tb_lop = df['Tong_ket'].mean()
sv_max = df.loc[df['Tong_ket'].idxmax()]['Họ và tên']
diem_max = df['Tong_ket'].max()
sv_min = df.loc[df['Tong_ket'].idxmin()]['Họ và tên']
diem_min = df['Tong_ket'].min()
so_sv_dat = len(df[df['Tong_ket'] >= 5.0])

col1, col2 = st.columns(2)
with col1:
    st.metric(label="Điểm TB của lớp", value=f"{diem_tb_lop:.2f}")
    st.metric(label="Số sinh viên đạt (>= 5.0)", value=so_sv_dat)
with col2:
    st.metric(label="SV điểm cao nhất", value=f"{sv_max} ({diem_max} điểm)")
    st.metric(label="SV điểm thấp nhất", value=f"{sv_min} ({diem_min} điểm)")

# 3. Danh sách xổ xuống chọn sinh viên
st.subheader("🔍 Tra cứu thông tin từng sinh viên")
selected_student = st.selectbox("Chọn tên sinh viên:", df['Họ và tên'])
student_info = df[df['Họ và tên'] == selected_student].iloc[0]

st.write(f"- *Điểm Chuyên cần:* {student_info['Chuyên cần']}")
st.write(f"- *Điểm Giữa kỳ:* {student_info['Giữa kỳ']}")
st.write(f"- *Điểm Cuối kỳ:* {student_info['Cuối kỳ']}")
st.write(f"- *Điểm tổng kết:* {student_info['Tong_ket']}")
st.write(f"- *Xếp loại:* {student_info['Xep_loai']}")

# 4. Biểu đồ
st.subheader("📈 Biểu đồ cột thể hiện điểm tổng kết")
fig, ax = plt.subplots(figsize=(8, 4))
ax.barh(df['Họ và tên'], df['Tong_ket'], color='skyblue')
ax.set_xlabel('Điểm tổng kết')
ax.set_ylabel('Tên sinh viên')
ax.set_title('Biểu đồ điểm tổng kết 10 sinh viên')
ax.set_xlim(0, 10)
st.pyplot(fig)

# 5. Tên và MSSV ở cuối trang
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray; font-size: 12px;'>Người tạo ứng dụng: [Đỗ Huy Cường] - [05]</p>", unsafe_allow_html=True)
