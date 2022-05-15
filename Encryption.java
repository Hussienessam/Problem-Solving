import java.io.*;
import java.util.*;

class Result {

    /*
     * Complete the 'encryption' function below.
     *
     * The function is expected to return a STRING.
     * The function accepts STRING s as parameter.
     */

    public static String encryption(String s) {
    // Write your code here
        
        s = s.replaceAll(" ", "");
        int length = s.length();
        double rootLength = Math.sqrt(length);
        int rows = (int)rootLength;
        int columns;
        if(rootLength > (double)rows) {
            columns = (int)rootLength + 1;
            rows = rows*columns - length > 0 ? rows: columns;
        }
        else {
            columns = (int) rootLength;
        }
        ArrayList<ArrayList<Character>> strings = new ArrayList<ArrayList<Character>>(rows);
        for(int i = 0; i < rows; i++) {
            ArrayList<Character> currentString = new ArrayList<Character>();
            for(int j = 0; j < columns; j++) {
                int index = (columns * i) + j;
                if(index < length) {
                    currentString.add(s.charAt(index));
                }
                else {
                    currentString.add('-');
                }
            }
            strings.add(currentString);
        }
        String encryptedString = "";
        for(int i = 0; i < columns; i++) {
            for(int j = 0; j < rows; j++) {
                if(strings.get(j).get(i) != '-') {
                    encryptedString += strings.get(j).get(i);
                }
            }
            encryptedString += " ";
        }
        return encryptedString;
    }

}

public class Encryption {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String s = bufferedReader.readLine();

        String result = Result.encryption(s);

        bufferedWriter.write(result);
        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }
}
