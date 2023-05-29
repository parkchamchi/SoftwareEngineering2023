Django를 이용한 프로토타입입니다.

## 실행
- (한번만 시행) `venv_create`로 venv 생성
- `venv`로 venv 적용
- (한번만 시행) `pip install -r requirements.txt`로 라이브러리 다운로드
- `runserver`로 서버 실행. 이후 `http://127.0.0.1:8000/lists`로 진입.

## 코드
- `lists/models.py`에 `List`와 `Task`모델이 있습니다.
- `lists/views.py`에 이 모델들을 조작하는 view들이 있습니다.
- `lists/urls.py`
- HTML 파일들은 `templates/` 아래에 있습니다.