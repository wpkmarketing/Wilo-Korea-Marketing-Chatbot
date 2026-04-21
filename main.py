import json

# 1. 저장한 FAQ 데이터 불러오기
def load_faq():
    with open('faq.json', 'r', encoding='utf-8') as f:
        return json.load(f)

# 2. 사용자의 질문에 맞는 답변 찾기
def get_answer(user_question, faq_data):
    for item in faq_data:
        # 질문 내용이나 태그에 키워드가 포함되어 있는지 확인
        if any(tag in user_question for tag in item['tags']) or item['question'] in user_question:
            return item['answer']
    
    return "상세한 상담이 필요하신가요? 1688-5890으로 연락 주시면 담당자를 연결해 드리겠습니다."

# 3. 테스트 실행
if __name__ == "__main__":
    data = load_faq()
    
    # 예시: 나중에 실제 챗봇 서비스와 연결될 부분입니다.
    test_query = "서비스 센터 번호 알려줘" 
    print(f"고객 질문: {test_query}")
    print(f"챗봇 답변: {get_answer(test_query, data)}")
