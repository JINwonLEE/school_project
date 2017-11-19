/** 
  * Combination
  *
  * Lee Jin Won
  *
	*	2016-12-28
*/


#include <iostream>
using namespace std;

int fact( int N );
void comb( int n, int m );

int fact( int N ) {
	if( N==0 ) 
		return 1;
	else 
		return N * fact( N - 1 );
}

void comb( int n, int m ) {
	if ( n == m )
		cout << "1" << endl;
	else if ( n < m ) 
		cout << "wrong!" << endl;
	else {
		int com;
		int x = n - m;
		com = fact( n ) / ( fact( m ) * fact( x ));
		cout << com << endl;
	}
}

int main()
{
	int x, y;
	cin >> x >> y;
	comb(x, y);
	return 0;
}
