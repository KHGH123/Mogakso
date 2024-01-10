import java.util.function.*;

public class s5 {
    public static void main(String args[]) {
        Function<String, Integer> f1 = (s) -> Integer.parseInt(s);
        Function<String, Integer> f2 = Integer::parseInt;

        System.out.println(f1.apply("100") + f2.apply("200"));

        Supplier<MyClass> s1 = () -> new MyClass();
        Supplier<MyClass> s2 = MyClass::new;

        Function<Integer, YourClass> s3 = (i) -> new YourClass(i);
        Function<Integer, YourClass> s4 = YourClass::new;

        Function<Integer, int []> a1 = (i) -> new int[i];
        Function<Integer, int []> a2 = int[]::new;
    }

}
class MyClass { }

class YourClass {
    int i;
    YourClass(int i) {
        this.i = i;
    }
}
