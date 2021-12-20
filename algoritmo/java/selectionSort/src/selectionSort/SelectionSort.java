/**
 * 
 */
package selectionSort;

/**
 * @author Iasmim Araujo 14 de dez de 2021
 * 
 */
public class SelectionSort {
	static void printArray(int[] array) {
		System.out.println("----------------");
		for(int i = 0; i < array.length; i++) {
			System.out.print(array[i] + " ");
		}
	}
	public void selection(int[] array) {
		int n = array.length;
		int cont = n;
		int aux = 0, aux2 = 0;
		for(int i = 0; i < n; i++) {
			if(aux > array[i]) {
				aux = array[i];
			}
			if(i == n - 1) {
				i = i - cont + 1;
				aux2 = array[i];
				array[i] = aux;
				array[i + 1] = aux2;
				cont = cont - 1;				
			}
		}
		
	}
	public static void main(String[] args) {
		int[] array = {2,3,4,5,6,9,1,10,-1};
		SelectionSort sc = new SelectionSort();
		sc.selection(array);
		printArray(array);
		

	}

}
