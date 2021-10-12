package net.ddns.hollow;

import java.io.FileNotFoundException;
import java.io.IOException;
import java.nio.file.*;

public class Main {
    public static void main(String[] args) {
        Path source = Paths.get("/home/void/Desktop/Anti-Space/Java/Moving Files/movethis");
        Path target = Paths.get("/home/void/Desktop/Anti-Space/Java/Moving Files/to here/movethis");


        // Error handling
        try {
            Files.move(source, target);
            System.out.println("\nMoved.");
        } catch (FileAlreadyExistsException fae) {
            System.out.println("\nFile already exists.");
        } catch (FileNotFoundException fnf) {
            System.out.println("\nFile not found");
        } catch (NoSuchFileException nsf) {
            System.out.println("\nThere's no such file");
        } catch (AccessDeniedException ad) {
            System.out.println("\nCannot move file - Permission Denied");
        } catch (IOException e) {
            System.out.println("\nInput/Output Error");
        }
    }
}
