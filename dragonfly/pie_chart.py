import matplotlib.pyplot as plt


def make_chart(num_fixes):
    """creates pie chart visualization of commit data"""
    files = []
    fixes = []
    colors = ['#4477AA', '#66CCEE', '#228833', '#CCBB44', '#EE6677',
              '#AA3377', '#BBBBBB']
    # makes lists of file names and num of fixes/file from dictionary
    try:
        for key, value in num_fixes.items():
            files.append(key)
            fixes.append(value)
    except AttributeError:
        return

    # uses matplotlib to create and label graph and axes
    fig1, ax1 = plt.subplots()
    ax1.pie(fixes, labels=files, colors=colors, autopct='%1.0f%%',
            labeldistance=1.02)
    ax1.axis('equal')
    plt.title('Bug % by File', fontsize=20, pad=20)

    # sets size of chart output and saves to file
    dpi = 200
    width = 1920
    height = 1080
    fig1.set_size_inches(width / dpi, height / dpi)
    fig1.savefig('pie_chart.png', dpi=dpi, bbox_inches='tight')
