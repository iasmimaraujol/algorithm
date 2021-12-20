package q1;

public class Duplicate {
	static void printArray(int[] array) {
		System.out.println("----------------");
		for(int i = 0; i < array.length; i++) {
			System.out.print(array[i] + " ");
		}
	}
	public static void find(int[] ar) {
		int aux = 0, cont = 0;
		for(int i = 0; i<ar.length; i++) {
			cont = i;
			aux = ar[i];
			while (cont != 0) {
				if(ar[cont] == ar[i]) {
					ar[i] = 0;
					cont = 1;					
				}
				cont = cont - 1;
			}
			
						
		}
		//printArray(ar);
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String[] st = {"G", "e", "e", "k", "s"}; 
		int[] ar = {1, 10, 2, 2, 10, 3, 3, 3, 4, 5, 5};
		Duplicate dp = new Duplicate();
		dp.find(ar);		
		printArray(ar);

	}

}
