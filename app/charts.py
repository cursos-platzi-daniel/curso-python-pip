import matplotlib.pyplot as plt

def generate_bar_chart(name, labels, values):
  fig, ax = plt.subplots()
  plt.gca().invert_xaxis() # Ordenamos de menor a mayor año
  ax.bar(labels, values)
  plt.savefig(f'./imgs/{name}.png')

def generate_pie_chart(labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  ax.axis('equal')
  plt.savefig('./imgs/pie.png')

if __name__ == '__main__':
  labels = ['a', 'b', 'c']
  values = [10, 40, 800]
  generate_bar_chart(labels, values)
  generate_pie_chart(labels, values)