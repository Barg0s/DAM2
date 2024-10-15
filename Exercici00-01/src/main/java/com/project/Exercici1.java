package com.project;

import java.lang.reflect.Constructor;

public class Exercici1 {
    public static void main(String[] args) {
        try {
            for (int i = 1; i < 4; i++) {
                System.out.println("iniciant " + i);
                Thread.sleep(1000); 
            }
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        Objecte instanceOne = Objecte.getInstance("David", "Bargados", 18);
        Objecte instanceTwo = getNewDestroyedInstance("Marc", "Cachinero", 25);
        Objecte instanceThree = getNewDestroyedInstance("Adria", "Martinez", 18);

        System.out.println(instanceOne);
        System.out.println(instanceTwo);
        System.out.println(instanceThree);
    }

    private static Objecte getNewDestroyedInstance(String nom, String cognom, int edat) {
        Objecte instance = null;
        try {
            Constructor<Objecte> constructor = Objecte.class.getDeclaredConstructor(String.class, String.class, int.class);
            constructor.setAccessible(true);
            instance = constructor.newInstance(nom, cognom, edat);
        } catch (Exception e) {
            e.printStackTrace();
        }
        return instance;
    }
}
