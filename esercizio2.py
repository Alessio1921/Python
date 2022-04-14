# Search Vocal
print('funzione cerca vocali')

def searchVocal(y):
    if y == "A" or y == "E" or y == "I" or y == "O" or y == "U":
      y = "Il carrattere inserito è una vocale"
    else:
      y = "Il carrattere inserito non è una vocale"  
    return y

x = input('inserisci una lettera o una vocale: ').upper()

print( searchVocal(x))

#  Palindrome Word

print('Funzione cerca parole Palindrome')

def serchPalindrome(wordTemp):
  reverseWord = wordTemp[::-1]
  answer = ""
  if reverseWord == wordTemp:
    answer = "La parola inserita è palindroma!"
  else:
    answer = "La parola inserita non è palindroma!"
  return answer

word = input('inserisci una parola: ').lower()
print(serchPalindrome(word))
