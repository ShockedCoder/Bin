package com.fuckoff;


import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.Scanner;
/*
class vars{

    public enum Global {
        token,
        prefix,
        Creator,
        Dev
    }

    public static void main(String[] args) {

        try {
            File tokenFile = new File("TOKEN");
            Scanner token = new Scanner(tokenFile);
            System.out.println(token);
        } catch (FileNotFoundException e) {
            System.out.println("Make a file name \"TOKEN\" and put your token in it");
            e.printStackTrace();
        }

        try {
            File prefixFile = new File("./PREFIX");
            Scanner rawPrefix = new Scanner(prefixFile);
        } catch (FileNotFoundException e) {
            final String prefix = "-- ";
        }


        final long Creator = 287190213451710464L; // Void
        final long[] Dev = {422801394957942789L, 226589962789715968L, 169501254899335168L}; // Jakub, Leon, Stevie

        System.out.println("\n" + Global.token + " " + Global.prefix + " " + Creator + " " + Dev);

    }
}

class Main{
    public static void main(String[] args) {
        System.out.println("\n\n" + vars.Global.token + " " + vars.Global.prefix + " " + vars.Global.Creator + " " + vars.Global.Dev + "\n");
    }
}
*/

class Main {
    public static void main(String[] args) {

        /*try {
            File file = new File("TOKEN");
            Scanner scanner = new Scanner(file);
            System.out.println(scanner);
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }*/

        try {
            // create a reader
            FileReader reader = new FileReader("TOKEN");

            // read every characer
            int ch;
            while ((ch = reader.read()) != -1) {
                System.out.print((char) ch);
            }

            // close the reader
            reader.close();

        } catch (IOException ex) {
            ex.printStackTrace();
        }

    }
}