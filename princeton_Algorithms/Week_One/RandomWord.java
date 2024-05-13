import java.util.Scanner;

public class RandomWord {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String champion = ""; // Current champion word
        int count = 0; // Count of words read so far

        System.out.println("Enter a sequence of words followed by Ctrl+D (Unix-like) or Ctrl+Z (Windows) to end:");

        while (scanner.hasNext()) {
            String word = scanner.next();
            count++;

            // Knuth's method: select the word with probability 1/count to be the champion
            if (Math.random() < 1.0 / count) {
                champion = word;
            }
        }

        // Print the surviving champion
        System.out.println("Randomly selected word: " + champion);

        scanner.close();
    }
}
