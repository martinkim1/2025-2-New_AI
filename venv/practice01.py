from openai import OpenAI
from dotenv import load_dotenv

# .env 파일에서 환경 변수 로드
load_dotenv()

# API 키는 환경 변수(`OPENAI_API_KEY`)에서 자동으로 로드됩니다.
client = OpenAI()

try:
    # Chat Completions API 호출
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "너는 채점기다. 사용자의 질문에 대해 정답만 한 단어로 출력한다. "
                    "불필요한 단어, 설명, 조사, 접미사, 따옴표, 마침표 없이 정답만 출력하라. 예: '서울'"
                ),
            },
            {"role": "user", "content": "파이썬의 최초 개발자는 누구인가요?"},
        ],
        # 안전하게 한 단어만 유도하기 위해 최대 토큰을 작게 제한
        max_tokens=5,
        temperature=0,
    )

    # 응답에서 메시지 내용 추출 및 출력
    message_content = response.choices[0].message.content.strip()
    print(message_content)

except Exception as e:
    print(f"An error occurred: {e}")