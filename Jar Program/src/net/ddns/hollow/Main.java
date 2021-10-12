package net.ddns.hollow;

import java.io.*;

public class Main {
    public static void main(String[] args) {
        //If exists
        if(new File("/home/void/'Tis I").exists()){ //Can also do .isFile() or .isDirectory()
            System.out.println("\nSup, Void?\n");
        } else {
            System.out.println("\nIf not an ally, thy be foe.\n");
        }
    }
}
// For the "Jar Program" part https://www.jetbrains.com/help/idea/creating-and-running-your-first-java-application.html
// For the "If exists" part https://stackoverflow.com/questions/487181/how-to-check-path-is-existing-or-not-in-java#487187
