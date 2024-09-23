package com.project;

import java.lang.reflect.Constructor;

public class Exercici1 {
    public static void main(String[] args) {
        try {
            for (int i = 0; i < 3; i++) {
                System.out.println("iniciant " + i);
                Thread.sleep(1000); 
            }
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        Objecte instanceOne = Objecte.getInstance("David", "Bargados", 18);


        Objecte instanceTwo = null;
        Objecte instanceThree = null; 

        try {
            Constructor[] constructors = Objecte.class.getDeclaredConstructors();
            for (Constructor constructor : constructors) {
                constructor.setAccessible(true); 
                instanceTwo = (Objecte) constructor.newInstance("Marc", "Cachinero", 25);
                instanceThree = (Objecte) constructor.newInstance("Manel", "Polar", 18);
                break;
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        System.out.println(instanceOne);
        System.out.println(instanceTwo);
        System.out.println(instanceThree);
    }
}
