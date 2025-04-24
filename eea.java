public class eea {
	public static void main(String[] args) {
		int a = Integer.parseInt(args[0]);
		int b = Integer.parseInt(args[1]);
		int q = a / b;
		int r = a % b;

		// make sure a is greater than b
		if (a < b) {
			int temp = a;
			a = b;
			b = temp;
		}

		// calculation loop
		while (r != 0) {
			q = a / b;
			r = a % b;

			System.out.println(a + " = (" + q + ")(" + b + ") + " + r);			

			if (r != 0) {
				a = b;
				b = r;
			}

		}
		System.out.println("GCD: " + b);
	}
}
