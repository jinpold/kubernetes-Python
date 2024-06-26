'''Overview
The data has been split into two groups:

training set (train.csv)
test set (test.csv)
The training set should be used to build your machine learning models.
For the training set,
we provide the outcome (also known as the "ground truth") for each passenger.
Your model will be based on "features" like passengers' gender and class.
You can also use feature engineering to create new features.

The test set should be used to see how well your model performs on unseen data.
For the test set, we do not provide the ground truth for each passenger.
It is your job to predict these outcomes.
For each passenger in the test set,
use the model you trained to predict
whether or not they survived the sinking of the Titanic.

We also include gender_submission.csv,
a set of predictions that assume all and only female passengers survive,
as an example of what a submission file should look like.


Variable Notes
pclass: A proxy for socio-economic status (SES)
1st = Upper
2nd = Middle
3rd = Lower

age: Age is fractional if less than 1.
If the age is estimated, is it in the form of xx.5

sibsp: The dataset defines family relations in this way...
Sibling = brother, sister, stepbrother, stepsister
Spouse = husband, wife (mistresses and fiancés were ignored)

parch: The dataset defines family relations in this way...
Parent = mother, father
Child = daughter, son, stepdaughter, stepson
Some children travelled only with a nanny, therefore parch=0 for them.
컬럼(column) = 변수(variable) = 피처(feature)
'Survived', --> label
'Pclass',
'Name',
'Sex',
'Age',
'SibSp',
'Parch',
'Ticket',
'Fare',
'Cabin',
'Embarked'

# Categorical

데이터가 카테고리로 묶일 때 사용한다.

**nominal** : 이름을 바탕으로 하는 척도
순서와는 상관없이 그냥 셀 수 있는 정도의 데이터
ex)_ 청팀, 홍팀, 백팀 ....

**ordinal** : 순서를 바탕으로 하는 척도
자료들 사이에 순서(서열)가 있는 경우
ex)_ 청팀이 이길 가능성 1. 매우 낮음 2. 낮음 3. 보통 4. 높음 5. 매우높음

# Quantitative

숫자로 셀 수 있을때 사용한다.

**interval** : 간격 바탕으로 하는 척도
기준이 없이 일정한 측정 구간을 갖는 데이터
ex)_ 11:00~11:05, 15:55~16:00, 온도, ph (10배 덥다, 10배 시다 불가능)

**ratio** : 비율을 바탕으로 하는 척도
임의의 원점을 기준으로 두고 정하는 데이터
ex)_ 나이, 돈, 몸무게 (10배 많다...가 가능)'''