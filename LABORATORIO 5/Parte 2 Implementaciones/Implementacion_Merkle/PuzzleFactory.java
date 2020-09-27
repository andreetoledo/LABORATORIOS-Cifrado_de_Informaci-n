import java.util.HashMap;
import java.util.Map;

//Laboratorio 5 Cifrado de la Informacion
//Grupos v2 # 6

/**
 *Program Based on:
 * https://github.com/kn100/Merkel-Puzzles
 */
public class PuzzleFactory {
    //Number of puzzles to make
    private static final int PUZZLES = 1024;

    /**
     * makePuzzles makes a set of puzzles all of which have their own unique ID.
     * @return a Map<Integer,Puzzle> where the key is the ID of the puzzle, and the value is the puzzle object.
     */
    public static Map<Integer,Puzzle> makePuzzles() {
        System.out.println("makePuzzles::Making 1024 puzzles");
        Map<Integer,Puzzle> puzzleSet = new HashMap<>(PUZZLES);
        for(int i=0;i<PUZZLES;i++) {
            puzzleSet.put(i,new Puzzle(i));
        }
        return puzzleSet;
    }
}
