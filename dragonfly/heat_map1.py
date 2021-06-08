import matplotlib.pyplot as plt


def make_chart(num_fixes):

    files = []
    fixes = []
    colors = ['#5A69AF', '#579E65', '#F9C784', '#FC944A', '#F24C00', '#00B825']
    for key, value in num_fixes.items():
        files.append(key)
        fixes.append(value)

    fig1, ax1 = plt.subplots()
    ax1.pie(fixes, labels=files, autopct='%1.0f')
    ax1.axis('equal')
    plt.title('Number of bug fixes per file', fontsize=20, pad=20)

    dpi = 200
    width = 1920
    height = 1080
    fig1.set_size_inches(width/dpi, height/dpi)
    fig1.savefig('heat_map1.png', dpi=dpi, bbox_inches='tight')
