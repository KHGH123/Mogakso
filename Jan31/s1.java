import java.io.*;
import java.util.*;
import java.util.stream.*;

public class s1 {
    public static void main(String[] args) {
        File[] arr = {new File("Ex1.java"),
        new File("Ex1.bak"),
        new File("Ex1"),
        new File("Ex2.java"),
        new File("Ex2.txt")
        };
        Stream<File> fileStream = Stream.of(arr);
        Stream<String> filenameStream = fileStream.map(File::getName);
        filenameStream.forEach(System.out::println);
    
        fileStream = Stream.of(arr);

        fileStream.map(f->f.getName())
        .filter(s->s.indexOf('.')!=-1)
        .peek(s->System.out.printf("---%s---\n", s))
        .map(s->s.substring(s.indexOf('.')+1))
        .map(String::toUpperCase)
        .forEach(System.out::println);
        }

}
