weather = input("Whats the weather like today? (sunny/cold/rainy):  ").strip.lower()

match weather:
   case  "sunny":
     print("wear a t-shirt and sunglasses.")
   case  "cold":
     print("make sure to wear a warm coat and a scarf.")
   case  "rainy":
     print("dont forget your umbrella and a raincoat.")
   case _:
    print("sorry.")
if __name__ == "__main__":
    get_weather_advice()