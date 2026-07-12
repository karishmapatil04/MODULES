class Animal {
    private String name;
    private int age;

    public Animal(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public String getName() {
        return name;
    }

    public int getAge() {
        return age;
    }

    public void makeSound() {
        System.out.println("The animal makes a sound");
    }
}

class Dog extends Animal {
    private String breed;

    public Dog(String name, int age, String breed) {
        super(name, age);
        this.breed = breed;
    }

    public String getBreed() {
        return breed;
    }

    @Override
    public void makeSound() {
        System.out.println("The dog barks");
    }
}

class Cat extends Animal {
    private boolean isIndoor;

    public Cat(String name, int age, boolean isIndoor) {
        super(name, age);
        this.isIndoor = isIndoor;
    }

    public boolean getIsIndoor() {
        return isIndoor;
    }

    @Override
    public void makeSound() {
        System.out.println("The cat meows");
    }
}

public class Main {
    public static void main(String[] args) {
        Dog d = new Dog("Buddy", 3, "Labrador");
        Cat c = new Cat("Kitty", 2, true);

        System.out.println(d.getName() + " - " + d.getAge() + " - " + d.getBreed());
        d.makeSound();

        System.out.println(c.getName() + " - " + c.getAge() + " - Indoor: " + c.getIsIndoor());
        c.makeSound();
    }
}