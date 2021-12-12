/**
 * 
 */
package linearSearch;

/**
 * @author Iasmim Araujo 12 de dez de 2021
 * linearSearch
 */
public class LinearSearch {

	public static void main(String[] args) {
		int toFind = 6;
		String string = "";
		int[] vect = {8,10,94,6,1,70,64,30,84};
		int i = 0;
		int control = vect.length;
		while(toFind != vect[i]) { 
			i++;
			if(i == control) {
				string = "element isn't present";
				break;
			}
		}
		if (string == "")
				string = Integer.toString(i);
		System.out.println(string);
	}

}
