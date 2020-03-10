public class Application {
    public static void main(String args[]) {
        DoublyLinkedList<Integer> dll = new DoublyLinkedList<Integer>();

        dll.addFirst(100);
        dll.addLast(200);
        dll.add(300);
        System.out.println("dll is " + dll.toString());
    }


}