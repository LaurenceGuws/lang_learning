package lang.learn.goose;

import java.util.NoSuchElementException;

import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;

import lang.learn.goose.entities.Person;
import lang.learn.goose.repositories.PersonRepository;


@SpringBootApplication
public class GooseApplication {

    public static void main(String[] args) {
        SpringApplication.run(GooseApplication.class, args);
    }

    @Bean
    CommandLineRunner runner(PersonRepository repository) {
        return args -> {

            Person person = new Person();
            person.setName("John");

            repository.save(person);
            Person saved = repository.findById(person.getId()).orElseThrow(NoSuchElementException::new);
            System.out.println("Saved person's name is: " + saved.getName());
        };
    }
}
