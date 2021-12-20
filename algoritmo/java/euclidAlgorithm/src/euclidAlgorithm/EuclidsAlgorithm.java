/**
 * 
 */
package euclidAlgorithm;

/**
 * @author iasmim araujo (20/12/2021)
 *
 */
public class EuclidsAlgorithm {
	public static int gcd(int m, int n) {
		int d = 0, x = 0;
		while(true) {
			d = (int)m/n;
			x = m;
			m = n;
			n = x - d*m;
					
			//System.out.print(d);
			if(m%n == 0) {
				return n;
			}
			
		}
	}

	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		EuclidsAlgorithm alg = new EuclidsAlgorithm();
		int min = 0;
		
		min = alg.gcd(30,12);
		System.out.println(min);
		min = alg.gcd(123,36);
		System.out.println(min);
		min = alg.gcd(348,156);
		System.out.println(min);
		

	}

}
