package lang.learn.goose.repositories;

import java.util.Optional;

import org.springframework.data.repository.Repository;

import lang.learn.goose.entities.Person;


public interface PersonRepository extends Repository<Person, Long> {

  Person save(Person person);

  Optional<Person> findById(long id);
}
