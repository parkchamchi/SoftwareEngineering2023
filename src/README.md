Django를 이용한 프로토타입입니다.

## 수정방법
- (한번만 시행) `깃헙아이디`는 자기걸로 치환하세요
```
git clone https://github.com/parkchamchi/SoftwareEngineering2023`
git branch 깃헙아이디
git checkout 깃헙아이디
```

- `git pull origin main`: 수정하기 전에 시행해서 동기화할것
- 수정사항 적용 후, `git commit -m "의미있는 수정내역"`
- `git push origin 깃헙아이디`

그 다음 PR 올리시면 됩니다

## 실행
- (한번만 시행) `venv_create`로 venv 생성
- `venv`로 venv 적용
- (한번만 시행) `pip install -r requirements.txt`로 라이브러리 다운로드
- `runserver`로 서버 실행. 이후 `http://127.0.0.1:8000/lists`로 진입.

## 코드
- [lists/models.py](lists/models.py)에 `List`와 `Task`모델이 있습니다.
- [lists/views.py](lists/views.py)에 이 모델들을 조작하는 view들이 있습니다.
- [lists/urls.py](lists/urls.py)

- [templates/](templates/) 아래에 있는 HTML 파일 위주로 수정해주시면 됩니다. CSS는 그냥 HTML에 넣어주세요.
Bootstrap 사용 가능.
  - `base.html`: 페이지 헤더와 CSS 등이 있습니다.
  - `home.html`: 로그아웃 후 페이지.
  - `list_delete.html`: 삭제 확인 페이지
  - `list_detail.html`: 목록 내용 페이지 + 작업 삽입 폼
  - `list_edit.html`: 목록 내용 (제목) 수정 페이지
  - `list_list.html`: 목록을 나열한 페이지 (메인)
  - `list_new.html`: 목록 추가 (제목 설정) 페이지
  - `list_sort.html`: 목록 정렬 (기준 선택) 페이지
  - `task_item.html`: 작업 내용 (List에서 반복되어 표시됨)