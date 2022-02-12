\**본 시리즈는 python과 java에 대한 기본적인 이해를 토대로 합니다.
\** 제가 가진 궁금증에 조사와 이해를 더해 작성한 포스팅이라 오류가 있을 수 있습니다. 발견 시 지적해주시면 **매우매우** 감사하겠습니다.
<br>
python을 사용하다가 Java를 사용하면, 좀 더 엄격하고 세세한 문법에 궁금증이 생긴다. 코테 보다가 궁금해하지 말고 미리 해결 해보자.

### Integer와 int는 뭐가 다른가요?

- 한 줄 요약: Integer은 Class고 int는 숫자다.

||Integer|int|
|---|:---:|:---:|
|**type**|Wrapper Class|자료형(primative type)<sup>[2](#footprint_1)</sup>|
|**산술 연산** (a+b)|불가능|가능|
|**Null** (a == null)|가능|불가능|
|용도|객체가 필요할 때|변수의 type|
|ex.|Integer a = new Integer(10);|int y = 10;|

그러면 당연히 따라오는 질문:

### Wrapper Class가 뭐예요?

|자료형(primative type)|Wrapper Class|
|---|---|
|int|Integer|
|long|Long|
|double|Double|
|float|Float|
|boolean|Boolean|
|char|Char|
<sup>[ref_1](#ref_1)</sup>

이상한게, 제일 자주 쓰이는 **String**은 어디갔죠?
더 이상한게, String은 자료형 모양으로도 쓰이고 Wrapper Class 모양으로도 쓰이잖아요.

```java
String a = "Let it go";
ArrayList<String> b = new ArrayList<>();
```

얘는 특별대우래요. 왜이러는거야.
<img src="https://images.velog.io/images/randallkk/post/0322554e-0c78-46ab-ab63-0b71f9a72e32/CatCatStareGIF.gif" width="250" alt="CatCatStareGIF">

<details>
    <summary>
      참고 문헌
    </summary>
<a name="ref_1" href="https://wikidocs.net/205"> 점프 투 자바: 03-04 문자열 (String)</a>
</details>
