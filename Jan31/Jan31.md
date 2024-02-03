# 스트림의 중간연산

## 스트림 자르기
* `skip()` : 건너뛰기
    ```java
    Stream<T> skip(long n) // n만큼 건너뜀
    ```
* `limit()` : 스트림 요소 제한
    ```java
    Stream<T> limit(long maxSize) // maxSize까지만 제한
    ```

## 스트림 요소 걸러내기
* `filter()` : 주어진 조건에 맞지 않는 요소 제거
    ```java
    Stream<T> filter(Predicate<? super T> predicate)
    ```
* `distinct()` : 중복 요소 제거
    ```java
    Steram<T> distinct()
    ```

## 정렬
* `sorted()` : 스트림을 정렬
    ```java
    Stream<T> sorted()
    Stream<T> sorted(Comparator<? super T> comparator)
    ```

## 변환
* `map()` : T 타입의 스트림을 R 타입으로 변환
    ```java
    Stream<R> map(Function<? super T, ? extends R> mapper)
    ```
* `flatmap()` : 스트림의 요소가 배열이거나 `map()`의 연산 결과가 배열인 경우(Stream T[]), Stream<T>로 반환
    ```java
    Stream<String[]> strArrStream = Stream.of(
        new String[]{"abc","def","ghi"},
        new String[]{"ABC","GHI","JKLMN"}
    );

    Stream<String> strStream = strArrStream.flatmap(Arrays::Stream);
    // strStream은 Stream<String>으로, 요소는 "abc","def","ghi","ABC","GHI","JKLMN"이 있다.
    ```

## 조회
* `peek()` : 스트림의 요소를 소모하지 않고 확인 가능
    ```java
    .peek(s->System.out.printf("filename = %s", s))
    ```

# Optional<T>
* Optional<T> : T 타입(모든 타입)의 참조변수를 다음
    ```java
    public final class Optional<T> {
        ...
        private final T value;
        ...
    }
    ```
* Null을 직접 쓰면 위험함
    
    * `NullPointerException` 등등...

    그렇기 때문에 Optional을 통해 Null에 간접 접근

    * 최종 연산의 결과를 Optional 객체에 반환
    
## Optional<T> 객체 생성하기    
```java
String str = "abc";
Optional<String> optVal = Optional.of(str);
Optional<String> optVal = Optional.of("abc");
Optional<String> optVal = Optional.of(new String("abc"));

// null
Optional <String> optVal = Optional.of(null); // NullPointerException
Optional <String> optVal = Optional.ofNullabel(null);   // OK

Optional <String> optVal = null;
Optional <String> optVal = Optional.empty();
```

## Optional<T> 값 가져오기
```java
Optional <String> optVal = Optional.of("abc");
String str1 = optVal.get();  // optVal의 값 가져옴, null이면 예외 발생
String str2 = optVal.orElse(""); // null인 경우 ""를 반환

String str3 = optVal.orElseget(String::new); // ()->new String()과 동일
String str4 = optVal.orElseThrow(NullPointerException::new);
```
* `isPresent()` : Optional 객체의 값이 null이면 false, 아니면 true 반환

* `ifPresent()` : null이 아닌 경우 값 출력
    ```java
    optVal.ifPresent(System.out::println());
    ```
