public class FindEvenNumbers {

    // Method to find and return all even numbers from the input array
    public int[] findEvenNumbers(int[] numbers) {
        // Initialize an empty array to store even numbers
        int[] evenNumbers = new int[0];

        // Loop through the input array and check if each number is even
        for (int i = 0; i < numbers.length; i++) {
            if (numbers[i] % 2 == 0) {
                // Create a new array with one more space to hold the new even number
                int[] newEvenNumbers = new int[evenNumbers.length + 1];
                // Copy the existing even numbers to the new array
                System.arraycopy(evenNumbers, 0, newEvenNumbers, 0, evenNumbers.length);
                // Add the current even number to the new array
                newEvenNumbers[evenNumbers.length] = numbers[i];
                // Update the evenNumbers array to point to the new array
                evenNumbers = newEvenNumbers;
            }
        }

        // Return the array containing all even numbers
        return evenNumbers;
    }

    // Main method - Entry point of the program
    public static void main(String[] args) {
        // Sample input array
        int[] numbers = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };

        // Create an object of FindEvenNumbers class
        FindEvenNumbers obj = new FindEvenNumbers();

        // Call the method to get the even numbers from the input array
        int[] evenNumbers = obj.findEvenNumbers(numbers);

        // Print the even numbers
        System.out.print("Even numbers: ");
        for (int num : evenNumbers) {
            System.out.print(num + " ");
        }
    }
}