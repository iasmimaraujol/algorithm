package commonElements;

/**
 * @author iasmim
 *
 */
public class ComonElements {
	static void print(int[] array) {
		System.out.println();
		for(int i = 0; i <array.length; i++) {
			System.out.print(array[i] + " ");
		}
	}
	public int[] comon(int[] l1, int[] l2) {
		int[] l = new int[6];
		int aux = 0;
		for(int i = 0; i < l1.length; i++) {
			for(int j = 0; j < l2.length; j++) {
				if(l1[i]==l2[j]) {
					l[aux] = l1[i];
					aux += 1;
					break;
				}				
			}			
		}
		return l;
	}
	
	public static void main(String[] args) {
		int[] l1 = {2,5,5,5};
		int[] l2 = {2,2,3,5,5,7};
		ComonElements ce = new ComonElements();
		int[] l  =	ce.comon(l1, l2);
		print(l);
		
		// TODO Auto-generated method stub

	}

}
