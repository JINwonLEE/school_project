/**
  LEE JIN WON
  checking bracket

	2016-12-28
*/

import java.util.Scanner;
import java.util.*;

public class search_bracket {
	static int count = 1;
	static int length_ = 0;

public static void main(String[] args) {

	Scanner scan = new Scanner(System.in);
	String expre;
	Stack open_bracket_ind = new Stack();
	expre = scan.nextLine();
	length_ = expre.length();
	c_searching(expre, 0, open_bracket_ind);

}


public static void c_searching(String bracket, int index, Stack open_bracket_ind_) {
	if( index == length_ ) {
		return;
	}
	if( bracket.charAt(index) == ')' ) {
		if( open_bracket_ind_.empty() ) {
			System.out.println("Error ");
			return;
		}
		int ind_s = (int) open_bracket_ind_.pop();
		String sub_bracket = bracket.substring(ind_s, index + 1);
		System.out.println("<E" + count + "> => " + sub_bracket);
		count++;
	}
	else if( bracket.charAt(index) == '(' ) {
		open_bracket_ind_.push( new Integer(index) );
	}
	c_searching(bracket, index + 1, open_bracket_ind_);
}



/*
public static void searching(String a){
	String str = a;
	char[] temparr = str.toCharArray();
	int pcount = 0;
	for(int i = 0; i < str.length(); i++){
		try{ String x = expre;} catch (Exception e) {break;}
		 if(temparr[i] ==')'){
			pcount--;
				if(pcount == 0){
					count++;
				System.out.println("<E" + count + "> => " + a);}
		}
		 
		 else if(temparr[i] == '('){
			pcount++;
			String temp = "";
			 int pcount2 = pcount;
			Character cr = null;
			int pst = 0;
			for(int m = i; m< str.length();m++){
				if(temparr[m] == ')'){
				pcount2--;}
				if(pcount2 ==0){
				pst = m;}}
			for(int l = i; l < pst ; l++){
				cr = new Character(temparr[l]);
				temp += cr.toString();}
				searching(temp);
			}
	}
	
}
*/
}

