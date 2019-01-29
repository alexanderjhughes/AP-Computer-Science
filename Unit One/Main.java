import java.util.Scanner;

class Main {

  public static Scanner scanner = new Scanner(System.in);

  public static void main(String args[]) {
	  //greedy();
	  creditCard();
  }

  public static void greedy() {
	  System.out.println("Enter in your change: ");
	  Double changeTotal = Double.parseDouble(scanner.nextLine());
	  Double change = (double) Math.round((changeTotal%1)*100);
	  int quaters = 0;
	  int dimes = 0;
	  int nickels = 0;
	  int pennies = 0;
	  System.out.println(change);
	  if(change>=25) {
		  quaters = (int) Math.floor(change/25.00);
		  change = change-(quaters*25.00);
	  }
	  if(change>=10) {
		  dimes = (int) Math.floor(change/10.0);
		  change = change-(dimes*10.0);
	  }
	  if(change>=5) {
		  nickels = (int) Math.floor(change/5.0);
		  change = change-(nickels*5.0);
	  }
	  if(change>=1) {
		  pennies = (int) Math.floor(change/1.0);
		  change = change-(pennies*1.0);
	  }
	  System.out.println(quaters + " Quaters, " + dimes + " Dimes, " + nickels + " Nickels, and " + pennies + " Pennies.");
  }
  
  public static void creditCard() {
	  System.out.println("Enter in your credit card number: ");
	  long cardnumber = Long.parseLong(scanner.nextLine());
	  long origcardnumber = cardnumber;
	  int sumOdd = 0;
	  int sumEven = 0;
	  int sum = 0;
	  int pos = 0;
	  while(cardnumber > 0) {
		  long digit = cardnumber % 10;
	      if (pos % 2 == 1) {
	    	  digit *= 2;
	    	  if(String.valueOf(digit).toString().length()==2) {
	    		  sumEven += digit/10 + digit%10;
	    	  } else {
	    		  sumEven += digit;
	    	  }
	      }
	      if (pos % 2 == 0) {
	    	  sumOdd += digit;
	      }
	      cardnumber /= 10;
	      pos++;
	  }
	  sum = sumEven + sumOdd;
	  if (sum%10==0) {
		  System.out.println(prefixName(origcardnumber));
	  } else {
		  System.out.println("INVALID");
	  }
  }
  
  public static String prefixName(long cardnum) {
	  int cardnumlength = String.valueOf(cardnum).length();
	  if (cardnumlength==15) {
		  return "AMEX";
	  }
	  if (cardnumlength==13) {
		  return "VISA";
	  }
	  int firstdigit = Integer.parseInt(Long.toString(cardnum).substring(0, 1));
	  if (firstdigit==4) {
		  return "VISA";
	  }
	  return "MASTERCARD";
  }
}
