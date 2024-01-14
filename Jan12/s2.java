import java.util.*;
import java.util.stream.*;

public class s2 {
    public static void main(String[] args) {
        Stream<String[]> strArrStream = Stream.of (
            new String[]{"abc","def","ghi"},
            new String[]{"ABC","GHI","JKL"}
        );

        Stream<String> strStream = strArrStream.flatMap(Arrays::stream);
        strStream.map(String::toLowerCase)
        .distinct()
        .sorted()
        .forEach(System.out::println);

        String[] lineArr = {
            "NewJeans Ditto",
            "Ive I don't know their songs"
        };

        Stream<String> lineStream = Arrays.stream(lineArr);
        lineStream.flatMap(line->Stream.of(line.split(" +")))
        .map(String::toLowerCase)
        .distinct()
        .sorted()
        .forEach(System.out::println);
        
    }
}
