#include <iostream> /*include le varie librerie necessarie
                    (<iostream> va sempre inclusa) */
using namespace std; /*viene utilizzato il namespace standard*/

int main() /*l'esecuzione del programma inizia con questa funzione,
            le "{}" indicano l'inizio e la fine di una funzione,
            tutto ci� che c'� al loro interno sono le istruzioni
            (ci� che la funzione deve fare quando viene eseguita)*/
{
    cout<<"hello world"<<endl; /*la funzione "cout" restituisce in output
                                i valori  che seguono "<<"
                                (alla fine di ogni istruzione �
                                IMPORTANTISSIMO mettere ";"*/
                             /*endl serve per printare nella riga
                                successiva*/
    cout<<"i'm back";
	return 0; /*serve per terminare la funzione*/
}
