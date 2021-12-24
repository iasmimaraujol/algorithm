import java.util.Arrays;

/**
 * @author iasmim
 *
 */
public class Main {
	public static void main(String[] arg) {
		int[] x = {1,3,7,0,9,-1,46,81,24,9,60,8};
		int aux;
		for(int j = 0; j<x.length - 1; j++){
			for(int i = j + 1; i <= x.length - 1; i++){
				if(x[j]>x[i]) {
					aux = x[j];
					x[j] = x[i];
					x[i] = aux;
				}
			}
		}
		System.out.println(Arrays.toString(x));
	}
}


