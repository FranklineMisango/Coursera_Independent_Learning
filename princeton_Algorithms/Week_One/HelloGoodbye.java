public class HelloGoodbye {
    public static void main(String[] args) {
        if (args.length != 2) {
            System.out.println("Usage: java HelloGoodbye <name1> <name2>");
            return;
        }

        String name1 = args[0];
        String name2 = args[1];

        // Print hello messages
        System.out.println("Hello " + name1 + "!");
        System.out.println("Hello " + name2 + "!");

        // Print goodbye messages in reverse order
        System.out.println("Goodbye " + name2 + "!");
        System.out.println("Goodbye " + name1 + "!");
    }
}
