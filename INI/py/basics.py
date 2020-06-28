#OPERAZIONI
#somma
1+2
#differenza
5-3
#moltiplicazione
6*7
#elevamento a potenza
3**2
#elevamento a potenza frazionaria (radice)
9**(1/2)
#quoto
20//6
#resto
20%6

#STRINGHE
#apostrofi e virgolette(") vanno inserite con un backslahsh(\)
print('Brian\'s mother: He\'s not the Messiah. He\'s a very naughty boy!')
print("""Customer: Good morning.
Owner: Good morning, Sir. Welcome to the National Cheese Emporium.""")
#come breakrow per andare a capo si usa "\n"
print('hello world\nhi!')
#concatenazione, si usa "+" per unire le stringhe
print("Spam"+'eggs') #'Spameggs'
print("First string" + ", " + "second string") #First string, second string
#la "somma" di stringhe e numeri causa errore
#ricorda di fare attenzione
#le stringhe possono essere moltiplicate per numeri interi
print("spam" * 3)
#spamspamspam
print(4 * '2')
#'2222'
print(0 * '2')
#printa una linea vuota

#INPUT/OUTPUT
#per ottenere un output si usa "print()"
print('hello world')
#per poter inserire dei valori in input si usa "input()"
input("Enter something please: ")
#Enter something please: (This is what\nthe user enters)

#VARIABILI
#per assegnare un valore ad una variabile si usa "="
x=3
print(x+7)
#10
spam="eggs"
print(spam*3)
#eggseggseggs
#le variabili non hanno un tipo specifico; perciò si possono assegnare
#valori diversi alla stessa variabile
x = 123.456
print(x)
#123.456
x = "This is a string"
print(x + "!")
#This is a string!
#comunque non è una buona abitudine poichè potrebbe fare confusione

#NOME DELLE VARIABILI
#sono consentiti solo: LETTERE, NUMERI e UNDERSCORES
#non possono iniziare con un numero
#se così fosse risulterebbe un errore (SyntaxError: invalid syntax)
this_is_a_normal_name=7
#va bene
#123abc=7
#SyntaxError: invalid syntax
#space are not allowed
#SyntaxError: invalid syntax
#Python è CASE SENSITIVE, perciò Lastname e lastname sono due variabili diverse

#VARIABILI ELIMINATE
#Cercando di fare riferimento a una variabile non assegnata a causa di un
#errore.
#È possibile utilizzare l'istruzione "del" per rimuovere una variabile,
#il che significa che il riferimento dal nome al valore viene eliminato
#e il tentativo di utilizzare la variabile causa un errore.
#Le variabili eliminate possono essere riassegnate in un secondo momento.
foo = "a string"
foo
#'a string'
bar
#NameError: name 'bar' is not defined
del foo
foo
#NameError: name 'foo' is not defined

#ACQUISIRE VALORI
#si possono anche acquisire i valori delle variabili dall'utente:
foo = input("Enter a number: ")
#Enter a number: 7
print(foo)
#7
#Le variabili foo e bar sono chiamate variabili metasintattiche,
#nel senso che vengono utilizzate come nomi segnaposto nel codice di
#esempio per dimostrare qualcosa.
