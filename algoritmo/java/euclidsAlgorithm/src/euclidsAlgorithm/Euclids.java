/**
 * 
 */
package euclidsAlgorithm;

/**
 * @author iasmim Araujo 20 de dez de 2021 
 * The idea this project is create an algorithm that 
 * organize the terms and calculate the gcd 
 */
public class Euclids {
	public static int euclids(int m, int n) {
		int r = m, aux = 0;
		//this part organize the terms
		if(m < n) {
			m = n;
			n = r;
		}
		if(n == 0) 
			return 0;
		//system that calculate the gcd
		while(m%n != 0) {
			r = (int)m/n;
			aux = m;
			m = n;
			n = aux - m*r;
		}
		return n;
	}
	static void print(int r) {
		System.out.println(r);
		System.out.println("----------");
	}

	public static void main(String[] args) {
		Euclids e = new Euclids();
		int r = 0;
		r= e.euclids(12,30);
		print(r);
		r = e.euclids(30,12);
		print(r);
		r = e.euclids(123,36);
		print(r);
		r = e.euclids(36,123);
		print(r);
		r = e.euclids(348,156);
		print(r);
		r = e.euclids(156, 348);
		print(r);
		
	}

}
