package com.project;

import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        
        List<Electrodomestic> llista = new ArrayList<>();
        List<Electrodomestic> llistaCopy = new ArrayList<>();

        // RENTADORES
        Rentadora rentadora1 = new Rentadora();
        rentadora1.nom = "Rentadora LG";     
        rentadora1.color = "Gris";       
        rentadora1.preu = 699.99;         
        rentadora1.marca = "LG";        
        rentadora1.eficiencia = "A++"; 
        rentadora1.revolucions = 1400;   
        rentadora1.soroll = 70;         
        llista.add(rentadora1);

        Rentadora rentadora2 = new Rentadora();
        rentadora2.nom = "Rentadora New Pol";     
        rentadora2.color = "Blanca";       
        rentadora2.preu = 299.00;         
        rentadora2.marca = "New Pol";        
        rentadora2.eficiencia = "A"; 
        rentadora2.revolucions = 1000;   
        rentadora2.soroll = 58;         
        llista.add(rentadora2);

        // NEVERES
        Nevera nevera1 = new Nevera();
        nevera1.nom = "Nevera Samsung";     
        nevera1.color = "Blanc";       
        nevera1.preu = 799.99;         
        nevera1.marca = "Samsung";        
        nevera1.eficiencia = "A+"; 
        nevera1.frigories = 300;     
        nevera1.soroll = 40;         
        llista.add(nevera1);

        Nevera nevera2 = new Nevera();
        nevera2.nom = "Nevera Siemens";     
        nevera2.color = "Negre";       
        nevera2.preu = 999.99;         
        nevera2.marca = "Siemens";        
        nevera2.eficiencia = "A++"; 
        nevera2.frigories = 450;     
        nevera2.soroll = 30;         
        llista.add(nevera2);

        // FORNS
        Forn forn1 = new Forn();
        forn1.nom = "Forn Bosch";     
        forn1.color = "Negre";       
        forn1.preu = 599.99;         
        forn1.marca = "Bosch";        
        forn1.eficiencia = "A++";    
        forn1.temperatura = 250;       
        forn1.autoneteja = true;     
        llista.add(forn1);

        Forn forn2 = new Forn();
        forn2.nom = "Forn Balay";     
        forn2.color = "Blanc";       
        forn2.preu = 399.99;         
        forn2.marca = "Balay";        
        forn2.eficiencia = "A+";    
        forn2.temperatura = 270;       
        forn2.autoneteja = false;     
        llista.add(forn2);

        // Clonar la llista
        for (Electrodomestic obj : llista) {
            llistaCopy.add(obj.clone());
        }

        System.out.println("Comparar la mateixa llista:");
        for (int i = 0; i < llista.size(); i++) {
            compare(i, llista.get(i), llista.get(i));
        }

        System.out.println("Comparar amb la llista clonada:");
        for (int i = 0; i < llista.size(); i++) {
            compare(i, llista.get(i), llistaCopy.get(i));
        }

        System.out.println("Comparar amb la llista clonada però invertida:");
        for (int i = 0; i < llista.size(); i++) {
            compare(i, llista.get(i), llistaCopy.get(llista.size() - i - 1));
        }
    }

    static void compare (int i, Electrodomestic a, Electrodomestic b) {
        if (a == b) {
            System.out.println(i + ": Els electrodomestics són el mateix objecte");
        } else {
            System.out.print(i + ": Els electrodomestics són objectes diferents - ");
            if (a.equals(b)) {
                System.out.println(i + ": Els electrodomestics són idèntics");
            } else {
                System.out.println(i + ": Els electrodomestics NO són identics");
            }
        }
    }
}
