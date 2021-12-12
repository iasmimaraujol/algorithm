/**
 * 
 */
package insertionSort;

/**
 * @author iasmim araujo 10/12/2021
 *
 */
public class InsertionSort {
	static void arrayPrint(int[] arr) {
		int n = arr.length;	
		System.out.println("--------------");
		for(int i= 0; i < n; i++) {
			System.out.print(arr[i] + " ");
		}
		System.out.println();
	}

	public static void main(String[] args) {
		int[] vector = {1,95,64,2,7,1,67,98,33,14};
		for(int i = 1; i < vector.length; i++) {
			while(vector[i] < vector[i - 1]){				
				//arrayPrint(vector);
				int aux = vector[i - 1];
				vector[i - 1] = vector[i];
				vector[i] = aux;
				i--;				
			}
		}
		arrayPrint(vector);
	}
}
