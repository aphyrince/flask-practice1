# HW6

안정호 · 21011318

## 실행 방법

.venv/Scripts/activate 로 가상환경 켜기.

터미널에서 pip install -r requirements.txt 실행.

터미널에서 cd .\HW6\ 실행.

jupyter 로 hw6.ipynb 를 열고, Kernel을 venv로 바꾼 후 Run All

터미널에서 flask run 뒤 http://127.0.0.1:5000/api/docs 접속.

## 단계③답

선형회귀 모델은 덧셈으로 관계를 표현한다.

그러나 데이터에는 quantity x unit_price = total_sales 로 표현되는 곱셈 관계가 성립중이다.

따라서 qp 컬럼을 더함으로써 입력 데이터의 곱셈 관계를 반영할 수 있다.

## 단계⑤결정과 이유

max_depth=8 로 결정.

교차 검증 평균이 충분히 높고, 8보다 큰 깊이에서의 교차 검증 평균 값들이 거의 같으므로 그 중 가장 단순한 8이 합리적.

## 단계⑦답

모델 : linear + qp

제시된 3가지 모델들 중 가장 높은 성적을 얻었다.

qp 컬럼을 추가함으로써 quantity x price 라는 실제 계산 공식과 동일한 결과를 얻었다.

후에 입력 feature의 구성이 달라졌을 때 코드를 수정하기 쉽다.
