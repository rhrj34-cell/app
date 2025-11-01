# Streamlit 라이브러리를 st라는 별칭으로 가져옵니다.
# Streamlit은 웹 앱을 만들기 위한 파이썬 라이브러리입니다.
import streamlit as st

# --- 1. 앱 제목 및 수업 목표 설정 ---

# st.title() 함수를 사용하여 웹 앱의 제목을 설정합니다.
# 이 제목은 가장 큰 글씨체로 화면에 표시됩니다.
st.title("물리학1")

# st.write() 함수를 사용하여 일반 텍스트를 화면에 표시합니다.
# 여기서는 수업 목표를 따옴표와 중괄호를 포함하여 그대로 출력합니다.
st.write("특수상대성이론의 결과로 나타나는 시간지연, 길이수축 현상에 대해 이해할 수 있다. ")

# st.divider() 함수를 사용하여 시각적인 구분선을 추가합니다.
st.divider()

# --- 2. 핵심 개념 요약 (AI 생성) ---

# st.subheader() 함수를 사용하여 소제목을 표시합니다.
st.subheader("핵심 개념 살펴보기")

# AI가 수업 제목과 목표에 맞춰 생성한 핵심 개념 요약 텍스트입니다.
# 변수 'core_concept'에 이 요약 내용을 문자열로 저장합니다.
core_concept = "특수상대성이론에 따르면, 물체가 빛의 속도에 가깝게 빠르게 움직일수록 관찰자에게는 그 물체의 시간이 느리게 가는 '시간 지연' 현상이 나타납니다. 또한, 그 물체의 운동 방향으로의 길이는 정지했을 때보다 짧아지는 '길이 수축' 현상도 함께 발생합니다."

# st.info() 함수를 사용하여 정보성 메시지를 강조하는 파란색 상자 안에 텍스트를 표시합니다.
# f-string (f"...")을 사용하여 변수 'core_concept'의 내용을 문자열 안에 포함시킵니다.
st.info(f"핵심 개념 요약: {core_concept}")

# 시각적인 구분선을 추가합니다.
st.divider()

# --- 3. 미니 퀴즈 (상태 관리) ---

# 소제목을 표시합니다.
st.subheader("미니 퀴즈")

# 퀴즈에 필요한 데이터(질문, 보기, 정답)를 변수에 저장합니다.
quiz_question = "정지한 관찰자가 빛의 속도에 가깝게 아주 빠르게 움직이는 우주선을 볼 때, 우주선 내부의 시간은 어떻게 관측될까요?"
quiz_options = [
    "정지한 관찰자의 시간보다 빠르게 흐른다.",  # 보기 1
    "정지한 관찰자의 시간보다 느리게 흐른다.",  # 보기 2 (정답)
    "정지한 관찰자의 시간과 동일하게 흐른다.",  # 보기 3
    "시간이 거꾸로 흐른다."  # 보기 4
]
# 정답에 해당하는 문자열을 'correct_answer' 변수에 저장합니다.
correct_answer = "정지한 관찰자의 시간보다 느리게 흐른다."

# st.session_state는 Streamlit 앱이 재실행되어도 데이터를 유지하는 특별한 딕셔너리(저장 공간)입니다.
# 'user_choice'라는 키(이름표)가 st.session_state에 아직 없으면(즉, 사용자가 아직 아무것도 선택하지 않았으면)
# 'user_choice'의 값을 None (값이 없음)으로 설정하여 초기화합니다.
if 'user_choice' not in st.session_state:
    st.session_state.user_choice = None  # 사용자의 선택을 저장할 공간을 만듭니다.

# st.radio() 함수를 사용하여 라디오 버튼 퀴즈를 만듭니다.
# 첫 번째 인자: 라디오 버튼 그룹의 제목 (여기서는 퀴즈 질문)
# options: 사용자에게 보여줄 선택지 목록 (위에서 정의한 quiz_options 변수)
# key: 이 라디오 버튼의 상태를 저장할 st.session_state의 키 이름입니다.
#      사용자가 보기를 선택하면, 그 선택된 값이 st.session_state.user_choice에 *자동으로* 저장됩니다.
st.radio(
    label=quiz_question,
    options=quiz_options,
    key='user_choice'  # 사용자의 선택이 이 키를 통해 'st.session_state.user_choice'에 연결(저장)됩니다.
)

# st.button() 함수를 사용하여 "정답 확인"이라는 텍스트가 표시된 버튼을 만듭니다.
# 이 버튼을 클릭하면, if 문 안의 코드가 실행됩니다.
if st.button("정답 확인"):
    # 버튼이 클릭되었을 때,
    # st.session_state에 저장된 사용자의 선택(st.session_state.user_choice)과
    # 미리 정의된 정답(correct_answer)을 비교합니다.
    if st.session_state.user_choice == correct_answer:
        # 두 값이 같다면 (즉, 정답이라면)
        # st.success() 함수를 사용하여 초록색 성공 메시지 상자를 표시합니다.
        st.success("정답입니다! 훌륭합니다.")
    else:
        # 두 값이 다르다면 (즉, 오답이라면)
        # st.error() 함수를 사용하여 빨간색 오류 메시지 상자를 표시합니다.
        st.error("아쉽네요. 다시 생각해 보세요.")
    