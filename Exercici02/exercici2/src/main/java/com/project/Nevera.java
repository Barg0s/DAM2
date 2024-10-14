package com.project;

public class Nevera extends Electrodomestic {
    public int frigories;
    public int soroll;

    public Nevera(){};

    public Nevera(Nevera target){
        super(target);
        if (target != null) {
            this.frigories = target.frigories;
            this.soroll = target.soroll;
        }
    }

    @Override
    public Electrodomestic clone() {
        return new Nevera(this);
    }

    @Override
    public boolean equals(Object object2) {
        // Comprova si són la mateixa referència
        if (this == object2) return true;

        if (!(object2 instanceof Electrodomestic) || !super.equals(object2)) return false;

        // Comprova si els dos objectes són exactament de la mateixa classe
        if (!this.getClass().equals(object2.getClass())) return false;

        Nevera cast2 = (Nevera) object2;
        return cast2.frigories == frigories && cast2.soroll == soroll;
    }
}