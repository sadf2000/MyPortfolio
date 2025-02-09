import java.util.Scanner;

public class input_test{
  public static void main (String[] args){
    int x, y;
    // Чтение значений x, y из консоли
    Scanner in = new Scanner(System.in);
    System.out.println("Enter x :");
    x = in.nextInt();
    System.out.println("Enter y :");
    y = in.nextInt();
    System.out.printf ("Результат:"+Integer.toString(x+y));

  }
}
