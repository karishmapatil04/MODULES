class staticcounter {
    // uncomment the below lines to know the importance of static keyword

    int number = 10;
    // static int number=10;

    void increment() {
        number = number + 1;
    }

    public static void main(String[] args) {
        staticcounter obj1 = new staticcounter();
        staticcounter obj2 = new staticcounter();
        staticcounter obj3 = new staticcounter();

        // Guess the answer
        obj1.increment();
        obj2.increment();
        obj3.increment();

        // to check your answers uncomment the next lines

        // System.out.println(obj1.number);
        // System.out.println(obj2.number);
        // System.out.println(obj3.number);
    }
}