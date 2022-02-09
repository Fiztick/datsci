from preprocessor import load_data

def main():
    pokemon = load_data("dataset/pokemon_alopez247.csv")
    # print(pokemon.keys())

    # grass_poke = pokemon["Type_1"] == "Grass"
    # print(grass_poke)

    grass_pokemon = pokemon.copy().loc[pokemon["Type_1"] == "Grass"]
    
    print(grass_pokemon.sort_values(by="Attack", ascending=False))

    # pokemon["combine"] = pokemon["HP"] - pokemon["Attack"]
    # print(pokemon.loc[:5])

    # print(pokemon.loc[:3, :"HP"])

if __name__ == "__main__":
    main()