import matplotlib.pyplot as plt
import seaborn as sns


if __name__ == '__main__':
    tips = sns.load_dataset('tips')
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))

    culori = {'Male': '#3498db', 'Female': '#e74c3c'}

    for sex, culoare in culori.items():
        subset = tips[tips['sex'] == sex]
        axes[0, 0].scatter(subset['total_bill'], subset['tip'],
        label=sex, color=culoare, alpha=0.7, s=50)
    #Scatter
    axes[0, 0].set_title('Scatter')
    axes[0, 0].set_xlabel('tip')
    axes[0, 0].set_ylabel('total_bill')
    axes[0, 0].grid(True, alpha=0.3)



    sns.boxplot(data=tips, x='day', y='total_bill', ax=axes[0, 1])
    axes[1, 0].set_title('Total bill over days')
    axes[1, 0].set_xlabel('Day')


    sns.histplot(data=tips, x='tip', hue='time',
                 kde=True, bins=15, ax=axes[1, 0])
    axes[1, 0].set_title('Distributia tipsurilor')
    axes[1, 0].set_xlabel('Tips')



    medie_per_zi = tips.groupby('day').mean(numeric_only=True)['tip']
    axes[1, 1].bar(medie_per_zi.index, medie_per_zi.values,
                  color=['#e74c3c', '#3498db', '#2ecc71','#a73c4c'], edgecolor='black',
                  alpha=0.8)

    axes[1, 1].set_title('Barplot')
    axes[1, 1].set_xlabel('Ziua')
    axes[1, 1].set_ylabel('Bacsisul mediu')
    
    
    
    plt.tight_layout()
    plt.savefig('TemaC.png', dpi=150, bbox_inches='tight')
    plt.show()