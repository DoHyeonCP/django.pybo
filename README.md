# django.pybo
- Django로 게시판을 만들며 웹 제작해보기

### 1. 메인화면
![pybomain](https://github.com/DoHyeonCP/django.pybo/assets/119473997/cce2f379-29e4-4c1b-b90c-d64996ea1a20)
#### 1) 질문등록하기 
- 질문등록하기 버튼을 누르면 질문을 등록할 수 있습니다.
![pyboregistration](https://github.com/DoHyeonCP/django.pybo/assets/119473997/dc66960e-7bdf-4ac9-b934-86b4048fc013)

#### 2) 검색
- 검색어와 유사한 제목 + 내용을 가진 게시물만 볼 수 있습니다. 
![pybosearch](https://github.com/DoHyeonCP/django.pybo/assets/119473997/2d9ff3c2-e250-4060-94d8-d30c8ebb5bd2)

### 3) 페이징네이션을 사용하여 20개의 게시물씩 한 페이지에서 확인 가능하며 페이지가 너무 많을 경우 현재 페이지를 기준으로 왼쪽 2개 오른쪽 2개만을 소분하여 보여줍니다.

### 2. 회원가입 및 로그인
#### 1) 회원가입
- 회원가입을 자신의 계정을 등록할 수 있습니다.
![image](https://github.com/DoHyeonCP/django.pybo/assets/119473997/ad81be0f-fc62-4106-9d50-3b3876a94c17)

#### 2) 로그인/로그아웃
- 로그인하여 게시물 작성, 답변작성 등에 대한 권한을 얻을 수 있고 자유롭게 로그아웃 가능합니다.
![image](https://github.com/DoHyeonCP/django.pybo/assets/119473997/d952a2ce-fe24-4fe8-8365-a0fbb026e96e)


### 3. 게시물
#### 1) 게시물
![스크린샷 2023-10-15 212843](https://github.com/DoHyeonCP/django.pybo/assets/119473997/a53b4d20-764e-4029-bae4-70d877b025ed)
- 게시물을 통해 답변을 작성할 수 있으며 자신이 작성한 게시물과 답변을 수정, 삭제할 수 있습니다.

#### 2) 마크다운 및 추천,앵커 기능
- 마크다운을 사용하여 게시물을 편리하게 작성할 수 있습니다.
![스크린샷 2023-10-15 212948](https://github.com/DoHyeonCP/django.pybo/assets/119473997/56d5f83e-e5ea-4d03-bec6-1b4a4e8b38aa)

- 다른 사람이 작성한 게시물의 좋아요를 누를수 있습니다.
![스크린샷 2023-10-15 212948](https://github.com/DoHyeonCP/django.pybo/assets/119473997/6fa46720-051f-44d1-b1d9-531aafcf84be)

- 앵커 태그를 활용하여 답변등록 후 불필요한 스크롤 활동을 제거했습니다.
![스크린샷 2023-10-15 213241](https://github.com/DoHyeonCP/django.pybo/assets/119473997/4d85fc40-b99e-404b-be07-29816e68177e)


