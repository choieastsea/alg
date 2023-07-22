import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
	private int pivRecursionCount(int n) {
		if (n == 1 || n == 2) {
			return 1;
		} else
			return (pivRecursionCount(n - 1) + pivRecursionCount(n - 2));
	}

	private int pivDpCount(int n) {
		return n-2;
	}

	private void solution() throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int piv_size = Integer.parseInt(br.readLine());
		int recursionCount = pivRecursionCount(piv_size);
		System.out.println(recursionCount);
		int dpCount = pivDpCount(piv_size);
		System.out.println(dpCount);
	}

	public static void main(String[] args) throws Exception {
		new Main().solution();
	}

}