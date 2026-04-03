class Person {
    private String lastName;
    private int age;
    private boolean isMarried;

    public Person(String lastName, int age, boolean isMarried) {
        this.lastName = lastName;
        this.age = age;
        this.isMarried = isMarried;
    }

    public String getLastName() {
        return lastName;
    }

    public int getAge() {
        return age;
    }

    public boolean isMarried() {
        return isMarried;
    }
}

interface PersonFilter {
    boolean apply(Person person);
}

class AdultFilter implements PersonFilter {
    // Implement Adult filter
    @Override
    public boolean apply(Person person){
        if (person.age >= 18){
            return true;
        }
        return false;
    }
}

class SeniorFilter implements PersonFilter {
    // Implement Senior filter
    @Override
    public boolean apply(Person person){
        if (person.age >= 65){
            return true;
        }
        return false;
    }
}

class MarriedFilter implements PersonFilter {
    // Implement Married filter
    @Override
    public boolean apply(Person person){
        if (person.isMarried){
            return true;
        }
        return false;
    }
}

class PeopleCounter {
    private PersonFilter filter;
    private int count;

    public void setFilter(PersonFilter filter) {
        this.filter = filter;
    }

    public int count(List<Person> people) {
        // Implement method here
        count = 0;
        for(Person p : people){
            if (this.filter.apply(p))
            count ++;
        }
        return count;
    }
}
