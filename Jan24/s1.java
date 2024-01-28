import java.util.Random;
import java.util.stream.IntStream;
import java.util.stream.Stream;

public class s1 {
    public static void main(String[] args) {
        IntStream intStream1 = new Random().ints();
        intStream1.limit(5).forEach(System.out::println);

        IntStream intStream2 = new Random().ints(5,1,6);
        intStream2.limit(5).forEach(System.out::println);

        Stream<Integer> intStream3 = Stream.iterate(0, n->n+2);
        intStream3.limit(10).forEach(System.out::println);

        Stream<Integer> intStream4 = Stream.generate(()->1);
        intStream4.limit(10).forEach(System.out::print);
    }
}
