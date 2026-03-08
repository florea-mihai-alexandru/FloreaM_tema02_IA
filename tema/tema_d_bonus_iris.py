import matplotlib.pyplot as plt
import seaborn as sns


if __name__ == '__main__':
    iris = sns.load_dataset('iris')
    sns.pairplot(iris, hue='species', diag_kind='kde')
    plt.suptitle('Dataset', y=1.02)
    plt.savefig('TemaDPart1.png', dpi=150, bbox_inches='tight')
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))

    sns.violinplot(data=iris, x='species', y='sepal_length', ax=axes[0,0],hue='species', split=False)
    axes[0,0].set_title('Violinplot — lungimea petalei')

    sns.violinplot(data=iris, x='species', y='sepal_width', ax=axes[0,1],hue='species', split=False)
    axes[0,1].set_title('Violinplot — lungimea petalei')

    sns.violinplot(data=iris, x='species', y='petal_length', ax=axes[1,0],hue='species', split=False)
    axes[1,0].set_title('Violinplot — lungimea petalei')

    sns.violinplot(data=iris, x='species', y='petal_width', ax=axes[1,1],hue='species', split=False)
    axes[1,1].set_title('Violinplot — lungimea petalei')

    plt.tight_layout()
    plt.savefig('TemaDPart1.png', dpi=150, bbox_inches='tight')

    plt.show()