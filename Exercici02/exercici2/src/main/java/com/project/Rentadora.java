package com.project;

public class Rentadora extends Electrodomestic {
    public int revolucions;
    public int soroll;

    public Rentadora(){};

    public Rentadora(Rentadora target){
        super(target);
        if (target != null) {
            this.revolucions = target.revolucions;
            this.soroll = target.soroll;
        }
    }

    @Override
    public Electrodomestic clone() {
        return new Rentadora(this);
    }

    @Override
    public boolean equals(Object object2) {
        // Comprova si són la mateixa referència
        if (this == object2) return true;

        if (!(object2 instanceof Electrodomestic) || !super.equals(object2)) return false;

        // Comprova si els dos objectes són exactament de la mateixa classe
        if (!this.getClass().equals(object2.getClass())) return false;

        Rentadora cast2 = (Rentadora) object2;
        return cast2.revolucions == revolucions && cast2.soroll == soroll;
    }
}