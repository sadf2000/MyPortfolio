import java.util.Scanner;

public class test{
  public static void main(String[] args){
    System.out.println("Калькулятор(1 - вычитание; 2 - сложение)");
    Scanner input = new Scanner(System.in);
    String lol = input.nextInteger();
    if (lol == 1){
      System.out.println("Напишите 1 число:");
      Float num1 = input.nextFloat();
      System.out.println("Напишите 2 число:");
      Float num2 = input.nextFloat();
      System.out.println("Ответ:"+Float.toString(num1+num2));
    }
    if (lol == 2){
      System.out.println("Напишите 1 число:");
      Float num1 = input.nextFloat();
      System.out.println("Напишите 2 число:");
      Float num2 = input.nextFloat();
      System.out.println("Ответ:"+Float.toString(num1-num2));
    }
  }
}
