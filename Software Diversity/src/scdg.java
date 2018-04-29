import java.io.*;
import java.util.*;

//SCDG = System Call Dependence Graph
public class scdg
{
	public static void main(String[] args) {
		
	    // The name of the file to open.
	    String fileName = "test.txt";
	
	    // This will reference one line at a time
	    String line = null;
	    String arr[] = new String[1000];
	    
	    List<String> syscalls = new ArrayList<>();
	    
	
	    try {
	        // FileReader reads text files in the default encoding.
	        FileReader fileReader = new FileReader(fileName);
	
	        // Always wrap FileReader in BufferedReader.
	        BufferedReader bufferedReader = new BufferedReader(fileReader);
	        
	        //Parses syscalls commands to arraylist.
	        while((line = bufferedReader.readLine()) != null) {
	            //System.out.println(line);
	        	arr = line.split("\\(");
	        	syscalls.add(arr[0]);
	        }   
	
	        // Always close files.
	        bufferedReader.close();         
	    }
	    catch(FileNotFoundException ex) {
	        System.out.println(
	            "Unable to open file '" + fileName + "'");                
	    }
	    catch(IOException ex) {
	        System.out.println(
	            "Error reading file '" + fileName + "'");                  
	        
	    }
	}      

}

// End HelloJGraphT.java