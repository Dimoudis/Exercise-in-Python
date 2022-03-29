#Εκφωνηση ασκησης

#α) Να γραφεί πρόγραμμα, το οποίο να διαβάζει μία συμβολοσειρά ως είσοδο από τον 
#χρήστη. Να εφαρμοστεί αμυντικός προγραμματισμός ώστε η συμβολοσειρά να μην είναι κενή.

#β) Στη συνέχεια, να τυπώνει τη συμβολοσειρά αφού έχει αφαιρέσει τον χαρακτήρα 
#στη θέση Ν (1 έως και το μήκος της συμβολοσειράς) που θα υποδείξει ο χρήστης. 
#Να εφαρμοστεί αμυντικός προγραμματισμός ώστε η θέση που υποδεικνύει ο χρήστης να είναι έγκυρη.

#γ) Τέλος, να ζητά από τον χρήστη έναν χαρακτήρα και να επιστρέφει το πλήθος και 
#το ποσοστό των εμφανίσεων του συγκεκριμένου χαρακτήρα στην αρχική συμβολοσειρά.

x = input("Παρακαλώ εισάγεται μια συμβολοσειρά:")
n = int(input("Παρακαλώ εισάγετε τη θέση του προς αφαίρεση χαρακτήρα:"))
a = x[0:n-1]
b = x[n:]
print("Η νέα συμβολοσειρά είναι:",a + b)
c = input("Παρακαλώ εισάγετε έναν χαρακτήρα:")
count = 0
for i in x:
    if i == c:
        count += 1
print("Ο χαρακτήρας",c,"εμφανίζεται",count,"φορά/ες.")
pososto = float(count)/float(len(x)) * 100
print("Το ποσοστό των εμφανίσεων του χαρακτήρα",c," στην αρχική συμβολοσειρά ειναi:",pososto,"%")
print("Ολοκληρώθηκε η εκτέλεση του προγράμματος!")
