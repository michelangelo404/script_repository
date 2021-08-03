import java.util.Scanner;

abstract class Shape { //superclasse forma con variabili e metodo area
    int width;
    abstract void area();
}
class Square extends Shape { 
    Square(int a){
        this.setWidth(a);
    }
    public void setWidth(int a){
        this.width = a;  //eredito width
    }
    void area(){
        int res;
        res = width * width;
        System.out.println(res);
    }
    
}
class Circle extends Shape {
    Circle(int b){
        this.setWidth(b);
    }
    public void setWidth(int b){
        this.width = b;  //eredito width
    }
    void area(){ //
        double res;
        res = Math.PI * width * width;
        System.out.println(res);
    }
    
}
//your code goes here


public class Program {
    public static void main(String[ ] args) {
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();
        int y = sc.nextInt();
        
        //creazione oggetti
        Square a = new Square(x); 
        Circle b = new Circle(y);
        //costruttore, da notare senza parametri
        a.area();
        b.area();
    }
}