import java.util.Scanner;
import java.util.Random;
public class Project{
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        Random random= new Random();
        System.out.print("how many rolls you want:");
        int num_of_roll=scan.nextInt();
        for(int i=0;i<num_of_roll;i++){
            int roll= random.nextInt(1,7);
            System.out.println("\n**********************");
            System.out.print("you rolled:"+roll+"\n");
            Print_dice(roll);
            System.out.println("**********************");
        }
    }
    static void Print_dice(int roll){

        String dice1= """
                      ---------
                      |       |
                      |   ♦   |
                      |       |
                      ---------
                      """;
        String dice2= """
                      ---------
                      |       |
                      | ♦   ♦ |
                      |       |
                      ---------
                      """;
        String dice3= """
                      ---------
                      | ♦     |
                      |   ♦   |
                      |     ♦ |
                      ---------
                      """;
        String dice4= """
                      ---------
                      | ♦   ♦ |
                      |       |
                      | ♦   ♦ |
                      ---------
                      """;
        String dice5= """
                      ---------
                      | ♦   ♦ |
                      |   ♦   |
                      | ♦   ♦ |
                      ---------
                      """;
        String dice6= """
                      ---------
                      | ♦   ♦ |
                      | ♦   ♦ |
                      | ♦   ♦ |
                      ---------
                      """;
        switch(roll){
            case 1: System.out.println(dice1);break;
            case 2: System.out.println(dice2);break;
            case 3: System.out.println(dice3);break;
            case 4: System.out.println(dice4);break;
            case 5: System.out.println(dice5);break;
            case 6: System.out.println(dice6);break;

        }
    }


}
