package com.project;

public class Exercici0 {
    public static void main(String[] args) {
        try {
            for (int i = 1; i < 4; i++) {
                System.out.println("iniciant " + i);
                Thread.sleep(1000); }
        } catch (InterruptedException ex) {
            ex.printStackTrace();
        }

        Objecte obj1 = Objecte.getInstance("David", "Bargados", 18);
        Objecte obj2 = Objecte.getInstance("Adrià", "Martinez", 19);
        Objecte obj3 = Objecte.getInstance("Manel", "Polar", 18);

        System.out.println(obj1); 
        System.out.println(obj2);
        System.out.println(obj3);
    }
}
