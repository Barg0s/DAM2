package com.project;

public final class Objecte {
    private static Objecte instance;
    private String nom;
    private String cognom;
    private int edat;

    private Objecte(String nom, String cognom, int edat) {
        this.nom = nom;
        this.cognom = cognom;
        this.edat = edat;
    }

    public static Objecte getInstance(String nom, String cognom, int edat) {
        if (instance == null) {
            instance = new Objecte(nom, cognom, edat);
        }
        return instance;
    }

    @Override
    public String toString() {
        return  "nom: " + nom  + ' ' +"cognom: " + cognom +' ' + "edat: " + edat  ;
    }

}