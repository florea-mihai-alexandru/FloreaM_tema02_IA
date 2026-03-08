import seaborn as sns

if __name__ == "__main__":
    tips = sns.load_dataset('tips')

    print(f"Dimensiune: {tips.shape[0]} linii × {tips.shape[1]} coloane")

    print("Tipuri de date ", tips.dtypes)

    print("\n=== Statistici descriptive ===")
    print(tips.describe().round(2))

    medie_per_zi = tips.groupby('day').mean(numeric_only=True).round(2)
    medie_per_specie = tips.groupby('sex').mean(numeric_only=True).round(2)
    print(medie_per_zi)
    print(medie_per_specie)

    copy = tips.copy()
    copy["procent_bacsis"] = copy["tip"] / copy["total_bill"] * 100
    print(copy)

    generoase = copy.nlargest(5, "procent_bacsis")
    print(generoase)

    nr_mese_fumate = tips.groupby(['day', 'smoker']).count()['total_bill']
    print(nr_mese_fumate)

