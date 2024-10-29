package com.project;

import org.json.JSONArray;
import org.json.JSONObject;

import java.io.*;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;


public class DaoEina implements Dao<ObjEina> {
    private void writeList(ArrayList<ObjEina> llista) {
        try {
            JSONArray jsonArray = new JSONArray();
            for (ObjEina eina : llista) {
                JSONObject jsonObject = new JSONObject();
                jsonObject.put("id", eina.getId());
                jsonObject.put("nom", eina.getNom());
                jsonObject.put("any", eina.getAny());
                JSONArray jsonLlenguatges = new JSONArray(eina.getLlenguatges());
                jsonObject.put("llenguatges", jsonLlenguatges);
                jsonArray.put(jsonObject);
            }
            PrintWriter out = new PrintWriter(Main.einesPath);
            out.write(jsonArray.toString(4)); // 4 es l'espaiat
            out.flush();
            out.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
    private int getPosition (int id) {
        int result = -1;
        ArrayList<ObjEina> llista = getAll();
        for (int cnt = 0; cnt < llista.size(); cnt = cnt + 1) {
            ObjEina eina = llista.get(cnt);
            if (eina.getId() == id) {
                result = cnt;
                break;
            }
        }
        return result;
    }

    @Override
    public void add(ObjEina eina){
        ArrayList<ObjEina> llista = getAll();
        ObjEina item = get(eina.getId());
        if (item == null) {
            llista.add(eina);
            writeList(llista);
        }


    }


    @Override
    public ObjEina get(int id) {
        ObjEina result = null;
        ArrayList<ObjEina> llista = getAll();
        int pos = getPosition(id);
        if (pos != -1) {
            result = llista.get(pos);
        }
        return result;
    }

    @Override
    public ArrayList<ObjEina> getAll() {
        ArrayList<ObjEina> result = new ArrayList<>();
        try {
            String content = new String(Files.readAllBytes(Paths.get(Main.einesPath)));
            
            JSONArray jsonArray = new JSONArray(content);
            for (int i = 0; i < jsonArray.length(); i++) {
                JSONObject jsonObject = jsonArray.getJSONObject(i);
                int id = jsonObject.getInt("id");
                String nom = jsonObject.getString("nom");
                int any = jsonObject.getInt("any");
                JSONArray jsonLlenguatges = jsonObject.getJSONArray("llenguatges");
                ArrayList<Integer> llenguatges = new ArrayList<>();
                for (int j = 0; j < jsonLlenguatges.length(); j++) {
                    llenguatges.add(jsonLlenguatges.getInt(j));
                }
                ObjEina eina = new ObjEina(id, nom, any, llenguatges);
                result.add(eina);
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        return result;
    }
    


    @Override
    public void setAny(int id,int any){
        ArrayList<ObjEina> llista = getAll();
        int pos = getPosition(id);
        if (pos != -1) {
            ObjEina eina = llista.get(pos);
            eina.setAny(any);
            writeList(llista);
        }
    }

    @Override
    public void setNom(int id,String nom){
        ArrayList<ObjEina> llista = getAll();
        int pos = getPosition(id);
        if (pos != -1) {
            ObjEina eina = llista.get(pos);
            eina.setNom(nom);
            writeList(llista);
        }
    }

    public void setLlenguatgesAdd(int id,int idLlenguatge){
        ArrayList<ObjEina> llista = getAll();
        int pos = getPosition(id);
        if (pos != -1) {
            ObjEina eina = llista.get(pos);
            ArrayList<Integer> llenguatges = eina.getLlenguatges();
            llenguatges.add(idLlenguatge);
            eina.setLlenguatges(llenguatges);
            writeList(llista);
        }

    }

    public void setLlenguatgesDelete(int id,int idLlenguatge){
        ArrayList<ObjEina> llista = getAll();
        int pos = getPosition(id);
        if (pos != -1) {
            ObjEina eina = llista.get(pos);
            ArrayList<Integer> llenguatges = eina.getLlenguatges();
            llenguatges.remove(Integer.valueOf(idLlenguatge));
            eina.setLlenguatges(llenguatges);
            writeList(llista);
        }

    }

    @Override
    public void update(int id, ObjEina eina) {
        ArrayList<ObjEina> llista = getAll();
        int pos = getPosition(id);
        if (pos != -1) {
            llista.set(pos, eina);
            writeList(llista);
        }
    }

    @Override
    public void delete(int id) {
        ArrayList<ObjEina> llista = getAll();
        int pos = getPosition(id);
        if (pos != -1) {
            llista.remove(pos);
            writeList(llista);
        }
    }

    @Override
    public void print () {
        ArrayList<ObjEina> llista = getAll();
        for (int cnt = 0; cnt < llista.size(); cnt = cnt + 1) {
            System.out.println("    " + llista.get(cnt));
        }
    }
}

