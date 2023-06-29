def fehrenhitetocelsius(c):
  return c*(9/5)+32

def main():
  print("this program convert fehrenhite to celsius ")
  fehrenhite=float(input("enter a tempreture degree in fehrenhite : "))
  print(f"{fehrenhite}°",fehrenhitetocelsius(fehrenhite),"celsius")

main()